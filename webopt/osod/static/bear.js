/* ══ PIXEL BEAR — Paudronix GT ══ */

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

/* ── 5 frases rotativas ── */
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
        /* ── MODO LOGIN: arriba del card, pequeño ── */
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

        // Burbuja ARRIBA, luego el oso debajo
        loginSlot.appendChild(bubble);
        loginSlot.appendChild(wrap);

        wrap.addEventListener('click', () => mostrar(FRASES[Math.floor(Math.random()*FRASES.length)], 5000));
        wrap.addEventListener('touchend', e => { e.preventDefault(); mostrar(FRASES[Math.floor(Math.random()*FRASES.length)], 5000); });

    } else {
        /* ── MODO PANEL: esquina superior derecha ── */
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
