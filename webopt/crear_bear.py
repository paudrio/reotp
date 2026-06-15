import os, re

CSS = r"""/* ══ PIXEL BEAR ══ */

/* ── MODO LOGIN: arriba del card, centrado ── */
#bear-above-card {
    position: relative;
    width: 280px;
    height: 100px;
    margin-bottom: 10px;
}

#bear-wrap-login {
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    cursor: pointer;
    user-select: none;
}

#bear-head-clip-login {
    width: 62px;
    height: 50px;
    overflow: hidden;
    image-rendering: pixelated;
    filter: drop-shadow(0 4px 16px rgba(139,92,246,0.6));
    animation: bearFloat 3s ease-in-out infinite;
    display: block;
}

/* ── MODO PANEL: esquina superior derecha ── */
#bear-wrap-panel {
    position: fixed;
    top: 0;
    right: 24px;
    z-index: 1000;
    cursor: pointer;
    user-select: none;
}

#bear-head-clip-panel {
    width: 70px;
    height: 54px;
    overflow: hidden;
    image-rendering: pixelated;
    filter: drop-shadow(0 4px 16px rgba(139,92,246,0.6));
    animation: bearFloat 3s ease-in-out infinite;
}

/* ── SVG ── */
@keyframes bearFloat {
    0%,100% { transform: translateY(0); }
    50%     { transform: translateY(-5px); }
}
.bear-svg { display: block; overflow: visible; }

/* ── BLINK ── */
.bear-eye-l, .bear-eye-r {
    transform-box: fill-box;
    transform-origin: center;
    animation: bearBlink 5s ease-in-out infinite;
}
.bear-eye-r { animation-delay: 0.09s; }
@keyframes bearBlink {
    0%,83%,100% { transform: scaleY(1); }
    85%          { transform: scaleY(0.05); }
    87%          { transform: scaleY(1); }
}

/* ── BUBBLE LOGIN ── */
.bear-bubble-login {
    display: none;
    position: absolute;
    bottom: 58px;
    left: 0; right: 0;
    margin: 0 auto;
    width: fit-content;
    background: rgba(14,9,36,0.97);
    border: 2px solid rgba(167,139,250,0.55);
    border-radius: 8px;
    padding: 7px 13px;
    font-family: 'Inter', sans-serif;
    font-size: 0.72rem;
    font-weight: 700;
    color: #ddd0ff;
    text-align: center;
    box-shadow: 0 4px 18px rgba(139,92,246,0.38);
    pointer-events: none;
    white-space: nowrap;
    z-index: 20;
    animation: bubbleIn 0.22s cubic-bezier(0.22,1,0.36,1) both;
}
.bear-bubble-login::after {
    content: '';
    position: absolute;
    bottom: -9px;
    left: 0; right: 0;
    margin: 0 auto;
    width: 0;
    border: 8px solid transparent;
    border-top-color: rgba(167,139,250,0.55);
    border-bottom: none;
}

/* ── BUBBLE PANEL ── */
.bear-bubble-panel {
    display: none;
    position: absolute;
    top: 58px;
    right: 0;
    background: rgba(14,9,36,0.97);
    border: 2px solid rgba(167,139,250,0.55);
    border-radius: 8px 0 8px 8px;
    padding: 7px 13px;
    font-family: 'Inter', sans-serif;
    font-size: 0.74rem;
    font-weight: 700;
    color: #ddd0ff;
    white-space: nowrap;
    box-shadow: 0 4px 18px rgba(139,92,246,0.38);
    pointer-events: none;
    z-index: 1001;
    animation: bubbleIn 0.22s cubic-bezier(0.22,1,0.36,1) both;
}
.bear-bubble-panel::before {
    content: '';
    position: absolute;
    top: -10px; right: 14px;
    border: 8px solid transparent;
    border-bottom-color: rgba(167,139,250,0.55);
    border-top: none;
}

@keyframes bubbleIn {
    from { opacity:0; transform:scale(0.75) translateY(-6px); }
    to   { opacity:1; transform:scale(1)    translateY(0); }
}
.bubble-fade {
    animation: bubbleFade 0.22s ease forwards !important;
}
@keyframes bubbleFade {
    to { opacity:0; transform:scale(0.8) translateY(-4px); }
}
"""

