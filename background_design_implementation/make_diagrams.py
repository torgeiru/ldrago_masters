import cairosvg, os

svgs = {}

# ── 1. Avail Ring Enqueue ────────────────────────────────────────────────────
svgs["avail_enqueue"] = """<svg width="680" height="190" viewBox="0 0 680 190" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#185FA5" stroke-width="1.5" stroke-linecap="round"/></marker></defs>
<rect width="680" height="190" fill="white"/>
<rect x="20" y="16" width="110" height="158" rx="6" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.8"/>
<rect x="20" y="16" width="110" height="28" rx="6" fill="#378ADD" stroke="#185FA5" stroke-width="0.8"/>
<rect x="20" y="40" width="110" height="4" fill="#378ADD"/>
<text x="75" y="34" text-anchor="middle" font-family="Helvetica" font-size="13" font-weight="bold" fill="white">Avail</text>
<rect x="20" y="44" width="110" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="75" y="60" text-anchor="middle" font-family="Courier" font-size="11" fill="#185FA5">idx</text>
<rect x="20" y="68" width="110" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="75" y="84" text-anchor="middle" font-family="Courier" font-size="11" fill="#185FA5">0</text>
<rect x="20" y="92" width="110" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="75" y="108" text-anchor="middle" font-family="Courier" font-size="11" fill="#185FA5">ring[]</text>
<rect x="20" y="116" width="110" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="75" y="132" text-anchor="middle" font-family="Courier" font-size="11" fill="#185FA5">0</text>
<rect x="20" y="140" width="110" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="75" y="156" text-anchor="middle" font-family="Courier" font-size="11" fill="#185FA5">...</text>
<path d="M 172,16 Q 166,16 166,22 L 166,44 L 660,44 L 660,22 Q 660,16 654,16 Z" fill="#378ADD" stroke="#185FA5" stroke-width="0.8"/>
<rect x="200" y="40" width="460" height="4" fill="#378ADD"/>
<text x="430" y="34" text-anchor="middle" font-family="Helvetica" font-size="13" font-weight="bold" fill="white">Descriptor area</text>
<rect x="166" y="44" width="115" height="24" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="239" y="60" text-anchor="middle" font-family="Helvetica" font-size="11" fill="white">Buffer</text>
<rect x="281" y="44" width="86" height="24" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="324" y="60" text-anchor="middle" font-family="Helvetica" font-size="11" fill="white">Len</text>
<rect x="367" y="44" width="86" height="24" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="410" y="60" text-anchor="middle" font-family="Helvetica" font-size="11" fill="white">Flags</text>
<rect x="453" y="44" width="207" height="24" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="556" y="60" text-anchor="middle" font-family="Helvetica" font-size="11" fill="white">Next</text>
<rect x="166" y="68" width="115" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="239" y="84" text-anchor="middle" font-family="Courier" font-size="11" fill="#185FA5">0x8000</text>
<rect x="281" y="68" width="86" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="324" y="84" text-anchor="middle" font-family="Courier" font-size="11" fill="#185FA5">2000</text>
<rect x="367" y="68" width="86" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="410" y="84" text-anchor="middle" font-family="Courier" font-size="11" fill="#185FA5">W</text>
<rect x="453" y="68" width="207" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="556" y="84" text-anchor="middle" font-family="Courier" font-size="11" fill="#185FA5">0</text>
<rect x="166" y="92" width="494" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="413" y="108" text-anchor="middle" font-family="Courier" font-size="11" fill="#185FA5">...</text>
<line x1="130" y1="128" x2="164" y2="82" stroke="#185FA5" stroke-width="1.3" marker-end="url(#a)"/>
<text x="340" y="152" text-anchor="middle" font-family="Helvetica" font-size="10" fill="#5F5E5A">Driver places descriptor chain head index 0 into ring[0]</text>
</svg>"""

# ── 2. Avail Ring Expose ─────────────────────────────────────────────────────
svgs["avail_expose"] = """<svg width="680" height="190" viewBox="0 0 680 190" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#185FA5" stroke-width="1.5" stroke-linecap="round"/></marker>
<marker id="g" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#0F6E56" stroke-width="1.5" stroke-linecap="round"/></marker>
</defs>
<rect width="680" height="190" fill="white"/>
<rect x="20" y="16" width="110" height="158" rx="6" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.8"/>
<rect x="20" y="16" width="110" height="28" rx="6" fill="#378ADD" stroke="#185FA5" stroke-width="0.8"/>
<rect x="20" y="40" width="110" height="4" fill="#378ADD"/>
<text x="75" y="34" text-anchor="middle" font-family="Helvetica" font-size="13" font-weight="bold" fill="white">Avail</text>
<rect x="20" y="44" width="110" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="75" y="60" text-anchor="middle" font-family="Courier" font-size="11" fill="#185FA5">idx</text>
<rect x="20" y="68" width="110" height="24" fill="#1D9E75" stroke="#0F6E56" stroke-width="0.8"/>
<text x="75" y="84" text-anchor="middle" font-family="Courier" font-size="11" font-weight="bold" fill="white">1</text>
<rect x="20" y="92" width="110" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="75" y="108" text-anchor="middle" font-family="Courier" font-size="11" fill="#185FA5">ring[]</text>
<rect x="20" y="116" width="110" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="75" y="132" text-anchor="middle" font-family="Courier" font-size="11" fill="#185FA5">0</text>
<rect x="20" y="140" width="110" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="75" y="156" text-anchor="middle" font-family="Courier" font-size="11" fill="#185FA5">...</text>

<path d="M 172,16 Q 166,16 166,22 L 166,44 L 660,44 L 660,22 Q 660,16 654,16 Z" fill="#378ADD" stroke="#185FA5" stroke-width="0.8"/>
<rect x="200" y="40" width="460" height="4" fill="#378ADD"/>
<text x="430" y="34" text-anchor="middle" font-family="Helvetica" font-size="13" font-weight="bold" fill="white">Descriptor area</text>
<rect x="166" y="44" width="115" height="24" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="239" y="60" text-anchor="middle" font-family="Helvetica" font-size="11" fill="white">Buffer</text>
<rect x="281" y="44" width="86" height="24" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="324" y="60" text-anchor="middle" font-family="Helvetica" font-size="11" fill="white">Len</text>
<rect x="367" y="44" width="86" height="24" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="410" y="60" text-anchor="middle" font-family="Helvetica" font-size="11" fill="white">Flags</text>
<rect x="453" y="44" width="207" height="24" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="556" y="60" text-anchor="middle" font-family="Helvetica" font-size="11" fill="white">Next</text>
<rect x="166" y="68" width="115" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="239" y="84" text-anchor="middle" font-family="Courier" font-size="11" fill="#185FA5">0x8000</text>
<rect x="281" y="68" width="86" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="324" y="84" text-anchor="middle" font-family="Courier" font-size="11" fill="#185FA5">2000</text>
<rect x="367" y="68" width="86" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="410" y="84" text-anchor="middle" font-family="Courier" font-size="11" fill="#185FA5">W</text>
<rect x="453" y="68" width="207" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="556" y="84" text-anchor="middle" font-family="Courier" font-size="11" fill="#185FA5">0</text>
<rect x="166" y="92" width="494" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="413" y="108" text-anchor="middle" font-family="Courier" font-size="11" fill="#185FA5">...</text>
<line x1="130" y1="128" x2="164" y2="82" stroke="#185FA5" stroke-width="1.3" marker-end="url(#a)"/>
<text x="340" y="152" text-anchor="middle" font-family="Helvetica" font-size="10" fill="#5F5E5A">Driver increments idx to 1, exposing the request to the device</text>
</svg>"""

# ── 3. Used Ring Enqueue ─────────────────────────────────────────────────────
svgs["used_enqueue"] = """<svg width="680" height="190" viewBox="0 0 680 190" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#185FA5" stroke-width="1.5" stroke-linecap="round"/></marker></defs>
<rect width="680" height="190" fill="white"/>
<rect x="10" y="16" width="100" height="158" rx="6" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.8"/>
<rect x="10" y="16" width="100" height="28" rx="6" fill="#378ADD" stroke="#185FA5" stroke-width="0.8"/>
<rect x="10" y="40" width="100" height="4" fill="#378ADD"/>
<text x="60" y="34" text-anchor="middle" font-family="Helvetica" font-size="12" font-weight="bold" fill="white">Avail</text>
<rect x="10" y="44" width="100" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="60" y="60" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">idx</text>
<rect x="10" y="68" width="100" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="60" y="84" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">1</text>
<rect x="10" y="92" width="100" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="60" y="108" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">ring[]</text>
<rect x="10" y="116" width="100" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="60" y="132" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">0</text>
<rect x="10" y="140" width="100" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="60" y="156" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">...</text>
<path d="M 164,16 Q 158,16 158,22 L 158,44 L 522,44 L 522,22 Q 522,16 516,16 Z" fill="#378ADD" stroke="#185FA5" stroke-width="0.8"/>
<rect x="158" y="40" width="364" height="4" fill="#378ADD"/>
<text x="340" y="34" text-anchor="middle" font-family="Helvetica" font-size="12" font-weight="bold" fill="white">Descriptor area</text>
<rect x="158" y="44" width="91" height="24" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="203" y="60" text-anchor="middle" font-family="Helvetica" font-size="10" fill="white">Buffer</text>
<rect x="249" y="44" width="68" height="24" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="283" y="60" text-anchor="middle" font-family="Helvetica" font-size="10" fill="white">Len</text>
<rect x="317" y="44" width="68" height="24" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="351" y="60" text-anchor="middle" font-family="Helvetica" font-size="10" fill="white">Flags</text>
<rect x="385" y="44" width="137" height="24" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="453" y="60" text-anchor="middle" font-family="Helvetica" font-size="10" fill="white">Next</text>
<rect x="158" y="68" width="91" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="203" y="84" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">0x8000</text>
<rect x="249" y="68" width="68" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="283" y="84" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">2000</text>
<rect x="317" y="68" width="68" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="351" y="84" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">W</text>
<rect x="385" y="68" width="137" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="453" y="84" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">0</text>
<rect x="158" y="92" width="364" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="340" y="108" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">...</text>
<rect x="570" y="16" width="100" height="158" rx="6" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.8"/>
<rect x="570" y="16" width="100" height="28" rx="6" fill="#378ADD" stroke="#185FA5" stroke-width="0.8"/>
<rect x="570" y="40" width="100" height="4" fill="#378ADD"/>
<text x="620" y="34" text-anchor="middle" font-family="Helvetica" font-size="12" font-weight="bold" fill="white">Used</text>
<rect x="570" y="44" width="100" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="620" y="60" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">idx</text>
<rect x="570" y="68" width="100" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="620" y="84" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">0</text>
<rect x="570" y="92" width="100" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="620" y="108" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">ring[]</text>
<rect x="570" y="116" width="100" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="620" y="132" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">0</text>
<rect x="570" y="140" width="100" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="620" y="156" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">...</text>
<line x1="110" y1="128" x2="156" y2="82" stroke="#185FA5" stroke-width="1.3" marker-end="url(#a)"/>
<line x1="568" y1="128" x2="522" y2="82" stroke="#185FA5" stroke-width="1.3" marker-end="url(#a)"/>
<text x="340" y="152" text-anchor="middle" font-family="Helvetica" font-size="10" fill="#5F5E5A">Device writes completed descriptor head index into used ring[0]</text>
</svg>"""

