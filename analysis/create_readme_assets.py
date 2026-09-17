"""Create local vector README artwork; badges describe the recorded run, not CI."""
from pathlib import Path
from html import escape
R=Path(__file__).resolve().parents[1]/'assets'
R.mkdir(exist_ok=True)
banner='''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="300" viewBox="0 0 1280 300" role="img" aria-labelledby="title desc">
<title id="title">AI in the knowledge economy — autonomy, capability, and formal proof</title>
<desc id="desc">Ide and Talamàs, 2025. A three-type derivation and a transparent partial Lean formalization.</desc>
<rect width="1280" height="300" rx="16" fill="#122838"/>
<rect x="42" y="38" width="46" height="5" fill="#65d4c1"/>
<g font-family="Inter,Segoe UI,Arial,sans-serif">
<text x="42" y="75" fill="#92aeb9" font-size="15" letter-spacing="3">ECONOMIC MODELING × FORMAL VERIFICATION</text>
<text x="42" y="133" fill="#ffffff" font-size="40" font-weight="700">AI in the knowledge economy</text>
<text x="42" y="175" fill="#65d4c1" font-size="25">Autonomy. Capability. Proof.</text>
<text x="42" y="232" fill="#d1dce1" font-size="17">Ide &amp; Talamàs (2025) · Propositions 5–6 · arXiv v11</text>
<text x="42" y="260" fill="#92aeb9" font-size="15">Three human types. Explicit assumptions. An honest Lean boundary.</text>
<path d="M920 76 L1110 76 L1110 148 L1190 148" fill="none" stroke="#395667" stroke-width="2"/>
<path d="M920 224 L1028 224 L1028 148 L1110 148" fill="none" stroke="#395667" stroke-width="2"/>
<circle cx="920" cy="76" r="22" fill="#1b3d4a" stroke="#65d4c1" stroke-width="2"/>
<circle cx="920" cy="224" r="22" fill="#1b3d4a" stroke="#65d4c1" stroke-width="2"/>
<rect x="1068" y="106" width="84" height="84" rx="10" fill="#65d4c1"/>
<text x="1110" y="151" fill="#122838" font-size="18" font-weight="700" text-anchor="middle">LEAN</text>
<text x="1110" y="171" fill="#122838" font-size="12" text-anchor="middle">CHECKED</text>
<text x="920" y="82" fill="#ffffff" font-size="18" text-anchor="middle">AI</text>
<text x="920" y="230" fill="#ffffff" font-size="18" text-anchor="middle">Time</text>
<circle cx="1190" cy="148" r="5" fill="#65d4c1"/>
</g></svg>'''
(R/'banner.svg').write_text(banner)
for name,label,value,color,w1,w2 in [
 ('source','SOURCE','arXiv v11','#285b7a',76,92),
 ('lean-check','LEAN FAST CHECK','PASS · recorded run','#007f76',142,154),
 ('coverage','LEAN SCOPE','Discrete model','#007f76',106,126),
 ('deck','PRESENTATION','20 minutes','#285b7a',124,102)]:
 total=w1+w2
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{total}" height="28" role="img" aria-label="{escape(label)}: {escape(value)}"><rect width="{total}" height="28" rx="5" fill="{color}"/><path d="M5 0H{w1}V28H5Q0 28 0 23V5Q0 0 5 0" fill="#243d4d"/><g font-family="Segoe UI,Arial,sans-serif" font-size="11" text-anchor="middle" fill="white"><text x="{w1/2}" y="18">{escape(label)}</text><text x="{w1+w2/2}" y="18">{escape(value)}</text></g></svg>'''
 (R/f'badge-{name}.svg').write_text(svg)
