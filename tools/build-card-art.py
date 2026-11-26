from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / 'assets' / 'upgrades' / 'items'

# Each card receives one purpose-drawn, source-controlled miniature illustration.
# The common metal/glow treatment keeps the set coherent while the silhouettes differ.
ART = {
    'stat-composite-armor': ('#59d9ff', '''
      <path d="M64 13 104 29 99 72 64 105 29 72 24 29Z" fill="url(#metal)" stroke="#c5e8ee" stroke-width="3"/>
      <path d="M64 23 92 34 88 65 64 88 40 65 36 34Z" fill="url(#dark)" stroke="#1b3446" stroke-width="4"/>
      <path d="m64 29 21 9-4 24-17 16-17-16-4-24Z" fill="url(#energy)" stroke="#d6fbff" stroke-width="2"/>
      <path d="m30 33 14 4m40 0 14-4M34 66l12-5m36 0 12 5M48 82l-7 10m39-10 7 10" stroke="#54dfff" stroke-width="4" filter="url(#glow)"/>
      <circle cx="34" cy="31" r="3" fill="#f3fbff"/><circle cx="94" cy="31" r="3" fill="#f3fbff"/><circle cx="64" cy="97" r="3" fill="#f3fbff"/>'''),
    'stat-fire-rate': ('#63e4ff', '''
      <circle cx="64" cy="62" r="40" fill="url(#metal)" stroke="#c3e5ed" stroke-width="3"/>
      <circle cx="64" cy="62" r="29" fill="url(#dark)" stroke="#1c3445" stroke-width="4"/>
      <path d="M64 23 73 48 99 48 79 64 87 89 64 74 41 89 49 64 29 48 55 48Z" fill="#263f4d" stroke="#92adb8" stroke-width="2"/>
      <circle cx="64" cy="62" r="13" fill="url(#energy)" stroke="#e6ffff" stroke-width="3" filter="url(#glow)"/>
      <path d="M64 11v10m0 82v13M13 62h10m82 0h10M28 26l8 8m56 56 8 8m0-72-8 8m-56 56-8 8" stroke="#60e6ff" stroke-width="4"/>
      <path d="M47 16 64 7l17 9" fill="none" stroke="#d5faff" stroke-width="3"/>'''),
    'stat-shield-capacity': ('#58caff', '''
      <path d="M64 12 103 28v31c0 27-17 43-39 58C42 102 25 86 25 59V28Z" fill="url(#metal)" stroke="#d2e8ed" stroke-width="3"/>
      <path d="M64 24 91 35v23c0 19-11 31-27 42-16-11-27-23-27-42V35Z" fill="url(#dark)" stroke="#37566b" stroke-width="3"/>
      <path d="M64 31 80 48 64 83 48 48Z" fill="url(#energy)" stroke="#d6fbff" stroke-width="3" filter="url(#glow)"/>
      <path d="M18 53q-8 9 0 18m92-18q8 9 0 18M28 24l-7 8m79-8 7 8" fill="none" stroke="#5ddcff" stroke-width="4"/>'''),
    'stat-effect-radius': ('#65e2ff', '''
      <circle cx="64" cy="65" r="17" fill="url(#metal)" stroke="#d1e8ee" stroke-width="3"/>
      <circle cx="64" cy="65" r="8" fill="url(#energy)" stroke="#e5ffff" stroke-width="2" filter="url(#glow)"/>
      <path d="M64 42V23l10-8m-10 27 10-7m-10 30h26m-26 0-10 18m10-18-10-18m10 18H38m26 0 10 18m-10-41-10-7" fill="none" stroke="#b7dbe3" stroke-width="5" stroke-linecap="round"/>
      <path d="M31 31a48 48 0 0 0 0 68M97 31a48 48 0 0 1 0 68M20 21a62 62 0 0 0 0 88M108 21a62 62 0 0 1 0 88" fill="none" stroke="#59dfff" stroke-width="3" filter="url(#glow)"/>'''),
    'stat-ore-pickup-radius': ('#62e0ff', '''
      <path d="M37 23v38a27 27 0 0 0 54 0V23l-12 8v30a15 15 0 0 1-30 0V31Z" fill="url(#metal)" stroke="#c6e1e8" stroke-width="3"/>
      <path d="M39 25h15v13H39zm35 0h15v13H74Z" fill="url(#energy)" stroke="#e0ffff" stroke-width="2"/>
      <path d="m31 86 8-13 9 13-9 14Zm50 3 10-18 12 18-12 18Z" fill="#e2a943" stroke="#fff0ac" stroke-width="2"/>
      <path d="M64 76v18m-10-9h20M22 55l8 5m76-5-8 5" stroke="#5be3ff" stroke-width="3" filter="url(#glow)"/>'''),
    'stat-salvage-income': ('#ffc66c', '''
      <path d="M28 50 64 34l36 16v42l-36 19-36-19Z" fill="url(#metal)" stroke="#d5e4e6" stroke-width="3"/>
      <path d="m28 50 36 18 36-18M64 68v43" fill="none" stroke="#273d4c" stroke-width="5"/>
      <path d="m52 49 12-9 12 9-12 8Z" fill="url(#energy)" stroke="#fff1c6" stroke-width="2"/>
      <path d="M64 15V7m-7 10 7-7 7 7M24 37l-9-5m89 5 9-5" fill="none" stroke="#ffc55d" stroke-width="4"/>
      <circle cx="39" cy="78" r="4" fill="#ffd77d"/><circle cx="88" cy="83" r="4" fill="#ffd77d"/>'''),
    'gear-overdrive-core': ('#ffad4f', '''
      <path d="M45 13h38l7 12 14 6v43l-14 7-7 13H45l-7-13-14-7V31l14-6Z" fill="url(#metal)" stroke="#d5e5e7" stroke-width="3"/>
      <path d="M48 29h32l9 9v31l-9 9H48l-9-9V38Z" fill="url(#dark)" stroke="#344858" stroke-width="3"/>
      <path d="m64 35 16 27-16 17-16-17Z" fill="url(#energy)" stroke="#fff0cd" stroke-width="3" filter="url(#glow)"/>
      <path d="M13 49h14m74 0h14M33 17l8 9m54 55 8 9M95 17l-8 9m-54 55-8 9" stroke="#ffaf4b" stroke-width="4"/>'''),
    'gear-equal-exchange': ('#ffb954', '''
      <path d="M64 24v70M26 43h76M64 27 34 43m30-16 30 16" stroke="#c3d4db" stroke-width="6" stroke-linecap="round"/>
      <path d="M27 45 16 69h26ZM101 45 90 69h26Z" fill="url(#metal)" stroke="#d6e8ec" stroke-width="3"/>
      <path d="M21 70q12 13 24 0M95 70q12 13 24 0" fill="none" stroke="#ffbd55" stroke-width="4"/>
      <path d="M51 95h26l9 13H42Z" fill="url(#dark)" stroke="#c5d9df" stroke-width="3"/>
      <circle cx="34" cy="57" r="7" fill="#63dfff"/><circle cx="94" cy="57" r="7" fill="url(#energy)" stroke="#fff2d2" stroke-width="2"/>'''),
    'gear-self-repair-core': ('#82efb0', '''
      <path d="M44 29 64 17l20 12v31L64 72 44 60Z" fill="url(#metal)" stroke="#d2e7e7" stroke-width="3"/>
      <path d="m64 27 12 8v17L64 60 52 52V35Z" fill="url(#energy)" stroke="#dffff0" stroke-width="2" filter="url(#glow)"/>
      <path d="M39 43H22l-7 8 7 8h17m50-16h17l7 8-7 8H89" fill="none" stroke="#a6bac2" stroke-width="5"/>
      <path d="m22 49-7 2 7 8m84-10 7 2-7 8" fill="none" stroke="#75edb0" stroke-width="4"/>
      <path d="m35 82 13-10m45 10L80 72M64 77v22" stroke="#6de8a4" stroke-width="3"/><circle cx="64" cy="100" r="4" fill="#effff4"/>'''),
    'gear-fixed-fire-rate': ('#ffae58', '''
      <path d="M20 42h88v44H20Z" fill="url(#metal)" stroke="#d7e5e8" stroke-width="3"/>
      <path d="M29 51h69v25H29Z" fill="url(#dark)" stroke="#283f50" stroke-width="3"/>
      <circle cx="46" cy="63" r="10" fill="url(#energy)" stroke="#ffe6c1" stroke-width="3"/>
      <path d="M56 63h44m-35-8v16m12-16v16m12-16v16" stroke="#ffae58" stroke-width="4"/>
      <path d="M33 32h62M40 24v16m48-16v16M28 94h72" stroke="#8fa7b3" stroke-width="4"/>
      <circle cx="27" cy="48" r="3" fill="#ffe3b5"/><circle cx="101" cy="80" r="3" fill="#ffe3b5"/>'''),
    'gear-lightweight-frame': ('#6be5ff', '''
      <path d="M64 13 108 43 94 99 64 114 34 99 20 43Z" fill="none" stroke="url(#metal)" stroke-width="12" stroke-linejoin="round"/>
      <path d="M64 23 94 46 84 87 64 99 44 87 34 46Z" fill="url(#dark)" stroke="#6fe4ff" stroke-width="3"/>
      <path d="m64 27 12 29-12 34-12-34Z" fill="url(#energy)" stroke="#ddffff" stroke-width="2"/>
      <path d="M18 32 31 42m79-10-13 10M24 69l15 3m65-3-15 3" stroke="#5edcff" stroke-width="4"/>'''),
    'gear-heavy-armor-frame': ('#67caff', '''
      <path d="M18 34 46 16h36l28 18-9 61-37 17-37-17Z" fill="url(#metal)" stroke="#d8e6e9" stroke-width="4"/>
      <path d="M30 39 49 27h30l19 12-7 45-27 13-27-13Z" fill="url(#dark)" stroke="#465d6b" stroke-width="4"/>
      <path d="M44 45 64 34l20 11-5 27-15 9-15-9Z" fill="url(#energy)" stroke="#dffbff" stroke-width="3"/>
      <path d="M24 51h13m54 0h13M28 77l13-2m42 0 13 2" stroke="#69cfff" stroke-width="5"/>
      <circle cx="29" cy="37" r="3" fill="#f6ffff"/><circle cx="99" cy="37" r="3" fill="#f6ffff"/>'''),
    'gear-pulse-regulator': ('#69dfff', '''
      <path d="M27 24h74v78H27Z" fill="url(#metal)" stroke="#d6e7eb" stroke-width="3"/>
      <path d="M37 34h54v58H37Z" fill="url(#dark)" stroke="#304859" stroke-width="3"/>
      <path d="M43 75h8l6-24 9 40 8-30 7 14h8" fill="none" stroke="#67e5ff" stroke-width="5" filter="url(#glow)"/>
      <circle cx="47" cy="43" r="4" fill="#ffb652"/><circle cx="64" cy="43" r="4" fill="#69e5ff"/><circle cx="81" cy="43" r="4" fill="#ffb652"/>
      <path d="M18 43h9m74 0h9M18 83h9m74 0h9" stroke="#a8c1ca" stroke-width="4"/>'''),
    'gear-exploration-receiver': ('#63d6ff', '''
      <path d="M58 66 35 40 47 28l28 26Z" fill="url(#metal)" stroke="#d7e6e8" stroke-width="3"/>
      <path d="M30 20q-24 24 0 48l31-24Z" fill="url(#dark)" stroke="#a9c2cc" stroke-width="4"/>
      <path d="M31 27q-13 16 0 33l19-16Z" fill="url(#energy)" stroke="#e0ffff" stroke-width="2"/>
      <path d="m61 65 24 24m-25-3 18-18m-8 34 21-21" stroke="#aabec6" stroke-width="6" stroke-linecap="round"/>
      <path d="M90 25q17 14 0 28m9-37q29 23 0 46" fill="none" stroke="#62dfff" stroke-width="3" filter="url(#glow)"/>'''),
    'gear-precision-targeter': ('#6ce2ff', '''
      <path d="M64 15 77 28 94 26 96 43 109 55 99 69 101 87 83 90 72 104 57 96 40 101 35 84 21 75 29 59 25 42 43 37 51 22Z" fill="url(#metal)" stroke="#d9e8ed" stroke-width="3"/>
      <circle cx="64" cy="61" r="26" fill="url(#dark)" stroke="#4d6878" stroke-width="3"/>
      <circle cx="64" cy="61" r="13" fill="url(#energy)" stroke="#e6ffff" stroke-width="3" filter="url(#glow)"/>
      <path d="M64 16v19m0 52v19M20 61h19m50 0h19" stroke="#65e0ff" stroke-width="3"/>
      <circle cx="64" cy="61" r="36" fill="none" stroke="#76dfff" stroke-dasharray="5 5" stroke-width="2"/>'''),
    'gear-area-emitter': ('#ffb850', '''
      <path d="M64 40 84 52v24L64 88 44 76V52Z" fill="url(#metal)" stroke="#d7e5e8" stroke-width="3"/>
      <circle cx="64" cy="64" r="10" fill="url(#energy)" stroke="#fff0cf" stroke-width="2" filter="url(#glow)"/>
      <path d="M40 27a52 52 0 0 0 0 74M88 27a52 52 0 0 1 0 74M28 18a67 67 0 0 0 0 92M100 18a67 67 0 0 1 0 92" fill="none" stroke="#ffb954" stroke-width="4"/>
      <path d="M64 15v18m0 62v18M15 64h18m62 0h18" stroke="#91aab5" stroke-width="5"/>'''),
    'gear-repair-nanobots': ('#7fe9b3', '''
      <path d="M29 49 64 31l35 18v34L64 101 29 83Z" fill="url(#dark)" stroke="#aec6cb" stroke-width="3"/>
      <path d="M47 61 58 49l9 12 9-9 8 12-16 18-12-8-10 8Z" fill="url(#metal)" stroke="#d8e9e7" stroke-width="2"/>
      <path d="m58 49 9 12 9-9m-22 28 12-12" fill="none" stroke="#79edb0" stroke-width="4"/>
      <g fill="url(#energy)" stroke="#e5fff0" stroke-width="2"><circle cx="31" cy="34" r="8"/><circle cx="97" cy="35" r="8"/><circle cx="27" cy="95" r="7"/><circle cx="101" cy="93" r="7"/></g>
      <path d="M35 40 43 49m50-9-8 9M34 91l9-5m43 5-9-5" stroke="#83efb4" stroke-width="3"/>'''),
    'gear-reinforced-shield-cell': ('#68d6ff', '''
      <path d="M64 11 108 29v36c0 27-19 43-44 57C39 108 20 92 20 65V29Z" fill="url(#metal)" stroke="#dbe9ec" stroke-width="4"/>
      <path d="M64 25 94 37v27c0 19-12 31-30 41-18-10-30-22-30-41V37Z" fill="url(#dark)" stroke="#496474" stroke-width="3"/>
      <path d="M64 34 81 51 64 82 47 51Z" fill="url(#energy)" stroke="#e4ffff" stroke-width="3" filter="url(#glow)"/>
      <path d="M17 49h14m66 0h14M24 82l13-5m54 0 13 5" stroke="#6bdbff" stroke-width="5"/>'''),
    'gear-salvage-drone': ('#ffbd57', '''
      <path d="M34 39 64 25l30 14v33L64 88 34 72Z" fill="url(#metal)" stroke="#d8e6e8" stroke-width="3"/>
      <path d="M47 46 64 38l17 8v18L64 75 47 64Z" fill="url(#dark)" stroke="#526a75" stroke-width="3"/>
      <circle cx="64" cy="56" r="8" fill="url(#energy)" stroke="#fff1ca" stroke-width="2"/>
      <path d="M36 47 18 35 10 43l15 20 16 2m51-18 18-12 8 8-15 20-16 2M54 80l-8 13m28-13 8 13" fill="none" stroke="#b6c8ce" stroke-width="5"/>
      <path d="m97 90 8-13 9 13-9 12Z" fill="#ffd36d" stroke="#fff2bd" stroke-width="2"/>'''),
    'gear-magnetic-tractor': ('#5fe0ff', '''
      <path d="M37 25v36a27 27 0 0 0 54 0V25H75v36a11 11 0 0 1-22 0V25Z" fill="url(#metal)" stroke="#d1e5ea" stroke-width="3"/>
      <path d="M36 22h18v18H36Zm38 0h18v18H74Z" fill="url(#energy)" stroke="#e4ffff" stroke-width="2"/>
      <path d="M64 88v12m0-9-15 9m15-9 15 9" stroke="#a8bac2" stroke-width="4"/>
      <path d="m30 85 8-13 9 13-9 13Zm42 11 9-15 10 15-10 14Z" fill="#ffc251" stroke="#fff0bd" stroke-width="2"/>
      <path d="M22 50q-8 12 0 24m84-24q8 12 0 24" fill="none" stroke="#62ddff" stroke-width="3"/>'''),
    'gear-lightweight-fire-module': ('#6de2ff', '''
      <path d="M23 39h82v43H23Z" fill="url(#dark)" stroke="#c0d5dc" stroke-width="3"/>
      <path d="M31 47h66v27H31Z" fill="url(#metal)" stroke="#385566" stroke-width="3"/>
      <circle cx="49" cy="60" r="10" fill="url(#energy)" stroke="#e4ffff" stroke-width="2"/>
      <path d="M60 60h35M67 52v16m12-16v16m12-16v16" stroke="#76e8ff" stroke-width="3"/>
      <path d="M18 31 27 39m74-8-9 8M25 89l12-8m54 0 12 8" stroke="#9fbac4" stroke-width="4"/>
      <path d="M36 25h54" stroke="#6be3ff" stroke-width="3"/>'''),
    'gear-barrier-frame': ('#60d9ff', '''
      <path d="M22 24h18v80H22Zm66 0h18v80H88Z" fill="url(#metal)" stroke="#d5e6e9" stroke-width="3"/>
      <path d="M40 34h48v60H40Z" fill="url(#dark)" stroke="#3c5a69" stroke-width="3"/>
      <path d="M48 40h32v48H48Z" fill="url(#energy)" opacity=".8" stroke="#dffcff" stroke-width="2"/>
      <path d="M40 48h48M40 64h48M40 80h48" stroke="#d9ffff" stroke-width="2" opacity=".8"/>
      <path d="M22 39h18m48 0h18M22 90h18m48 0h18" stroke="#59d9ff" stroke-width="4"/>'''),
    'gear-maintenance-assistant-chip': ('#7ee9b1', '''
      <path d="M34 28h60v68H34Z" fill="url(#metal)" stroke="#d6e8e8" stroke-width="3"/>
      <path d="M43 38h42v48H43Z" fill="url(#dark)" stroke="#46616d" stroke-width="3"/>
      <path d="M52 48h24v22H52Z" fill="url(#energy)" stroke="#dfffee" stroke-width="2"/>
      <path d="M28 40h-9v10h9m66-10h10v10H94M28 74h-9v10h9m66-10h10v10H94M48 22v-9h10v9m20 0v-9h10v9M48 102v9h10v-9m20 0v9h10v-9" fill="none" stroke="#b2c7cc" stroke-width="4"/>
      <path d="m56 59 5 5 12-13" fill="none" stroke="#effff3" stroke-width="4"/>'''),
    'support-counterattack-shield': ('#7de9b4', '''
      <circle cx="64" cy="62" r="43" fill="url(#metal)" stroke="#d5e7e8" stroke-width="4"/>
      <circle cx="64" cy="62" r="31" fill="url(#dark)" stroke="#496674" stroke-width="3"/>
      <path d="M64 38 82 46v15c0 12-7 20-18 27-11-7-18-15-18-27V46Z" fill="url(#energy)" stroke="#e4fff0" stroke-width="3" filter="url(#glow)"/>
      <path d="M11 62h15m76 0h15M64 9v15m0 76v15" stroke="#81efb8" stroke-width="4"/>
      <path d="M20 24q-12 12 0 24m88-24q12 12 0 24M20 76q-12 12 0 24m88-24q12 12 0 24" fill="none" stroke="#d0f8e5" stroke-width="2"/>'''),
    'support-targeting-satellite': ('#68e0ff', '''
      <path d="M48 43 70 65 55 80 33 58Z" fill="url(#metal)" stroke="#d7e7e9" stroke-width="3"/>
      <path d="M29 30 48 43 34 57 18 47Z" fill="url(#dark)" stroke="#83cce0" stroke-width="3"/>
      <path d="M70 65 84 51l21 11-16 18Z" fill="url(#dark)" stroke="#83cce0" stroke-width="3"/>
      <circle cx="61" cy="57" r="9" fill="url(#energy)" stroke="#e1ffff" stroke-width="2"/>
      <path d="M63 65 89 91m-6-2 12-12m-17 6 12-12" stroke="#b4c6ce" stroke-width="4"/>
      <path d="M100 30a26 26 0 0 1 0 34M108 22a38 38 0 0 1 0 50" fill="none" stroke="#69e1ff" stroke-width="3"/>'''),
    'support-ore-collector': ('#83efb0', '''
      <path d="M64 20 100 40v42l-36 22L28 82V40Z" fill="url(#metal)" stroke="#d8e9e7" stroke-width="3"/>
      <circle cx="64" cy="61" r="23" fill="url(#dark)" stroke="#56746f" stroke-width="3"/>
      <circle cx="64" cy="61" r="12" fill="url(#energy)" stroke="#eafff2" stroke-width="2" filter="url(#glow)"/>
      <path d="m33 44 10 5m52-5-10 5M37 78l10-5m44 5-10-5" stroke="#b8d1ce" stroke-width="4"/>
      <path d="m18 32 7-12 8 12-8 12Zm75 1 8-13 9 13-9 13Zm-39 69 8-13 9 13-9 13Z" fill="#ffd06a" stroke="#fff3c2" stroke-width="2"/>'''),
    'item-repair-kit': ('#8debb3', '''
      <path d="M31 39h66v60H31Z" fill="url(#metal)" stroke="#d7e7e8" stroke-width="3"/>
      <path d="M44 29h40v13H44Z" fill="url(#dark)" stroke="#a9c1c8" stroke-width="3"/>
      <path d="M57 49h14v12h12v14H71v12H57V75H45V61h12Z" fill="url(#energy)" stroke="#e6fff0" stroke-width="2" filter="url(#glow)"/>
      <path d="M31 54H19v31h12m66-31h12v31H97" fill="none" stroke="#9eb6c1" stroke-width="4"/>
      <circle cx="39" cy="47" r="3" fill="#effff6"/><circle cx="89" cy="47" r="3" fill="#effff6"/>'''),
    'item-target-link': ('#b994ff', '''
      <circle cx="37" cy="58" r="25" fill="url(#metal)" stroke="#dbd4f4" stroke-width="3"/>
      <circle cx="91" cy="58" r="25" fill="url(#metal)" stroke="#dbd4f4" stroke-width="3"/>
      <circle cx="37" cy="58" r="15" fill="url(#dark)" stroke="#695c8d" stroke-width="3"/>
      <circle cx="91" cy="58" r="15" fill="url(#dark)" stroke="#695c8d" stroke-width="3"/>
      <circle cx="37" cy="58" r="6" fill="#61dfff" filter="url(#glow)"/><circle cx="91" cy="58" r="6" fill="#c29aff" filter="url(#glow)"/>
      <path d="M56 58h16m-8-7 8 7-8 7M37 21v11m0 52v11m54-74v11m0 52v11" fill="none" stroke="#c5b0ff" stroke-width="4"/>
      <path d="M57 42q16-18 29 0M57 74q16 18 29 0" fill="none" stroke="#8cddff" stroke-width="3"/>'''),
}