# ── 4. Used Ring Expose ──────────────────────────────────────────────────────
svgs["used_expose"] = """<svg width="680" height="190" viewBox="0 0 680 190" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#185FA5" stroke-width="1.5" stroke-linecap="round"/></marker>
<marker id="g" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#0F6E56" stroke-width="1.5" stroke-linecap="round"/></marker>
</defs>
<rect width="680" height="190" fill="white"/>
<rect x="10" y="16" width="100" height="158" rx="6" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.8"/>
<rect x="10" y="16" width="100" height="28" rx="6" fill="#378ADD" stroke="#185FA5" stroke-width="0.8"/>
<rect x="10" y="40" width="100" height="4" fill="#378ADD"/>
<text x="60" y="34" text-anchor="middle" font-family="Helvetica" font-size="12" font-weight="bold" fill="white">Avail</text>
<rect x="10" y="44" width="100" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="60" y="60" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">idx</text>
<rect x="10" y="68" width="100" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="60" y="84" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">1</text>
<rect x="10" y="92" width="100" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="60" y="108" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">ring[]</text>
<rect x="10" y="116" width="100" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="60" y="132" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">0</text>
<rect x="10" y="140" width="100" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="60" y="156" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">...</text>
<path d="M 164,16 Q 158,16 158,22 L 158,44 L 522,44 L 522,22 Q 522,16 516,16 Z" fill="#378ADD" stroke="#185FA5" stroke-width="0.8"/>
<rect x="158" y="40" width="364" height="4" fill="#378ADD"/>
<text x="340" y="34" text-anchor="middle" font-family="Helvetica" font-size="12" font-weight="bold" fill="white">Descriptor area</text>
<rect x="158" y="44" width="91" height="24" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="203" y="60" text-anchor="middle" font-family="Helvetica" font-size="10" fill="white">Buffer</text>
<rect x="249" y="44" width="68" height="24" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="283" y="60" text-anchor="middle" font-family="Helvetica" font-size="10" fill="white">Len</text>
<rect x="317" y="44" width="68" height="24" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="351" y="60" text-anchor="middle" font-family="Helvetica" font-size="10" fill="white">Flags</text>
<rect x="385" y="44" width="137" height="24" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="453" y="60" text-anchor="middle" font-family="Helvetica" font-size="10" fill="white">Next</text>
<rect x="158" y="68" width="91" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="203" y="84" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">0x8000</text>
<rect x="249" y="68" width="68" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="283" y="84" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">2000</text>
<rect x="317" y="68" width="68" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="351" y="84" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">W</text>
<rect x="385" y="68" width="137" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="453" y="84" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">0</text>
<rect x="158" y="92" width="364" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="340" y="108" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">...</text>
<rect x="570" y="16" width="100" height="158" rx="6" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.8"/>
<rect x="570" y="16" width="100" height="28" rx="6" fill="#378ADD" stroke="#185FA5" stroke-width="0.8"/>
<rect x="570" y="40" width="100" height="4" fill="#378ADD"/>
<text x="620" y="34" text-anchor="middle" font-family="Helvetica" font-size="12" font-weight="bold" fill="white">Used</text>
<rect x="570" y="44" width="100" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="620" y="60" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">idx</text>
<rect x="570" y="68" width="100" height="24" fill="#1D9E75" stroke="#0F6E56" stroke-width="0.8"/>
<text x="620" y="84" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="white">1</text>
<rect x="570" y="92" width="100" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="620" y="108" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">ring[]</text>
<rect x="570" y="116" width="100" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="620" y="132" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">0</text>
<rect x="570" y="140" width="100" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="620" y="156" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">...</text>

<line x1="110" y1="128" x2="156" y2="82" stroke="#185FA5" stroke-width="1.3" marker-end="url(#a)"/>
<line x1="568" y1="128" x2="522" y2="82" stroke="#185FA5" stroke-width="1.3" marker-end="url(#a)"/>
<text x="340" y="152" text-anchor="middle" font-family="Helvetica" font-size="10" fill="#5F5E5A">Device increments used idx to 1, signalling completion to the driver</text>
</svg>"""

# ── 4b. Descriptor Chaining ───────────────────────────────────────────────────
svgs["desc_chain"] = """<svg width="680" height="210" viewBox="0 0 680 210" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#185FA5" stroke-width="1.5" stroke-linecap="round"/></marker>
<marker id="g" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#0F6E56" stroke-width="1.5" stroke-linecap="round"/></marker>
</defs>
<rect width="680" height="210" fill="white"/>
<!-- LEFT: Avail ring -->
<rect x="10" y="16" width="100" height="148" rx="6" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.8"/>
<rect x="10" y="16" width="100" height="28" rx="6" fill="#378ADD" stroke="#185FA5" stroke-width="0.8"/>
<rect x="10" y="40" width="100" height="4" fill="#378ADD"/>
<text x="60" y="34" text-anchor="middle" font-family="Helvetica" font-size="12" font-weight="bold" fill="white">Avail</text>
<rect x="10" y="44" width="100" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="60" y="60" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">idx</text>
<rect x="10" y="68" width="100" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="60" y="84" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">1</text>
<rect x="10" y="92" width="100" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="60" y="108" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">ring[]</text>
<rect x="10" y="116" width="100" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="60" y="132" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">0</text>
<rect x="10" y="140" width="100" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="60" y="156" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">...</text>
<!-- MIDDLE: Descriptor area header (same geometry as used_expose) -->
<path d="M 164,16 Q 158,16 158,22 L 158,44 L 522,44 L 522,22 Q 522,16 516,16 Z" fill="#378ADD" stroke="#185FA5" stroke-width="0.8"/>
<rect x="158" y="40" width="364" height="4" fill="#378ADD"/>
<text x="340" y="34" text-anchor="middle" font-family="Helvetica" font-size="12" font-weight="bold" fill="white">Descriptor area</text>
<!-- Column headers -->
<rect x="158" y="44" width="91" height="24" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="203" y="60" text-anchor="middle" font-family="Helvetica" font-size="10" fill="white">Buffer</text>
<rect x="249" y="44" width="58" height="24" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="278" y="60" text-anchor="middle" font-family="Helvetica" font-size="10" fill="white">Len</text>
<rect x="307" y="44" width="80" height="24" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="347" y="60" text-anchor="middle" font-family="Helvetica" font-size="10" fill="white">Flags</text>
<rect x="387" y="44" width="135" height="24" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="454" y="60" text-anchor="middle" font-family="Helvetica" font-size="10" fill="white">Next</text>
<!-- Desc 0 (y=68) — chain head, NEXT flag -->
<rect x="158" y="68" width="91" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="203" y="84" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">0x1000</text>
<rect x="249" y="68" width="58" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="278" y="84" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">48</text>
<rect x="307" y="68" width="80" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="347" y="84" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">NEXT</text>
<rect x="387" y="68" width="135" height="24" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="454" y="84" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="white">1</text>
<!-- Desc 1 (y=92) — NEXT|W -->
<rect x="158" y="92" width="91" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="203" y="108" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">0x2000</text>
<rect x="249" y="92" width="58" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="278" y="108" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">256</text>
<rect x="307" y="92" width="80" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="347" y="108" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">W|NEXT</text>
<rect x="387" y="92" width="135" height="24" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="454" y="108" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="white">2</text>
<!-- Desc 2 (y=116) — end of chain, W only -->
<rect x="158" y="116" width="91" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="203" y="132" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">0x3000</text>
<rect x="249" y="116" width="58" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="278" y="132" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">4096</text>
<rect x="307" y="116" width="80" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="347" y="132" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">W</text>
<rect x="387" y="116" width="135" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="454" y="132" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">&#x2014;</text>
<!-- "..." row -->
<rect x="158" y="140" width="364" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="340" y="156" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">...</text>
<!-- RIGHT: Used ring -->
<rect x="570" y="16" width="100" height="148" rx="6" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.8"/>
<rect x="570" y="16" width="100" height="28" rx="6" fill="#378ADD" stroke="#185FA5" stroke-width="0.8"/>
<rect x="570" y="40" width="100" height="4" fill="#378ADD"/>
<text x="620" y="34" text-anchor="middle" font-family="Helvetica" font-size="12" font-weight="bold" fill="white">Used</text>
<rect x="570" y="44" width="100" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="620" y="60" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">idx</text>
<rect x="570" y="68" width="100" height="24" fill="#1D9E75" stroke="#0F6E56" stroke-width="0.8"/>
<text x="620" y="84" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="white">1</text>
<rect x="570" y="92" width="100" height="24" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.5"/>
<text x="620" y="108" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">ring[]</text>
<rect x="570" y="116" width="100" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="620" y="132" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">0</text>
<rect x="570" y="140" width="100" height="24" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="620" y="156" text-anchor="middle" font-family="Courier" font-size="10" fill="#185FA5">...</text>
<!-- Avail ring[0]=0 → desc 0 head -->
<line x1="110" y1="128" x2="156" y2="82" stroke="#185FA5" stroke-width="1.3" marker-end="url(#a)"/>
<!-- Used ring[0]=0 → desc 0 head -->
<line x1="568" y1="128" x2="522" y2="82" stroke="#185FA5" stroke-width="1.3" marker-end="url(#a)"/>
<!-- Caption -->
<text x="340" y="192" text-anchor="middle" font-family="Helvetica" font-size="10" fill="#5F5E5A">Descriptor chaining: Next field links desc 0&#x2192;1&#x2192;2 into one logical buffer; avail ring[0] holds the chain head index</text>
</svg>"""

