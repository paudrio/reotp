#!/bin/bash
# ══════════════════════════════════════════
#  PAUDRONIX GT — ACTUALIZADOR RAPIDO
#  Ejecuta desde la carpeta webopt del proyecto
#  Uso: sudo bash update.sh
# ══════════════════════════════════════════

set -e

APP_DIR="/opt/otppro"

echo ""
echo "=========================================="
echo "   PAUDRONIX GT - ACTUALIZANDO..."
echo "=========================================="
echo ""

if [ "$EUID" -ne 0 ]; then
    echo "ERROR: Ejecuta como root: sudo bash update.sh"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ ! -f "${SCRIPT_DIR}/app.py" ]; then
    echo "ERROR: No se encontro app.py. Ejecuta desde la carpeta webopt/"
    exit 1
fi

echo "[1/4] Copiando archivos actualizados..."
cp "${SCRIPT_DIR}/app.py"           ${APP_DIR}/
cp -r "${SCRIPT_DIR}/templates"     ${APP_DIR}/
cp -r "${SCRIPT_DIR}/static/"*      ${APP_DIR}/static/ 2>/dev/null || true

# Preservar uploads existentes
mkdir -p ${APP_DIR}/static/uploads
echo "  OK"

echo "[2/4] Instalando nuevas dependencias (si las hay)..."
${APP_DIR}/venv/bin/pip install -r ${SCRIPT_DIR}/requirements.txt -q > /dev/null 2>&1
echo "  OK"

echo "[3/4] Reiniciando servicio..."
systemctl restart otppro
sleep 2
echo "  OK"

echo "[4/4] Verificando estado..."
STATUS=$(systemctl is-active otppro)
echo "  Estado: ${STATUS}"

echo ""
echo "=========================================="
if [ "$STATUS" = "active" ]; then
    echo "   ACTUALIZACION EXITOSA"
else
    echo "   ADVERTENCIA: El servicio no arranco bien"
    echo "   Revisa: sudo journalctl -u otppro -f"
fi
echo "=========================================="
echo ""