JS = r"""/* ══ PIXEL BEAR — Paudronix GT ══ */

const BEAR_SVG = `
<svg class="bear-svg" viewBox="0 0 90 100"
     xmlns="http://www.w3.org/2000/svg" style="overflow:visible;display:block">
  <rect x="6"  y="0"  width="18" height="20" fill="#8b5a30"/>
  <rect x="10" y="4"  width="10" height="12" fill="#f0a8b8"/>
  <rect x="66" y="0"  width="18" height="20" fill="#8b5a30"/>
  <rect x="70" y="4"  width="10" height="12" fill="#f0a8b8"/>
  <rect x="4"  y="14" width="82" height="52" fill="#c49a6c"/>
  <rect x="4"  y="14" width="82" height="6"  fill="#b8895a"/>
  <rect x="8"  y="40" width="12" height="7"  fill="rgba(230,90,90,0.22)"/>
  <rect x="70" y="40" width="12" height="7"  fill="rgba(230,90,90,0.22)"/>
  <rect x="14" y="24" width="16" height="14" fill="#fff9e8"/>
  <g class="bear-eye-l">
    <rect x="17" y="27" width="9" height="9" fill="#1a0a04"/>
    <rect x="17" y="27" width="3" height="3" fill="white"/>
  </g>
  <rect x="60" y="24" width="16" height="14" fill="#fff9e8"/>
  <g class="bear-eye-r">
    <rect x="63" y="27" width="9" height="9" fill="#1a0a04"/>
    <rect x="63" y="27" width="3" height="3" fill="white"/>
  </g>
  <rect x="24" y="42" width="42" height="20" fill="#f0c880"/>
  <rect x="34" y="44" width="22" height="10" fill="#1a0a04"/>
  <rect x="35" y="45" width="6"  height="4"  fill="#4a2010"/>
  <rect x="28" y="58" width="12" height="3"  fill="#8b5a30"/>
  <rect x="50" y="58" width="12" height="3"  fill="#8b5a30"/>
  <rect x="10" y="64" width="70" height="36" fill="#c49a6c"/>
  <rect x="22" y="68" width="46" height="28" fill="#f0c880"/>
</svg>`;

const FRASES = [
    '¿No tienes acceso? Solicítalo con nuestro soporte 📩',
    '¡Monitoreando OTPs en tiempo real! 📡',
    '¡Accede seguro, tus cuentas protegidas! 🛡️',
    '¡Los códigos llegan automáticamente! ⚡',
    '¡Paudronix GT — OTP Pro al servicio! 🔑',
];

let _bubble   = null;
let _idx      = 0;
let _hideT    = null;

function mostrar(txt, dur) {
    if (!_bubble) return;
    clearTimeout(_hideT);
    _bubble.classList.remove('bubble-fade');
    _bubble.textContent = txt;
    _bubble.style.display = 'block';
    _bubble.style.animation = 'none';
    void _bubble.offsetWidth;
    _bubble.style.animation = '';
    _hideT = setTimeout(() => {
        _bubble.classList.add('bubble-fade');
        setTimeout(() => { if (_bubble) _bubble.style.display = 'none'; }, 240);
    }, dur || 5000);
}

function rotar() {
    mostrar(FRASES[_idx], 5200);
    _idx = (_idx + 1) % FRASES.length;
    setTimeout(rotar, 6000);
}

window.addEventListener('DOMContentLoaded', () => {
    const loginSlot = document.getElementById('bear-above-card');

    if (loginSlot) {
        const wrap = document.createElement('div');
        wrap.id = 'bear-wrap-login';
        wrap.innerHTML = BEAR_SVG;

        const clip = document.createElement('div');
        clip.id = 'bear-head-clip-login';
        clip.appendChild(wrap.querySelector('svg'));
        wrap.insertBefore(clip, wrap.firstChild);

        const bubble = document.createElement('div');
        bubble.className = 'bear-bubble-login';
        _bubble = bubble;

        loginSlot.appendChild(bubble);
        loginSlot.appendChild(wrap);

        wrap.addEventListener('click', () => mostrar(FRASES[Math.floor(Math.random()*FRASES.length)], 5000));
        wrap.addEventListener('touchend', e => { e.preventDefault(); mostrar(FRASES[Math.floor(Math.random()*FRASES.length)], 5000); });

    } else {
        const outer = document.createElement('div');
        outer.id = 'bear-wrap-panel';

        const clip = document.createElement('div');
        clip.id = 'bear-head-clip-panel';
        clip.innerHTML = BEAR_SVG;

        const bubble = document.createElement('div');
        bubble.className = 'bear-bubble-panel';
        _bubble = bubble;

        outer.appendChild(clip);
        outer.appendChild(bubble);
        document.body.appendChild(outer);

        outer.addEventListener('click', () => mostrar(FRASES[Math.floor(Math.random()*FRASES.length)], 5000));
        outer.addEventListener('touchend', e => { e.preventDefault(); mostrar(FRASES[Math.floor(Math.random()*FRASES.length)], 5000); });

        document.addEventListener('bear-otp', () => mostrar('¡Código OTP recibido! 🔑', 4000));
    }

    setTimeout(rotar, 1500);
});
"""

dest = "/opt/otppro/static"
os.makedirs(dest, exist_ok=True)

with open(os.path.join(dest, "bear.css"), "w", encoding="utf-8") as f:
    f.write(CSS)

with open(os.path.join(dest, "bear.js"), "w", encoding="utf-8") as f:
    f.write(JS)

print("bear.css y bear.js creados en", dest)

# ── Parchar template login_choice.html ──
tpl = "/opt/otppro/templates/login_choice.html"
try:
    with open(tpl, "r", encoding="utf-8") as f:
        html = f.read()

    changed = False

    # 1) Agregar bear.css en <head>
    if "bear.css" not in html:
        html = html.replace(
            '<link rel="icon"',
            '<link rel="stylesheet" href="/static/bear.css">\n    <link rel="icon"'
        )
        changed = True

    # 2) Agregar div#bear-above-card antes de la login-card
    if "bear-above-card" not in html:
        html = html.replace(
            '<div class="login-card">',
            '<!-- OSO ARRIBA DEL CARD -->\n        <div id="bear-above-card"></div>\n\n        <!-- CARD -->\n        <div class="login-card">'
        )
        changed = True

    # 3) Agregar bear.js antes de </body>
    if "bear.js" not in html:
        html = html.replace(
            "</body>",
            '    <script src="/static/bear.js"></script>\n</body>'
        )
        changed = True

    if changed:
        with open(tpl, "w", encoding="utf-8") as f:
            f.write(html)
        print("Template login_choice.html actualizado con el oso")
    else:
        print("Template ya tenia el oso — sin cambios")

except Exception as e:
    print("Error al parchar template:", e)

print("Reinicia el servicio: systemctl restart otppro")