# ── 5. VirtioFS Static Component Overview ────────────────────────────────────
svgs["virtiofs_static"] = """<svg width="680" height="510" viewBox="0 0 680 510" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#185FA5" stroke-width="1.5" stroke-linecap="round"/></marker>
<marker id="g" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#0F6E56" stroke-width="1.5" stroke-linecap="round"/></marker>
</defs>
<rect width="680" height="510" fill="white"/>

<!-- User Space (taller to hold two peer boxes) -->
<rect x="10" y="10" width="658" height="316" rx="16" fill="#EEF4FB" stroke="#85B7EB" stroke-width="1"/>
<text x="30" y="36" font-family="Helvetica" font-size="11" font-weight="bold" fill="#185FA5">User space</text>

<!-- QEMU Process (peer 1) -->
<rect x="26" y="48" width="624" height="138" rx="10" fill="#DAEAF8" stroke="#85B7EB" stroke-width="0.8"/>
<text x="44" y="68" font-family="Helvetica" font-size="10" fill="#185FA5">QEMU process</text>

<!-- Guest VM -->
<rect x="42" y="76" width="606" height="100" rx="8" fill="#EEF4FB" stroke="#378ADD" stroke-width="0.8"/>
<text x="58" y="95" font-family="Helvetica" font-size="10" fill="#185FA5">Guest VM</text>

<!-- VirtioFS Driver chip -->
<rect x="58" y="102" width="130" height="52" rx="6" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="123" y="122" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">VirtioFS</text>
<text x="123" y="140" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E6F1FB">guest driver</text>

<!-- Shared Memory guest chip -->
<rect x="222" y="102" width="408" height="52" rx="6" fill="#042C53" stroke="#185FA5" stroke-width="0.5"/>
<text x="426" y="132" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">Shared memory</text>

<!-- arrow driver -> shared mem -->
<line x1="188" y1="128" x2="220" y2="128" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>

<!-- VirtioFSD Process (peer 2 — same level as QEMU) -->
<rect x="26" y="200" width="624" height="116" rx="10" fill="#DAEAF8" stroke="#85B7EB" stroke-width="0.8"/>
<text x="44" y="220" font-family="Helvetica" font-size="10" fill="#185FA5">VirtioFSD process</text>

<!-- Shared memory VirtioFSD chip -->
<rect x="42" y="228" width="590" height="52" rx="6" fill="#042C53" stroke="#185FA5" stroke-width="0.5"/>
<text x="337" y="258" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">Shared memory</text>

<!-- Bidirectional dashed arrows between the two shared memory chips -->
<line x1="432" y1="154" x2="432" y2="228" stroke="#378ADD" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#a)"/>
<line x1="420" y1="228" x2="420" y2="154" stroke="#378ADD" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#a)"/>

<!-- Kernel Space -->
<rect x="10" y="338" width="658" height="160" rx="16" fill="#EDF7F3" stroke="#5DCAA5" stroke-width="1"/>
<text x="30" y="362" font-family="Helvetica" font-size="11" font-weight="bold" fill="#0F6E56">Kernel space</text>

<!-- VFS subsystem — dark teal component -->
<rect x="26" y="374" width="196" height="112" rx="10" fill="#1D9E75" stroke="#0F6E56" stroke-width="0.8"/>
<text x="124" y="428" text-anchor="middle" font-family="Helvetica" font-size="12" font-weight="bold" fill="white">VFS subsystem</text>

<!-- File system drivers container -->
<rect x="236" y="374" width="196" height="112" rx="10" fill="#D4F0E5" stroke="#5DCAA5" stroke-width="0.8"/>
<text x="334" y="394" text-anchor="middle" font-family="Helvetica" font-size="10" fill="#0F6E56">File system drivers</text>
<rect x="252" y="402" width="74" height="40" rx="6" fill="#1D9E75" stroke="#0F6E56" stroke-width="0.5"/>
<text x="289" y="426" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">EXT4</text>
<rect x="342" y="402" width="74" height="40" rx="6" fill="#1D9E75" stroke="#0F6E56" stroke-width="0.5"/>
<text x="379" y="426" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">XFS</text>

<!-- KVM kernel module — dark teal component -->
<rect x="446" y="374" width="196" height="112" rx="10" fill="#1D9E75" stroke="#0F6E56" stroke-width="0.8"/>
<text x="544" y="428" text-anchor="middle" font-family="Helvetica" font-size="12" font-weight="bold" fill="white">KVM kernel module</text>

<!-- Bidirectional arrows: VFS subsystem <-> File system drivers -->
<line x1="222" y1="424" x2="234" y2="424" stroke="#0F6E56" stroke-width="1.2" marker-end="url(#g)"/>
<line x1="234" y1="438" x2="222" y2="438" stroke="#0F6E56" stroke-width="1.2" marker-end="url(#g)"/>

<!-- separator line -->
<line x1="10" y1="334" x2="670" y2="334" stroke="#aaa" stroke-width="0.5" stroke-dasharray="5 4"/>
</svg>"""

# ── 6. VirtioFS Sequence Diagram ─────────────────────────────────────────────
svgs["virtiofs_sequence"] = """<svg width="680" height="560" viewBox="0 0 680 560" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#185FA5" stroke-width="1.5" stroke-linecap="round"/></marker>
<marker id="t" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#0F6E56" stroke-width="1.5" stroke-linecap="round"/></marker>
<marker id="d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#85B7EB" stroke-width="1.5" stroke-linecap="round"/></marker>
</defs>
<rect width="680" height="560" fill="white"/>
<!-- Actor boxes -->
<rect x="10" y="10" width="90" height="44" rx="6" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="55" y="35" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">Guest VFS</text>
<rect x="128" y="10" width="106" height="44" rx="6" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="181" y="29" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">VirtioFS</text>
<text x="181" y="47" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E6F1FB">guest driver</text>
<rect x="272" y="10" width="76" height="44" rx="6" fill="#1D9E75" stroke="#0F6E56" stroke-width="0.5"/>
<text x="310" y="35" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">KVM</text>
<rect x="386" y="10" width="96" height="44" rx="6" fill="#1D9E75" stroke="#0F6E56" stroke-width="0.5"/>
<text x="434" y="35" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">VirtioFSD</text>
<rect x="520" y="10" width="96" height="44" rx="6" fill="#1D9E75" stroke="#0F6E56" stroke-width="0.5"/>
<text x="568" y="35" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">Host VFS</text>
<!-- Lifelines -->
<line x1="55" y1="54" x2="55" y2="540" stroke="#85B7EB" stroke-width="0.5" stroke-dasharray="4 4"/>
<line x1="181" y1="54" x2="181" y2="540" stroke="#85B7EB" stroke-width="0.5" stroke-dasharray="4 4"/>
<line x1="310" y1="54" x2="310" y2="540" stroke="#5DCAA5" stroke-width="0.5" stroke-dasharray="4 4"/>
<line x1="434" y1="54" x2="434" y2="540" stroke="#5DCAA5" stroke-width="0.5" stroke-dasharray="4 4"/>
<line x1="568" y1="54" x2="568" y2="540" stroke="#5DCAA5" stroke-width="0.5" stroke-dasharray="4 4"/>
<!-- Activation bars -->
<rect x="51" y="78" width="8" height="432" rx="2" fill="#DAEAF8" stroke="#85B7EB" stroke-width="0.5"/>
<rect x="177" y="98" width="8" height="412" rx="2" fill="#DAEAF8" stroke="#85B7EB" stroke-width="0.5"/>
<rect x="430" y="260" width="8" height="230" rx="2" fill="#D4F0E5" stroke="#5DCAA5" stroke-width="0.5"/>
<!-- Start dot removed -->
<!-- msg 1: virtiofs_read -->
<line x1="59" y1="98" x2="177" y2="98" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<text x="116" y="92" text-anchor="middle" font-family="Courier" font-size="9" fill="#185FA5">virtiofs_read(...)</text>
<!-- msg 2: forge_request self-call -->
<line x1="185" y1="128" x2="214" y2="128" stroke="#378ADD" stroke-width="0.8" marker-end="url(#a)"/>
<line x1="214" y1="128" x2="214" y2="156" stroke="#378ADD" stroke-width="0.8"/>
<line x1="214" y1="156" x2="185" y2="156" stroke="#378ADD" stroke-width="0.8"/>
<text x="220" y="145" font-family="Courier" font-size="9" fill="#185FA5">forge_request()</text>
<!-- msg 3: queue_request self-call -->
<line x1="185" y1="180" x2="214" y2="180" stroke="#378ADD" stroke-width="0.8" marker-end="url(#a)"/>
<line x1="214" y1="180" x2="214" y2="208" stroke="#378ADD" stroke-width="0.8"/>
<line x1="214" y1="208" x2="185" y2="208" stroke="#378ADD" stroke-width="0.8"/>
<text x="220" y="197" font-family="Courier" font-size="9" fill="#185FA5">queue_request()</text>
<!-- phase band -->
<rect x="118" y="222" width="492" height="20" rx="3" fill="#DAEAF8" stroke="#85B7EB" stroke-width="0.5"/>
<text x="364" y="236" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">VM exit — notification crossing</text>
<!-- msg 4: signal_queue -> KVM -->
<line x1="185" y1="258" x2="305" y2="258" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<text x="244" y="252" text-anchor="middle" font-family="Courier" font-size="9" fill="#185FA5">signal_queue()</text>
<rect x="306" y="258" width="8" height="14" rx="2" fill="#D4F0E5" stroke="#5DCAA5" stroke-width="0.5"/>
<!-- msg 5: notify -> VirtioFSD -->
<line x1="314" y1="260" x2="430" y2="260" stroke="#0F6E56" stroke-width="1" marker-end="url(#t)"/>
<text x="370" y="254" text-anchor="middle" font-family="Courier" font-size="9" fill="#0F6E56">notify()</text>
<!-- msg 6: await_reply self-call -->
<line x1="185" y1="286" x2="214" y2="286" stroke="#378ADD" stroke-width="0.8" marker-end="url(#a)"/>
<line x1="214" y1="286" x2="214" y2="314" stroke="#378ADD" stroke-width="0.8"/>
<line x1="214" y1="314" x2="185" y2="314" stroke="#378ADD" stroke-width="0.8"/>
<text x="220" y="303" font-family="Courier" font-size="9" fill="#185FA5">await_reply()</text>
<!-- msg 7: read -> Host VFS -->
<line x1="438" y1="344" x2="566" y2="344" stroke="#0F6E56" stroke-width="1" marker-end="url(#t)"/>
<text x="500" y="338" text-anchor="middle" font-family="Courier" font-size="9" fill="#0F6E56">read(...)</text>
<rect x="564" y="344" width="8" height="46" rx="2" fill="#D4F0E5" stroke="#5DCAA5" stroke-width="0.5"/>
<!-- msg 8: read data <- Host VFS (dashed) -->
<line x1="564" y1="390" x2="438" y2="390" stroke="#5DCAA5" stroke-width="1" stroke-dasharray="5 3" marker-end="url(#t)"/>
<text x="500" y="384" text-anchor="middle" font-family="Courier" font-size="9" fill="#0F6E56">read data</text>
<!-- msg 9: forge_response self -->
<line x1="438" y1="416" x2="466" y2="416" stroke="#1D9E75" stroke-width="0.8" marker-end="url(#t)"/>
<line x1="466" y1="416" x2="466" y2="444" stroke="#1D9E75" stroke-width="0.8"/>
<line x1="466" y1="444" x2="438" y2="444" stroke="#1D9E75" stroke-width="0.8"/>
<text x="472" y="433" font-family="Courier" font-size="9" fill="#0F6E56">forge_response()</text>
<!-- msg 10: queue_response self -->
<line x1="438" y1="462" x2="466" y2="462" stroke="#1D9E75" stroke-width="0.8" marker-end="url(#t)"/>
<line x1="466" y1="462" x2="466" y2="490" stroke="#1D9E75" stroke-width="0.8"/>
<line x1="466" y1="490" x2="438" y2="490" stroke="#1D9E75" stroke-width="0.8"/>
<text x="472" y="479" font-family="Courier" font-size="9" fill="#0F6E56">queue_response()</text>
<!-- msg 11: read data <- driver (dashed) -->
<line x1="177" y1="510" x2="59" y2="510" stroke="#85B7EB" stroke-width="1" stroke-dasharray="5 3" marker-end="url(#d)"/>
<text x="116" y="504" text-anchor="middle" font-family="Courier" font-size="9" fill="#185FA5">read data</text>
<!-- start/return chips -->
<rect x="10" y="70" width="40" height="14" rx="3" fill="#EEF4FB" stroke="#85B7EB" stroke-width="0.5"/>
<text x="30" y="81" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#185FA5">start</text>
<rect x="10" y="522" width="40" height="14" rx="3" fill="#EEF4FB" stroke="#85B7EB" stroke-width="0.5"/>
<text x="30" y="533" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#185FA5">return</text>
</svg>"""

