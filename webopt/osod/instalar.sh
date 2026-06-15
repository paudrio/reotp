#!/bin/bash
# ══ OSOD — Actualizar archivos del oso ══
# Ejecuta desde /tmp/osod en el VPS:
#   sudo bash instalar.sh

APP="/opt/otppro"

echo "Copiando archivos..."
cp static/bear.css      $APP/static/bear.css
cp static/bear.js       $APP/static/bear.js
cp templates/login_choice.html $APP/templates/login_choice.html

echo "Reiniciando servicio..."
systemctl restart otppro
sleep 2

STATUS=$(systemctl is-active otppro)
echo "Estado: $STATUS"

if [ "$STATUS" = "active" ]; then
    echo "LISTO — Actualización aplicada."
else
    echo "ERROR — Revisa: sudo journalctl -u otppro -f"
fi