TEMPLATE = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" role="img">
<defs>
 <linearGradient id="metal" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#c3d0d1"/><stop offset=".23" stop-color="#667d88"/><stop offset=".56" stop-color="#263b4b"/><stop offset=".82" stop-color="#152635"/><stop offset="1" stop-color="#91a9b0"/></linearGradient>
 <linearGradient id="dark" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#1c3344"/><stop offset=".56" stop-color="#0b1826"/><stop offset="1" stop-color="#314a55"/></linearGradient>
 <linearGradient id="energy" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{accent}"/><stop offset=".48" stop-color="#f1ffff"/><stop offset="1" stop-color="{accent}"/></linearGradient>
 <filter id="glow" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
 <filter id="shade" x="-30%" y="-30%" width="160%" height="180%"><feGaussianBlur in="SourceAlpha" stdDeviation="2" result="blur"/><feOffset dy="3"/><feComponentTransfer><feFuncA type="linear" slope=".52"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<ellipse cx="64" cy="111" rx="34" ry="6" fill="#030913" opacity=".45"/>
<g filter="url(#shade)" stroke-linejoin="round" stroke-linecap="round">{body}</g>
</svg>'''

OUT.mkdir(parents=True, exist_ok=True)
for slug, (accent, body) in ART.items():
    (OUT / f'{slug}.svg').write_text(TEMPLATE.format(accent=accent, body=body), encoding='utf-8')
print(f'Wrote {len(ART)} unique card illustrations to {OUT}')