# ── 6b. Virtio PCI Sequence Diagram (design — combined interaction) ──────────
svgs["virtio_pci_sequence"] = """<svg width="680" height="544" viewBox="0 0 680 544" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#185FA5" stroke-width="1.5" stroke-linecap="round"/></marker>
<marker id="d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#85B7EB" stroke-width="1.5" stroke-linecap="round"/></marker>
</defs>
<rect width="680" height="544" fill="white"/>

<!-- Actor boxes -->
<rect x="10"  y="10" width="120" height="44" rx="6" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="70"  y="36" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">VirtioFS</text>

<rect x="228" y="10" width="144" height="44" rx="6" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="300" y="29" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">Virtio_control</text>
<text x="300" y="47" text-anchor="middle" font-family="Helvetica" font-size="9"  fill="#E6F1FB">PCI control plane</text>

<rect x="504" y="10" width="150" height="44" rx="6" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="579" y="29" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">Split_queue</text>
<text x="579" y="47" text-anchor="middle" font-family="Helvetica" font-size="9"  fill="#E6F1FB">data plane</text>

<!-- Lifelines -->
<line x1="70"  y1="54" x2="70"  y2="534" stroke="#85B7EB" stroke-width="0.5" stroke-dasharray="4 4"/>
<line x1="300" y1="54" x2="300" y2="534" stroke="#85B7EB" stroke-width="0.5" stroke-dasharray="4 4"/>
<line x1="579" y1="54" x2="579" y2="534" stroke="#85B7EB" stroke-width="0.5" stroke-dasharray="4 4"/>

<!-- Activation bars -->
<rect x="66"  y="78"  width="8" height="444" rx="2" fill="#DAEAF8" stroke="#85B7EB" stroke-width="0.5"/>
<rect x="296" y="96"  width="8" height="140" rx="2" fill="#DAEAF8" stroke="#85B7EB" stroke-width="0.5"/>
<rect x="575" y="196" width="8" height="72"  rx="2" fill="#DAEAF8" stroke="#85B7EB" stroke-width="0.5"/>
<rect x="575" y="352" width="8" height="148" rx="2" fill="#DAEAF8" stroke="#85B7EB" stroke-width="0.5"/>

<!-- ── Phase band 1: Initialization ── -->
<rect x="10" y="84" width="660" height="18" rx="3" fill="#DAEAF8" stroke="#85B7EB" stroke-width="0.5"/>
<text x="340" y="97" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">Initialization — construction order</text>

<!-- msg 1: Virtio_control constructor -->
<line x1="74"  y1="110" x2="296" y2="110" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<text x="183" y="104" text-anchor="middle" font-family="Courier" font-size="9" fill="#185FA5">Virtio_control(pci, req_features)</text>

<!-- msg 2: negotiate_features self-call (right-facing) -->
<line x1="304" y1="130" x2="330" y2="130" stroke="#378ADD" stroke-width="0.8" marker-end="url(#a)"/>
<line x1="330" y1="130" x2="330" y2="150" stroke="#378ADD" stroke-width="0.8"/>
<line x1="330" y1="150" x2="304" y2="150" stroke="#378ADD" stroke-width="0.8"/>
<text x="336" y="143" font-family="Courier" font-size="9" fill="#185FA5">negotiate_features()</text>

<!-- msg 3: pci ready return (dashed) -->
<line x1="296" y1="172" x2="74" y2="172" stroke="#85B7EB" stroke-width="1" stroke-dasharray="5 3" marker-end="url(#d)"/>
<text x="183" y="167" text-anchor="middle" font-family="Courier" font-size="9" fill="#185FA5">pci ready</text>

<!-- msg 4: Split_queue constructors (x2) -->
<line x1="74"  y1="196" x2="575" y2="196" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<text x="322" y="190" text-anchor="middle" font-family="Courier" font-size="9" fill="#185FA5">Split_queue(ctrl, idx)  ×2</text>

<!-- msg 5: alloc_rings self-call on Split_queue (right-facing) -->
<line x1="583" y1="216" x2="625" y2="216" stroke="#378ADD" stroke-width="0.8" marker-end="url(#a)"/>
<line x1="625" y1="216" x2="625" y2="236" stroke="#378ADD" stroke-width="0.8"/>
<line x1="625" y1="236" x2="583" y2="236" stroke="#378ADD" stroke-width="0.8"/>
<text x="604" y="212" text-anchor="middle" font-family="Courier" font-size="9" fill="#185FA5">alloc_rings()</text>

<!-- msg 6: enable_queue self-call on Split_queue (right-facing) -->
<line x1="583" y1="248" x2="625" y2="248" stroke="#378ADD" stroke-width="0.8" marker-end="url(#a)"/>
<line x1="625" y1="248" x2="625" y2="264" stroke="#378ADD" stroke-width="0.8"/>
<line x1="625" y1="264" x2="583" y2="264" stroke="#378ADD" stroke-width="0.8"/>
<text x="604" y="244" text-anchor="middle" font-family="Courier" font-size="9" fill="#185FA5">enable_queue()</text>

<!-- msg 7: queues ready return (dashed) -->
<line x1="575" y1="284" x2="74" y2="284" stroke="#85B7EB" stroke-width="1" stroke-dasharray="5 3" marker-end="url(#d)"/>
<text x="322" y="279" text-anchor="middle" font-family="Courier" font-size="9" fill="#185FA5">queues ready  ×2</text>

<!-- msg 8: set_driver_ok_bit -->
<rect x="296" y="298" width="8" height="16" rx="2" fill="#DAEAF8" stroke="#85B7EB" stroke-width="0.5"/>
<line x1="74"  y1="306" x2="296" y2="306" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<text x="183" y="300" text-anchor="middle" font-family="Courier" font-size="9" fill="#185FA5">set_driver_ok_bit()</text>

<!-- ── Phase band 2: I/O path ── -->
<rect x="10" y="326" width="660" height="18" rx="3" fill="#DAEAF8" stroke="#85B7EB" stroke-width="0.5"/>
<text x="340" y="339" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">I/O path — enqueue → poll → dequeue</text>

<!-- msg 9: enqueue(tokens) -->
<line x1="74"  y1="360" x2="575" y2="360" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<text x="322" y="354" text-anchor="middle" font-family="Courier" font-size="9" fill="#185FA5">enqueue(tokens)</text>

<!-- msg 10: build_chain self-call (right-facing) -->
<line x1="583" y1="380" x2="625" y2="380" stroke="#378ADD" stroke-width="0.8" marker-end="url(#a)"/>
<line x1="625" y1="380" x2="625" y2="398" stroke="#378ADD" stroke-width="0.8"/>
<line x1="625" y1="398" x2="583" y2="398" stroke="#378ADD" stroke-width="0.8"/>
<text x="604" y="376" text-anchor="middle" font-family="Courier" font-size="9" fill="#185FA5">build_chain()</text>

<!-- msg 11: _notify_device self-call (right-facing) -->
<line x1="583" y1="414" x2="625" y2="414" stroke="#378ADD" stroke-width="0.8" marker-end="url(#a)"/>
<line x1="625" y1="414" x2="625" y2="432" stroke="#378ADD" stroke-width="0.8"/>
<line x1="625" y1="432" x2="583" y2="432" stroke="#378ADD" stroke-width="0.8"/>
<text x="604" y="410" text-anchor="middle" font-family="Courier" font-size="9" fill="#185FA5">_notify_device()</text>

<!-- msg 12: enqueue return (dashed) -->
<line x1="575" y1="448" x2="74" y2="448" stroke="#85B7EB" stroke-width="1" stroke-dasharray="5 3" marker-end="url(#d)"/>

<!-- msg 13: has_processed_used spin (self-call on VirtioFS, right-facing) -->
<line x1="74"  y1="462" x2="102" y2="462" stroke="#378ADD" stroke-width="0.8" marker-end="url(#a)"/>
<line x1="102" y1="462" x2="102" y2="480" stroke="#378ADD" stroke-width="0.8"/>
<line x1="102" y1="480" x2="74"  y2="480" stroke="#378ADD" stroke-width="0.8"/>
<text x="108" y="474" font-family="Courier" font-size="9" fill="#185FA5">has_processed_used() [spin]</text>

<!-- msg 14: dequeue(&len) -->
<line x1="74"  y1="498" x2="575" y2="498" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<text x="322" y="492" text-anchor="middle" font-family="Courier" font-size="9" fill="#185FA5">dequeue(&amp;len)</text>

<!-- msg 15: VirtTokens return (dashed) -->
<line x1="575" y1="514" x2="74" y2="514" stroke="#85B7EB" stroke-width="1" stroke-dasharray="5 3" marker-end="url(#d)"/>
<text x="322" y="509" text-anchor="middle" font-family="Courier" font-size="9" fill="#185FA5">VirtTokens</text>

<!-- start / return chips -->
<rect x="10" y="70"  width="40" height="14" rx="3" fill="#EEF4FB" stroke="#85B7EB" stroke-width="0.5"/>
<text x="30"  y="81" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#185FA5">start</text>
<rect x="10" y="526" width="40" height="14" rx="3" fill="#EEF4FB" stroke="#85B7EB" stroke-width="0.5"/>
<text x="30"  y="537" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#185FA5">return</text>
</svg>"""

# ── 7. Virtio Component Diagram (design) ─────────────────────────────────────
svgs["virtio_component"] = """<svg width="680" height="220" viewBox="0 0 680 220" xmlns="http://www.w3.org/2000/svg">
<rect width="680" height="220" fill="white"/>
<!-- PMIO PCI -->
<rect x="20" y="90" width="16" height="10" rx="2" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<rect x="20" y="108" width="16" height="10" rx="2" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<rect x="32" y="80" width="110" height="48" rx="7" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="87" y="108" text-anchor="middle" font-family="Helvetica" font-size="12" font-weight="bold" fill="white">PMIO PCI</text>
<!-- connector 1: PMIO -> Control Plane: lollipop on PMIO right, socket on CP left -->
<line x1="142" y1="104" x2="158" y2="104" stroke="#185FA5" stroke-width="1"/>
<circle cx="166" cy="104" r="7" fill="#378ADD" stroke="#185FA5" stroke-width="1"/>
<line x1="173" y1="104" x2="192" y2="104" stroke="#185FA5" stroke-width="1"/>
<path d="M192,95 A9,9 0 0,1 192,113" fill="none" stroke="#185FA5" stroke-width="1.2"/>
<line x1="192" y1="104" x2="202" y2="104" stroke="#185FA5" stroke-width="1"/>
<!-- CONTROL PLANE -->
<rect x="200" y="90" width="16" height="10" rx="2" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<rect x="200" y="108" width="16" height="10" rx="2" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<rect x="212" y="80" width="140" height="48" rx="7" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="282" y="101" text-anchor="middle" font-family="Helvetica" font-size="12" font-weight="bold" fill="white">Control</text>
<text x="282" y="118" text-anchor="middle" font-family="Helvetica" font-size="12" font-weight="bold" fill="white">Plane</text>
<!-- connector 2: CP -> Device Driver -->
<line x1="352" y1="104" x2="368" y2="104" stroke="#185FA5" stroke-width="1"/>
<circle cx="376" cy="104" r="7" fill="#378ADD" stroke="#185FA5" stroke-width="1"/>
<line x1="383" y1="104" x2="402" y2="104" stroke="#185FA5" stroke-width="1"/>
<path d="M402,95 A9,9 0 0,1 402,113" fill="none" stroke="#185FA5" stroke-width="1.2"/>
<line x1="402" y1="104" x2="412" y2="104" stroke="#185FA5" stroke-width="1"/>
<!-- connector 3: CP bottom -> Split Queue top (lollipop on CP, socket on SQ) -->
<line x1="282" y1="128" x2="282" y2="143" stroke="#185FA5" stroke-width="1"/>
<circle cx="282" cy="151" r="7" fill="#378ADD" stroke="#185FA5" stroke-width="1"/>
<line x1="282" y1="158" x2="282" y2="172" stroke="#185FA5" stroke-width="1"/>
<path d="M273,172 A9,9 0 0,0 291,172" fill="none" stroke="#185FA5" stroke-width="1.2"/>
<line x1="282" y1="172" x2="282" y2="182" stroke="#185FA5" stroke-width="1"/>
<!-- SPLIT QUEUE -->
<rect x="212" y="180" width="140" height="48" rx="7" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="282" y="201" text-anchor="middle" font-family="Helvetica" font-size="12" font-weight="bold" fill="white">Split</text>
<text x="282" y="218" text-anchor="middle" font-family="Helvetica" font-size="12" font-weight="bold" fill="white">Queue</text>
<!-- connector 4: Split Queue right -> Device Driver bottom (lollipop on SQ, socket on DD) -->
<line x1="352" y1="204" x2="500" y2="204" stroke="#185FA5" stroke-width="1"/>
<circle cx="508" cy="204" r="7" fill="#378ADD" stroke="#185FA5" stroke-width="1"/>
<line x1="515" y1="204" x2="530" y2="204" stroke="#185FA5" stroke-width="1"/>
<line x1="530" y1="204" x2="530" y2="136" stroke="#185FA5" stroke-width="1"/>
<path d="M521,136 A9,9 0 0,0 539,136" fill="none" stroke="#185FA5" stroke-width="1.2"/>
<line x1="530" y1="136" x2="530" y2="128" stroke="#185FA5" stroke-width="1"/>
<!-- DEVICE DRIVER -->
<rect x="410" y="90" width="16" height="10" rx="2" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<rect x="410" y="108" width="16" height="10" rx="2" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.5"/>
<rect x="422" y="80" width="138" height="48" rx="7" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="491" y="101" text-anchor="middle" font-family="Helvetica" font-size="12" font-weight="bold" fill="white">Device</text>
<text x="491" y="118" text-anchor="middle" font-family="Helvetica" font-size="12" font-weight="bold" fill="white">Driver</text>
</svg>"""

# ── 8. VirtioFS Initialization Flowchart ─────────────────────────────────────
svgs["virtiofs_init"] = """<svg width="680" height="820" viewBox="0 0 680 820" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#185FA5" stroke-width="1.5" stroke-linecap="round"/></marker>
<marker id="r" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#E24B4A" stroke-width="1.5" stroke-linecap="round"/></marker>
</defs>
<rect width="680" height="820" fill="white"/>
<!-- LEFT COLUMN -->
<!-- START -->
<circle cx="140" cy="44" r="38" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="140" y="33" text-anchor="middle" font-family="Helvetica" font-size="10" font-weight="bold" fill="white">VirtioFS</text>
<text x="140" y="48" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E6F1FB">constructor</text>
<text x="140" y="62" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E6F1FB">START</text>
<line x1="140" y1="82" x2="140" y2="104" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<!-- Box 1 -->
<rect x="66" y="104" width="148" height="42" rx="7" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="140" y="121" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">Init virtio control</text>
<text x="140" y="137" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E6F1FB">constructor</text>
<line x1="140" y1="146" x2="140" y2="168" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<!-- Box 2 -->
<rect x="66" y="168" width="148" height="42" rx="7" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="140" y="185" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">Build request queue</text>
<text x="140" y="201" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E6F1FB">split queue constructor</text>
<line x1="140" y1="210" x2="140" y2="232" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<!-- Box 3 -->
<rect x="66" y="232" width="148" height="42" rx="7" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="140" y="249" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">Build hi-priority queue</text>
<text x="140" y="265" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E6F1FB">split queue constructor</text>
<line x1="140" y1="274" x2="140" y2="296" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<!-- Box 4: Assert driver_ok -->
<rect x="66" y="296" width="148" height="42" rx="7" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="140" y="313" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">Assert driver_ok</text>
<text x="140" y="329" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E6F1FB">signal device ready</text>
<!-- L-shaped connector to Send FUSE_init -->
<polyline points="214,317 298,317 298,638" fill="none" stroke="#185FA5" stroke-width="1" stroke-dasharray="5 3"/>
<line x1="298" y1="638" x2="358" y2="638" stroke="#185FA5" stroke-width="1" stroke-dasharray="5 3" marker-end="url(#a)"/>
<text x="306" y="310" font-family="Helvetica" font-size="9" fill="#185FA5">init handshake</text>
<!-- Separator -->
<line x1="318" y1="20" x2="318" y2="800" stroke="#ccc" stroke-width="0.5" stroke-dasharray="5 4"/>
<!-- RIGHT COLUMN (bottom-up flow) -->
<!-- DONE -->
<circle cx="490" cy="44" r="38" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="490" y="33" text-anchor="middle" font-family="Helvetica" font-size="10" font-weight="bold" fill="white">VirtioFS</text>
<text x="490" y="48" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E6F1FB">constructor</text>
<text x="490" y="62" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E6F1FB">DONE</text>
<!-- Mount -> DONE (arrow UP) -->
<line x1="490" y1="160" x2="490" y2="82" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<!-- Mount filesystem -->
<rect x="366" y="160" width="248" height="52" rx="7" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="490" y="180" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">Mount filesystem</text>
<text x="490" y="196" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E6F1FB">register fs at VFS manager</text>
<text x="490" y="208" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E6F1FB">with VirtioFS device id</text>
<!-- Record max_write -> Mount (UP) -->
<line x1="490" y1="280" x2="490" y2="212" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<!-- Record max_write -->
<rect x="366" y="280" width="248" height="42" rx="7" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="490" y="297" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">Record max_write</text>
<text x="490" y="313" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E6F1FB">store max write payload size</text>
<!-- minor YES -> Record (UP) -->
<line x1="490" y1="376" x2="490" y2="322" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<text x="472" y="353" text-anchor="end" font-family="Helvetica" font-size="9" fill="#185FA5">YES</text>
<!-- Diamond: minor version -->
<polygon points="490,376 548,422 490,468 432,422" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.8"/>
<text x="490" y="416" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">minor version</text>
<text x="490" y="430" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">matches?</text>
<!-- NO -> panic 1 -->
<line x1="548" y1="422" x2="606" y2="422" stroke="#E24B4A" stroke-width="1" marker-end="url(#r)"/>
<text x="574" y="414" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E24B4A">NO</text>
<rect x="606" y="398" width="58" height="46" rx="6" fill="#E24B4A" stroke="#A32D2D" stroke-width="0.5"/>
<text x="635" y="417" text-anchor="middle" font-family="Helvetica" font-size="10" font-weight="bold" fill="white">Panic</text>
<text x="635" y="433" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#FCEBEB">assert</text>
<!-- major YES -> minor diamond (UP) -->
<line x1="490" y1="502" x2="490" y2="468" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<text x="472" y="488" text-anchor="end" font-family="Helvetica" font-size="9" fill="#185FA5">YES</text>
<!-- Diamond: major version -->
<polygon points="490,502 548,548 490,594 432,548" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.8"/>
<text x="490" y="542" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">major version</text>
<text x="490" y="556" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">compatible?</text>
<!-- NO -> panic 2 -->
<line x1="548" y1="548" x2="606" y2="548" stroke="#E24B4A" stroke-width="1" marker-end="url(#r)"/>
<text x="574" y="540" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E24B4A">NO</text>
<rect x="606" y="524" width="58" height="46" rx="6" fill="#E24B4A" stroke="#A32D2D" stroke-width="0.5"/>
<text x="635" y="543" text-anchor="middle" font-family="Helvetica" font-size="10" font-weight="bold" fill="white">Panic</text>
<text x="635" y="559" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#FCEBEB">assert</text>
<!-- Send FUSE_init -> major (UP) -->
<line x1="490" y1="618" x2="490" y2="594" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<text x="472" y="608" text-anchor="end" font-family="Helvetica" font-size="9" fill="#185FA5">YES</text>
<!-- Send FUSE_init -->
<rect x="358" y="618" width="264" height="52" rx="7" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="490" y="638" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">Send FUSE_init</text>
<text x="490" y="654" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E6F1FB">driver major &amp; minor version handshake</text>
</svg>"""

# ── 8b. VirtioFS open() Flowchart ────────────────────────────────────────────
svgs["virtiofs_open"] = """<svg width="680" height="620" viewBox="0 0 680 620" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#185FA5" stroke-width="1.5" stroke-linecap="round"/></marker>
<marker id="r" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#E24B4A" stroke-width="1.5" stroke-linecap="round"/></marker>
<marker id="g" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#0F6E56" stroke-width="1.5" stroke-linecap="round"/></marker>
</defs>
<rect width="680" height="620" fill="white"/>
<!-- START -->
<circle cx="200" cy="44" r="32" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="200" y="36" text-anchor="middle" font-family="Helvetica" font-size="10" font-weight="bold" fill="white">VirtioFS</text>
<text x="200" y="50" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E6F1FB">open()</text>
<text x="200" y="64" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E6F1FB">START</text>
<line x1="200" y1="76" x2="200" y2="104" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<!-- Entry box -->
<rect x="126" y="104" width="148" height="42" rx="7" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="200" y="121" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">fs.open(fd, path, ...)</text>
<text x="200" y="137" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E6F1FB">driver entry from VFS</text>
<line x1="200" y1="146" x2="200" y2="172" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<!-- Decision diamond: O_CREAT? -->
<polygon points="200,172 260,212 200,252 140,212" fill="#EEF4FB" stroke="#185FA5" stroke-width="0.8"/>
<text x="200" y="208" text-anchor="middle" font-family="Helvetica" font-size="10" fill="#185FA5">O_CREAT</text>
<text x="200" y="222" text-anchor="middle" font-family="Helvetica" font-size="10" fill="#185FA5">set?</text>
<!-- NO (down) -->
<line x1="200" y1="252" x2="200" y2="282" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<text x="188" y="270" text-anchor="end" font-family="Helvetica" font-size="9" fill="#185FA5">NO</text>
<!-- YES arrow right to CREATE column -->
<line x1="260" y1="212" x2="490" y2="212" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<text x="375" y="206" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">YES &#8212; _open_creat</text>
<!-- CREATE box -->
<rect x="490" y="191" width="180" height="42" rx="7" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="580" y="208" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">Send FUSE_CREATE</text>
<text x="580" y="224" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E6F1FB">lookup + open in 1 RTT</text>
<!-- FUSE_LOOKUP (NO branch main column) -->
<rect x="126" y="282" width="148" height="42" rx="7" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="200" y="299" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">Send FUSE_LOOKUP</text>
<text x="200" y="315" text-anchor="middle" font-family="Courier" font-size="9" fill="#E6F1FB">path &#8594; inode</text>
<!-- LOOKUP error offshoot -->
<line x1="274" y1="303" x2="320" y2="303" stroke="#E24B4A" stroke-width="1" marker-end="url(#r)"/>
<rect x="320" y="282" width="130" height="42" rx="7" fill="#E24B4A" stroke="#A32D2D" stroke-width="0.5"/>
<text x="385" y="299" text-anchor="middle" font-family="Helvetica" font-size="10" font-weight="bold" fill="white">return -ENOENT</text>
<text x="385" y="315" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#FCEBEB">not found</text>
<line x1="200" y1="324" x2="200" y2="346" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<!-- FUSE_OPEN -->
<rect x="126" y="346" width="148" height="42" rx="7" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="200" y="363" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">Send FUSE_OPEN</text>
<text x="200" y="379" text-anchor="middle" font-family="Courier" font-size="9" fill="#E6F1FB">inode &#8594; file handle</text>
<!-- OPEN error offshoot -->
<line x1="274" y1="367" x2="320" y2="367" stroke="#E24B4A" stroke-width="1" marker-end="url(#r)"/>
<rect x="320" y="346" width="130" height="42" rx="7" fill="#E24B4A" stroke="#A32D2D" stroke-width="0.5"/>
<text x="385" y="363" text-anchor="middle" font-family="Helvetica" font-size="10" font-weight="bold" fill="white">return err</text>
<text x="385" y="379" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#FCEBEB">fuse_out_header.error</text>
<line x1="200" y1="388" x2="200" y2="414" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<!-- Store in _fd_info_map (merge point) -->
<rect x="126" y="414" width="148" height="42" rx="7" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="200" y="431" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">Store in _fd_info_map</text>
<text x="200" y="447" text-anchor="middle" font-family="Courier" font-size="9" fill="#E6F1FB">inode, fh, offset=0</text>
<!-- CREATE success path: down from CREATE, left to Store -->
<polyline points="580,233 580,435 274,435" fill="none" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<text x="590" y="330" font-family="Helvetica" font-size="9" fill="#185FA5">OK</text>
<!-- Arrow down to DONE -->
<line x1="200" y1="456" x2="200" y2="482" stroke="#0F6E56" stroke-width="1" marker-end="url(#g)"/>
<!-- DONE (green) -->
<circle cx="200" cy="516" r="32" fill="#1D9E75" stroke="#0F6E56" stroke-width="0.5"/>
<text x="200" y="510" text-anchor="middle" font-family="Helvetica" font-size="10" font-weight="bold" fill="white">return fd</text>
<text x="200" y="525" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E6F8EF">success</text>
</svg>"""

# ── 9. Read descriptor chain (implementation) ────────────────────────────────
svgs["read_chain"] = """<svg width="680" height="160" viewBox="0 0 680 160" xmlns="http://www.w3.org/2000/svg">
<rect width="680" height="160" fill="white"/>
<text x="340" y="20" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="#185FA5">FUSE Read — Descriptor Chain</text>
<!-- Readable section label -->
<text x="150" y="40" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">← Readable (driver→daemon) →</text>
<!-- Writable section label -->
<text x="490" y="40" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#0F6E56">← Writable (daemon→driver) →</text>
<!-- Divider between sections -->
<line x1="300" y1="46" x2="300" y2="130" stroke="#aaa" stroke-width="0.8" stroke-dasharray="4 3"/>
<!-- Descriptor 0: read req header -->
<rect x="20" y="50" width="260" height="70" rx="6" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.8"/>
<text x="150" y="78" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#185FA5">virtio_fs_read_req</text>
<text x="150" y="95" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">fuse_in_header + fuse_read_in</text>
<text x="150" y="111" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: READ (device read-only)</text>
<!-- Descriptor 1: out header -->
<rect x="310" y="50" width="170" height="70" rx="6" fill="#D4F0E5" stroke="#0F6E56" stroke-width="0.8"/>
<text x="395" y="78" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#0F6E56">fuse_out_header</text>
<text x="395" y="95" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#0F6E56">error + unique + len</text>
<text x="395" y="111" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: WRITE (device write-only)</text>
<!-- Descriptor 2: caller buffer -->
<rect x="490" y="50" width="170" height="70" rx="6" fill="#D4F0E5" stroke="#0F6E56" stroke-width="0.8"/>
<text x="575" y="78" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#0F6E56">caller buffer</text>
<text x="575" y="95" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#0F6E56">read data payload</text>
<text x="575" y="111" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: WRITE (device write-only)</text>
<!-- chain arrows -->
<text x="292" y="89" text-anchor="middle" font-family="Helvetica" font-size="14" fill="#185FA5">→</text>
<text x="474" y="89" text-anchor="middle" font-family="Helvetica" font-size="14" fill="#0F6E56">→</text>
<text x="340" y="148" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#5F5E5A">bytes_read = fuse_out_header.len − sizeof(fuse_out_header)</text>
</svg>"""

# ── 10. Write descriptor chain (implementation) ──────────────────────────────
svgs["write_chain"] = """<svg width="680" height="160" viewBox="0 0 680 160" xmlns="http://www.w3.org/2000/svg">
<rect width="680" height="160" fill="white"/>
<text x="340" y="20" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="#185FA5">FUSE Write — Descriptor Chain</text>
<text x="220" y="40" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">← Readable (driver→daemon) →</text>
<text x="570" y="40" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#0F6E56">← Writable →</text>
<line x1="430" y1="46" x2="430" y2="130" stroke="#aaa" stroke-width="0.8" stroke-dasharray="4 3"/>
<!-- Descriptor 0: write req header -->
<rect x="20" y="50" width="200" height="70" rx="6" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.8"/>
<text x="120" y="78" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#185FA5">virtio_fs_write_req</text>
<text x="120" y="95" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">fuse_in_header + fuse_write_in</text>
<text x="120" y="111" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: READ</text>
<!-- Descriptor 1: caller buffer (readable) -->
<rect x="230" y="50" width="190" height="70" rx="6" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.8"/>
<text x="325" y="78" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#185FA5">caller buffer</text>
<text x="325" y="95" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">write data payload (≤ max_write)</text>
<text x="325" y="111" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: READ</text>
<!-- Descriptor 2: write out (writable) -->
<rect x="440" y="50" width="220" height="70" rx="6" fill="#D4F0E5" stroke="#0F6E56" stroke-width="0.8"/>
<text x="550" y="78" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#0F6E56">fuse_write_out</text>
<text x="550" y="95" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#0F6E56">bytes accepted by daemon</text>
<text x="550" y="111" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: WRITE</text>
<!-- chain arrows -->
<text x="222" y="89" text-anchor="middle" font-family="Helvetica" font-size="14" fill="#185FA5">→</text>
<text x="432" y="89" text-anchor="middle" font-family="Helvetica" font-size="14" fill="#0F6E56">→</text>
<text x="340" y="148" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#5F5E5A">Write payload is capped at _max_write negotiated during FUSE_INIT</text>
</svg>"""

# ── 10b. Readv descriptor chain (implementation) ─────────────────────────────
svgs["readv_chain"] = """<svg width="680" height="160" viewBox="0 0 680 160" xmlns="http://www.w3.org/2000/svg">
<rect width="680" height="160" fill="white"/>
<text x="340" y="20" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="#185FA5">FUSE Readv — Vectorized Descriptor Chain</text>
<text x="90" y="40" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">← Readable (driver→daemon) →</text>
<text x="430" y="40" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#0F6E56">← Writable (daemon→driver) →</text>
<line x1="173" y1="46" x2="173" y2="130" stroke="#aaa" stroke-width="0.8" stroke-dasharray="4 3"/>
<!-- Desc 0: read request (R) -->
<rect x="10" y="50" width="155" height="70" rx="6" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.8"/>
<text x="87" y="78" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#185FA5">virtio_fs_read_req</text>
<text x="87" y="95" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">fuse_in_header + fuse_read_in</text>
<text x="87" y="111" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: READ</text>
<!-- Desc 1: fuse_out_header (W) -->
<rect x="181" y="50" width="116" height="70" rx="6" fill="#D4F0E5" stroke="#0F6E56" stroke-width="0.8"/>
<text x="239" y="78" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#0F6E56">fuse_out_header</text>
<text x="239" y="95" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#0F6E56">error + len</text>
<text x="239" y="111" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: WRITE</text>
<!-- Desc 2: iovec[0] caller buffer (W) -->
<rect x="305" y="50" width="108" height="70" rx="6" fill="#D4F0E5" stroke="#0F6E56" stroke-width="0.8"/>
<text x="359" y="78" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#0F6E56">iovec[0]</text>
<text x="359" y="95" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#0F6E56">caller buffer</text>
<text x="359" y="111" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: WRITE</text>
<!-- ··· -->
<text x="425" y="91" text-anchor="middle" font-family="Helvetica" font-size="13" fill="#0F6E56">···</text>
<!-- Desc n: iovec[n-1] caller buffer (W) -->
<rect x="442" y="50" width="138" height="70" rx="6" fill="#D4F0E5" stroke="#0F6E56" stroke-width="0.8"/>
<text x="511" y="78" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#0F6E56">iovec[n-1]</text>
<text x="511" y="95" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#0F6E56">caller buffer</text>
<text x="511" y="111" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: WRITE</text>
<!-- arrows -->
<text x="171" y="89" text-anchor="middle" font-family="Helvetica" font-size="14" fill="#185FA5">→</text>
<text x="296" y="89" text-anchor="middle" font-family="Helvetica" font-size="14" fill="#0F6E56">→</text>
<text x="437" y="89" text-anchor="middle" font-family="Helvetica" font-size="14" fill="#0F6E56">→</text>
<text x="340" y="148" text-anchor="middle" font-family="Helvetica" font-size="10" fill="#5F5E5A">Readv appends one writable descriptor per iovec element; N caller buffers are filled without any aggregation copy</text>
</svg>"""

# ── 10c. Writev descriptor chain (implementation) ────────────────────────────
svgs["writev_chain"] = """<svg width="680" height="160" viewBox="0 0 680 160" xmlns="http://www.w3.org/2000/svg">
<rect width="680" height="160" fill="white"/>
<text x="340" y="20" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="#185FA5">FUSE Writev — Vectorized Descriptor Chain</text>
<text x="220" y="40" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">← Readable (driver→daemon) →</text>
<text x="565" y="40" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#0F6E56">← Writable →</text>
<line x1="414" y1="46" x2="414" y2="130" stroke="#aaa" stroke-width="0.8" stroke-dasharray="4 3"/>
<!-- Desc 0: write request header (R) -->
<rect x="10" y="50" width="148" height="70" rx="6" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.8"/>
<text x="84" y="78" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#185FA5">virtio_fs_write_req</text>
<text x="84" y="95" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">fuse_in_header + fuse_write_in</text>
<text x="84" y="111" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: READ</text>
<!-- Desc 1: iovec[0] caller buffer (R) -->
<rect x="166" y="50" width="108" height="70" rx="6" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.8"/>
<text x="220" y="78" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#185FA5">iovec[0]</text>
<text x="220" y="95" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">caller buffer</text>
<text x="220" y="111" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: READ</text>
<!-- ··· -->
<text x="284" y="91" text-anchor="middle" font-family="Helvetica" font-size="13" fill="#185FA5">···</text>
<!-- Desc n-1: iovec[n-1] caller buffer (R) -->
<rect x="300" y="50" width="108" height="70" rx="6" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.8"/>
<text x="354" y="78" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#185FA5">iovec[n-1]</text>
<text x="354" y="95" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">caller buffer</text>
<text x="354" y="111" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: READ</text>
<!-- Desc n: fuse_write_out (W) -->
<rect x="422" y="50" width="148" height="70" rx="6" fill="#D4F0E5" stroke="#0F6E56" stroke-width="0.8"/>
<text x="496" y="78" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#0F6E56">fuse_write_out</text>
<text x="496" y="95" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#0F6E56">bytes accepted by daemon</text>
<text x="496" y="111" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: WRITE</text>
<!-- arrows -->
<text x="158" y="89" text-anchor="middle" font-family="Helvetica" font-size="14" fill="#185FA5">→</text>
<text x="295" y="89" text-anchor="middle" font-family="Helvetica" font-size="14" fill="#185FA5">→</text>
<text x="412" y="89" text-anchor="middle" font-family="Helvetica" font-size="14" fill="#0F6E56">→</text>
<text x="340" y="148" text-anchor="middle" font-family="Helvetica" font-size="10" fill="#5F5E5A">Writev prepends one readable descriptor per iovec element; each caller buffer is enqueued directly without copying</text>
</svg>"""

# ── 10d. FUSE_INIT descriptor chain ──────────────────────────────────────────
svgs["init_chain"] = """<svg width="680" height="160" viewBox="0 0 680 160" xmlns="http://www.w3.org/2000/svg">
<rect width="680" height="160" fill="white"/>
<text x="340" y="20" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="#185FA5">FUSE Init — Descriptor Chain</text>
<text x="162" y="40" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">← Readable (driver→daemon) →</text>
<text x="507" y="40" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#0F6E56">← Writable (daemon→driver) →</text>
<line x1="335" y1="46" x2="335" y2="130" stroke="#aaa" stroke-width="0.8" stroke-dasharray="4 3"/>
<!-- Descriptor 0: init request (R) -->
<rect x="10" y="50" width="305" height="70" rx="6" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.8"/>
<text x="162" y="75" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#185FA5">virtio_fs_init_req</text>
<text x="162" y="92" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">fuse_in_header + fuse_init_in</text>
<text x="162" y="109" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: READ</text>
<!-- Arrow -->
<text x="323" y="89" text-anchor="middle" font-family="Helvetica" font-size="14" fill="#185FA5">→</text>
<!-- Descriptor 1: init response (W) -->
<rect x="345" y="50" width="325" height="70" rx="6" fill="#D4F0E5" stroke="#0F6E56" stroke-width="0.8"/>
<text x="507" y="75" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#0F6E56">fuse_out_header + fuse_init_out</text>
<text x="507" y="92" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#0F6E56">major, minor, max_write, flags</text>
<text x="507" y="109" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: WRITE</text>
<text x="340" y="148" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#5F5E5A">max_write stored reduced by FUSE_BUFFER_HEADER_SIZE; daemon major version must match driver exactly</text>
</svg>"""

# ── 10e. FUSE_LOOKUP descriptor chain ────────────────────────────────────────
svgs["lookup_chain"] = """<svg width="680" height="160" viewBox="0 0 680 160" xmlns="http://www.w3.org/2000/svg">
<rect width="680" height="160" fill="white"/>
<text x="340" y="20" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="#185FA5">FUSE Lookup — Descriptor Chain</text>
<text x="208" y="40" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">← Readable (driver→daemon) →</text>
<text x="546" y="40" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#0F6E56">← Writable (daemon→driver) →</text>
<line x1="415" y1="46" x2="415" y2="130" stroke="#aaa" stroke-width="0.8" stroke-dasharray="4 3"/>
<!-- Descriptor 0: lookup request header (R) -->
<rect x="10" y="50" width="185" height="70" rx="6" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.8"/>
<text x="102" y="75" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#185FA5">virtio_fs_lookup_req</text>
<text x="102" y="92" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">fuse_in_header (nodeid=parent)</text>
<text x="102" y="109" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: READ</text>
<!-- Arrow 0→1 -->
<text x="203" y="89" text-anchor="middle" font-family="Helvetica" font-size="14" fill="#185FA5">→</text>
<!-- Descriptor 1: name string (R) -->
<rect x="211" y="50" width="195" height="70" rx="6" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.8"/>
<text x="308" y="75" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#185FA5">name / filename</text>
<text x="308" y="92" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">const char* (null-terminated)</text>
<text x="308" y="109" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: READ</text>
<!-- Arrow 1→2 -->
<text x="413" y="89" text-anchor="middle" font-family="Helvetica" font-size="14" fill="#185FA5">→</text>
<!-- Descriptor 2: entry response (W) -->
<rect x="423" y="50" width="247" height="70" rx="6" fill="#D4F0E5" stroke="#0F6E56" stroke-width="0.8"/>
<text x="546" y="75" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#0F6E56">fuse_out_header + fuse_entry_out</text>
<text x="546" y="92" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#0F6E56">nodeid, generation, attr</text>
<text x="546" y="109" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: WRITE</text>
<text x="340" y="148" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#5F5E5A">Returned nodeid and file handle are cached in _fd_info_map to avoid repeated lookups</text>
</svg>"""

# ── 10f. FUSE_OPEN descriptor chain ──────────────────────────────────────────
svgs["open_chain"] = """<svg width="680" height="160" viewBox="0 0 680 160" xmlns="http://www.w3.org/2000/svg">
<rect width="680" height="160" fill="white"/>
<text x="340" y="20" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="#185FA5">FUSE Open — Descriptor Chain</text>
<text x="162" y="40" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">← Readable (driver→daemon) →</text>
<text x="507" y="40" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#0F6E56">← Writable (daemon→driver) →</text>
<line x1="335" y1="46" x2="335" y2="130" stroke="#aaa" stroke-width="0.8" stroke-dasharray="4 3"/>
<!-- Descriptor 0: open request (R) -->
<rect x="10" y="50" width="305" height="70" rx="6" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.8"/>
<text x="162" y="75" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#185FA5">virtio_fs_open_req</text>
<text x="162" y="92" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">fuse_in_header + fuse_open_in (flags)</text>
<text x="162" y="109" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: READ</text>
<!-- Arrow -->
<text x="323" y="89" text-anchor="middle" font-family="Helvetica" font-size="14" fill="#185FA5">→</text>
<!-- Descriptor 1: open response (W) -->
<rect x="345" y="50" width="325" height="70" rx="6" fill="#D4F0E5" stroke="#0F6E56" stroke-width="0.8"/>
<text x="507" y="75" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#0F6E56">fuse_out_header + fuse_open_out</text>
<text x="507" y="92" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#0F6E56">fh (file handle), open_flags</text>
<text x="507" y="109" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: WRITE</text>
<text x="340" y="148" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#5F5E5A">Daemon returns a file handle (fh) stored in _fd_info_map and used in all subsequent read/write/release requests</text>
</svg>"""

# ── 10g. FUSE_CREATE descriptor chain ────────────────────────────────────────
svgs["create_chain"] = """<svg width="680" height="160" viewBox="0 0 680 160" xmlns="http://www.w3.org/2000/svg">
<rect width="680" height="160" fill="white"/>
<text x="340" y="20" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="#185FA5">FUSE Create — Descriptor Chain</text>
<text x="208" y="40" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">← Readable (driver→daemon) →</text>
<text x="546" y="40" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#0F6E56">← Writable (daemon→driver) →</text>
<line x1="415" y1="46" x2="415" y2="130" stroke="#aaa" stroke-width="0.8" stroke-dasharray="4 3"/>
<!-- Descriptor 0: create request header (R) -->
<rect x="10" y="50" width="185" height="70" rx="6" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.8"/>
<text x="102" y="75" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#185FA5">virtio_fs_create_req</text>
<text x="102" y="92" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">fuse_in_header + fuse_create_in</text>
<text x="102" y="109" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: READ</text>
<!-- Arrow 0→1 -->
<text x="203" y="89" text-anchor="middle" font-family="Helvetica" font-size="14" fill="#185FA5">→</text>
<!-- Descriptor 1: name string (R) -->
<rect x="211" y="50" width="195" height="70" rx="6" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.8"/>
<text x="308" y="75" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#185FA5">name / filename</text>
<text x="308" y="92" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">const char* (null-terminated)</text>
<text x="308" y="109" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: READ</text>
<!-- Arrow 1→2 -->
<text x="413" y="89" text-anchor="middle" font-family="Helvetica" font-size="14" fill="#185FA5">→</text>
<!-- Descriptor 2: combined create+open response (W) -->
<rect x="423" y="50" width="247" height="70" rx="6" fill="#D4F0E5" stroke="#0F6E56" stroke-width="0.8"/>
<text x="546" y="75" text-anchor="middle" font-family="Courier" font-size="9.5" font-weight="bold" fill="#0F6E56">fuse_out_header + fuse_entry_out</text>
<text x="546" y="90" text-anchor="middle" font-family="Courier" font-size="9.5" font-weight="bold" fill="#0F6E56">+ fuse_open_out</text>
<text x="546" y="106" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: WRITE</text>
<text x="340" y="148" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#5F5E5A">Response combines entry attributes and open file handle in one round-trip against the root inode</text>
</svg>"""

# ── 10h. FUSE_RELEASE (close) descriptor chain ───────────────────────────────
svgs["release_chain"] = """<svg width="680" height="160" viewBox="0 0 680 160" xmlns="http://www.w3.org/2000/svg">
<rect width="680" height="160" fill="white"/>
<text x="340" y="20" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="#185FA5">FUSE Release (Close) — Descriptor Chain</text>
<text x="162" y="40" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">← Readable (driver→daemon) →</text>
<text x="507" y="40" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#0F6E56">← Writable (daemon→driver) →</text>
<line x1="335" y1="46" x2="335" y2="130" stroke="#aaa" stroke-width="0.8" stroke-dasharray="4 3"/>
<!-- Descriptor 0: release request (R) -->
<rect x="10" y="50" width="305" height="70" rx="6" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.8"/>
<text x="162" y="75" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#185FA5">virtio_fs_release_req</text>
<text x="162" y="92" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">fuse_in_header + fuse_release_in (fh, flags)</text>
<text x="162" y="109" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: READ</text>
<!-- Arrow -->
<text x="323" y="89" text-anchor="middle" font-family="Helvetica" font-size="14" fill="#185FA5">→</text>
<!-- Descriptor 1: release response (W) -->
<rect x="345" y="50" width="325" height="70" rx="6" fill="#D4F0E5" stroke="#0F6E56" stroke-width="0.8"/>
<text x="507" y="75" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#0F6E56">fuse_out_header</text>
<text x="507" y="92" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#0F6E56">error status only</text>
<text x="507" y="109" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: WRITE</text>
<text x="340" y="148" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#5F5E5A">No data returned; descriptor removed from _fd_info_map and FUSE_FORGET sent on the high-priority queue</text>
</svg>"""

# ── 10i. Unlink descriptor chain (implementation) ────────────────────────────
svgs["unlink_chain"] = """<svg width="680" height="160" viewBox="0 0 680 160" xmlns="http://www.w3.org/2000/svg">
<rect width="680" height="160" fill="white"/>
<text x="340" y="20" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="#185FA5">FUSE Unlink — Descriptor Chain</text>
<text x="203" y="40" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">← Readable (driver→daemon) →</text>
<text x="548" y="40" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#0F6E56">← Writable (daemon→driver) →</text>
<!-- Divider -->
<line x1="415" y1="46" x2="415" y2="130" stroke="#aaa" stroke-width="0.8" stroke-dasharray="4 3"/>
<!-- Descriptor 0: fixed request header (R) -->
<rect x="10" y="50" width="185" height="70" rx="6" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.8"/>
<text x="102" y="75" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#185FA5">virtio_fs_unlink_req</text>
<text x="102" y="92" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">fuse_in_header</text>
<text x="102" y="109" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: READ</text>
<!-- chain arrow 0→1 -->
<text x="203" y="89" text-anchor="middle" font-family="Helvetica" font-size="14" fill="#185FA5">→</text>
<!-- Descriptor 1: name/path string (R) -->
<rect x="211" y="50" width="195" height="70" rx="6" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.8"/>
<text x="308" y="75" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#185FA5">name / path</text>
<text x="308" y="92" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">const char* (null-terminated, +1 offset)</text>
<text x="308" y="109" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: READ</text>
<!-- chain arrow 1→2 -->
<text x="413" y="89" text-anchor="middle" font-family="Helvetica" font-size="14" fill="#185FA5">→</text>
<!-- Descriptor 2: fuse_out_header (W) -->
<rect x="423" y="50" width="247" height="70" rx="6" fill="#D4F0E5" stroke="#0F6E56" stroke-width="0.8"/>
<text x="546" y="75" text-anchor="middle" font-family="Courier" font-size="10" font-weight="bold" fill="#0F6E56">fuse_out_header</text>
<text x="546" y="92" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#0F6E56">error + unique + len</text>
<text x="546" y="109" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#5F5E5A">Flags: WRITE</text>
<text x="340" y="148" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#5F5E5A">Name pointer is offset +1 byte to strip the leading path separator added by the VFS layer</text>
</svg>"""

# ── 11. VFS dispatch diagram (implementation) ────────────────────────────────
svgs["vfs_dispatch"] = """<svg width="680" height="260" viewBox="0 0 680 260" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#185FA5" stroke-width="1.5" stroke-linecap="round"/></marker></defs>
<rect width="680" height="260" fill="white"/>
<text x="340" y="20" text-anchor="middle" font-family="Helvetica" font-size="12" font-weight="bold" fill="#185FA5">VFS Layer — Path Dispatch and File Descriptor Lifecycle</text>
<!-- MUSL -->
<rect x="20" y="36" width="120" height="40" rx="6" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="80" y="60" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">MUSL syscall</text>
<!-- arrow MUSL -> sys_open -->
<line x1="140" y1="56" x2="186" y2="56" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<text x="163" y="49" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#185FA5">open(path)</text>
<!-- sys_open -->
<rect x="186" y="36" width="140" height="40" rx="6" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="256" y="60" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">sys_open stub</text>
<!-- arrow -> VFS lookup -->
<line x1="326" y1="56" x2="372" y2="56" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<text x="349" y="49" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#185FA5">prefix lookup</text>
<!-- fs::VFS -->
<rect x="372" y="36" width="130" height="40" rx="6" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="437" y="54" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">fs::VFS</text>
<text x="437" y="70" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E6F1FB">mount table</text>
<!-- arrow -> driver open -->
<line x1="502" y1="56" x2="548" y2="56" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<text x="525" y="49" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#185FA5">open(fd, tail)</text>
<!-- VirtioFS_device -->
<rect x="548" y="36" width="116" height="40" rx="6" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="606" y="54" text-anchor="middle" font-family="Helvetica" font-size="10" font-weight="bold" fill="white">VirtioFS</text>
<text x="606" y="70" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E6F1FB">_device driver</text>

<!-- FD_map box -->
<rect x="186" y="110" width="140" height="40" rx="6" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.8"/>
<text x="256" y="128" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="#185FA5">FD_map</text>
<text x="256" y="144" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">integer fd allocator</text>
<!-- File_FD box -->
<rect x="372" y="110" width="130" height="40" rx="6" fill="#DAEAF8" stroke="#185FA5" stroke-width="0.8"/>
<text x="437" y="128" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="#185FA5">File_FD</text>
<text x="437" y="144" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">per-file state</text>

<!-- arrows for lifecycle -->
<line x1="256" y1="76" x2="256" y2="110" stroke="#185FA5" stroke-width="1" stroke-dasharray="3 2" marker-end="url(#a)"/>
<text x="270" y="96" font-family="Helvetica" font-size="8" fill="#185FA5">alloc fd</text>
<line x1="326" y1="130" x2="372" y2="130" stroke="#185FA5" stroke-width="1" stroke-dasharray="3 2" marker-end="url(#a)"/>
<text x="349" y="123" text-anchor="middle" font-family="Helvetica" font-size="8" fill="#185FA5">bind Filesystem</text>
<line x1="502" y1="130" x2="548" y2="76" stroke="#185FA5" stroke-width="1" stroke-dasharray="3 2" marker-end="url(#a)"/>
<text x="540" y="110" font-family="Helvetica" font-size="8" fill="#185FA5">dispatch</text>

<!-- subsequent IO path -->
<rect x="20" y="190" width="640" height="56" rx="8" fill="#EEF4FB" stroke="#85B7EB" stroke-width="0.8"/>
<text x="340" y="210" text-anchor="middle" font-family="Helvetica" font-size="10" font-weight="bold" fill="#185FA5">Subsequent I/O (read/write/lseek/close) — no path resolution</text>
<text x="340" y="228" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">MUSL stub → FD_map::_get(fd) → File_FD::method() → Filesystem fn ptr → VirtioFS_device</text>
<text x="340" y="244" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#5F5E5A">Descriptors 1 &amp; 2 intercepted before FD_map — routed directly to os::print</text>
</svg>"""

OUT_DIRS = [
    "/sessions/peaceful-ecstatic-mayer/mnt/ldrago_masters/thesis_output/diagrams",
    "/sessions/peaceful-ecstatic-mayer/build/diagrams",
]
for d in OUT_DIRS:
    os.makedirs(d, exist_ok=True)

for name, svg in svgs.items():
    for d in OUT_DIRS:
        path = f"{d}/{name}.png"
        cairosvg.svg2png(bytestring=svg.encode(), write_to=path, scale=2.0)
    print(f"  {name}.png")

print("All done")
