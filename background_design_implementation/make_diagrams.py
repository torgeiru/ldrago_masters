import cairosvg, os
os.makedirs("/home/claude/diagrams", exist_ok=True)

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

# ── 5. VirtioFS Static Component Overview ────────────────────────────────────
svgs["virtiofs_static"] = """<svg width="680" height="380" viewBox="0 0 680 380" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#185FA5" stroke-width="1.5" stroke-linecap="round"/></marker></defs>
<rect width="680" height="380" fill="white"/>
<!-- User Space -->
<rect x="10" y="10" width="658" height="216" rx="16" fill="#EEF4FB" stroke="#85B7EB" stroke-width="1"/>
<text x="30" y="36" font-family="Helvetica" font-size="11" font-weight="bold" fill="#185FA5">User space</text>
<!-- QEMU Process -->
<rect x="26" y="46" width="624" height="166" rx="10" fill="#DAEAF8" stroke="#85B7EB" stroke-width="0.8"/>
<text x="44" y="66" font-family="Helvetica" font-size="10" fill="#185FA5">QEMU process</text>
<!-- Guest VM -->
<rect x="42" y="74" width="340" height="124" rx="8" fill="#EEF4FB" stroke="#378ADD" stroke-width="0.8"/>
<text x="58" y="92" font-family="Helvetica" font-size="10" fill="#185FA5">Guest VM</text>
<!-- VirtioFS Driver chip -->
<rect x="58" y="98" width="118" height="42" rx="6" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="117" y="115" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">VirtioFS</text>
<text x="117" y="131" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#E6F1FB">guest driver</text>
<!-- Shared Memory guest chip -->
<rect x="226" y="98" width="136" height="42" rx="6" fill="#042C53" stroke="#185FA5" stroke-width="0.5"/>
<text x="294" y="115" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">Shared memory</text>
<text x="294" y="131" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#B5D4F4">virtqueue ring</text>
<!-- arrow driver -> shared mem -->
<line x1="176" y1="119" x2="224" y2="119" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<!-- VirtioFSD box -->
<rect x="42" y="156" width="200" height="68" rx="8" fill="#EEF4FB" stroke="#378ADD" stroke-width="0.8"/>
<text x="58" y="174" font-family="Helvetica" font-size="10" fill="#185FA5">VirtioFSD process</text>
<rect x="58" y="180" width="136" height="34" rx="6" fill="#042C53" stroke="#185FA5" stroke-width="0.5"/>
<text x="126" y="201" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">Shared memory</text>
<!-- bidirectional dashed arrows between shared memory blocks -->
<line x1="272" y1="140" x2="166" y2="180" stroke="#378ADD" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#a)"/>
<line x1="156" y1="180" x2="262" y2="140" stroke="#378ADD" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#a)"/>
<!-- KVM box -->
<rect x="408" y="74" width="210" height="100" rx="8" fill="#EEF4FB" stroke="#378ADD" stroke-width="0.8"/>
<text x="424" y="92" font-family="Helvetica" font-size="10" fill="#185FA5">Hypervisor</text>
<rect x="424" y="98" width="178" height="42" rx="6" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="513" y="123" text-anchor="middle" font-family="Helvetica" font-size="13" font-weight="bold" fill="white">KVM</text>
<!-- Kernel Space -->
<rect x="10" y="240" width="658" height="128" rx="16" fill="#EDF7F3" stroke="#5DCAA5" stroke-width="1"/>
<text x="30" y="264" font-family="Helvetica" font-size="11" font-weight="bold" fill="#0F6E56">Kernel space</text>
<!-- VFS subsystem box -->
<rect x="26" y="272" width="310" height="84" rx="10" fill="#D4F0E5" stroke="#5DCAA5" stroke-width="0.8"/>
<text x="42" y="290" font-family="Helvetica" font-size="10" fill="#0F6E56">VFS subsystem</text>
<rect x="42" y="296" width="88" height="34" rx="6" fill="#1D9E75" stroke="#0F6E56" stroke-width="0.5"/>
<text x="86" y="317" text-anchor="middle" font-family="Helvetica" font-size="10" font-weight="bold" fill="white">EXT4 driver</text>
<rect x="138" y="296" width="88" height="34" rx="6" fill="#1D9E75" stroke="#0F6E56" stroke-width="0.5"/>
<text x="182" y="317" text-anchor="middle" font-family="Helvetica" font-size="10" font-weight="bold" fill="white">XFS driver</text>
<rect x="234" y="296" width="88" height="34" rx="6" fill="#1D9E75" stroke="#0F6E56" stroke-width="0.5"/>
<text x="278" y="317" text-anchor="middle" font-family="Helvetica" font-size="10" font-weight="bold" fill="white">VirtioFS drv</text>
<!-- KVM kernel module -->
<rect x="352" y="272" width="300" height="84" rx="10" fill="#D4F0E5" stroke="#5DCAA5" stroke-width="0.8"/>
<text x="368" y="290" font-family="Helvetica" font-size="10" fill="#0F6E56">KVM kernel module</text>
<rect x="368" y="296" width="268" height="34" rx="6" fill="#1D9E75" stroke="#0F6E56" stroke-width="0.5"/>
<text x="502" y="317" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">KVM module</text>
<!-- KVM user->kernel arrow -->
<line x1="513" y1="226" x2="513" y2="240" stroke="#185FA5" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#a)"/>
<text x="528" y="236" font-family="Helvetica" font-size="9" fill="#185FA5">VM exits</text>
<!-- separator line -->
<line x1="10" y1="236" x2="670" y2="236" stroke="#aaa" stroke-width="0.5" stroke-dasharray="5 4"/>
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
<rect x="272" y="10" width="76" height="44" rx="6" fill="#378ADD" stroke="#185FA5" stroke-width="0.5"/>
<text x="310" y="35" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">KVM</text>
<rect x="386" y="10" width="96" height="44" rx="6" fill="#1D9E75" stroke="#0F6E56" stroke-width="0.5"/>
<text x="434" y="35" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">VirtioFSD</text>
<rect x="520" y="10" width="96" height="44" rx="6" fill="#1D9E75" stroke="#0F6E56" stroke-width="0.5"/>
<text x="568" y="35" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">Host VFS</text>
<!-- Lifelines -->
<line x1="55" y1="54" x2="55" y2="540" stroke="#85B7EB" stroke-width="0.5" stroke-dasharray="4 4"/>
<line x1="181" y1="54" x2="181" y2="540" stroke="#85B7EB" stroke-width="0.5" stroke-dasharray="4 4"/>
<line x1="310" y1="54" x2="310" y2="540" stroke="#85B7EB" stroke-width="0.5" stroke-dasharray="4 4"/>
<line x1="434" y1="54" x2="434" y2="540" stroke="#5DCAA5" stroke-width="0.5" stroke-dasharray="4 4"/>
<line x1="568" y1="54" x2="568" y2="540" stroke="#5DCAA5" stroke-width="0.5" stroke-dasharray="4 4"/>
<!-- Activation bars -->
<rect x="51" y="78" width="8" height="432" rx="2" fill="#DAEAF8" stroke="#85B7EB" stroke-width="0.5"/>
<rect x="177" y="98" width="8" height="412" rx="2" fill="#DAEAF8" stroke="#85B7EB" stroke-width="0.5"/>
<rect x="430" y="242" width="8" height="202" rx="2" fill="#D4F0E5" stroke="#5DCAA5" stroke-width="0.5"/>
<!-- Start dot -->
<circle cx="55" cy="78" r="5" fill="#378ADD"/>
<!-- msg 1: virtiofs_read -->
<line x1="59" y1="98" x2="177" y2="98" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<text x="116" y="92" text-anchor="middle" font-family="Courier" font-size="9" fill="#185FA5">virtiofs_read(...)</text>
<!-- msg 2: forge_request self-call -->
<path d="M185 128 Q214 128 214 142 Q214 156 185 156" fill="none" stroke="#378ADD" stroke-width="0.8" marker-end="url(#a)"/>
<text x="220" y="145" font-family="Courier" font-size="9" fill="#185FA5">forge_request()</text>
<!-- msg 3: queue_request self-call -->
<path d="M185 180 Q214 180 214 194 Q214 208 185 208" fill="none" stroke="#378ADD" stroke-width="0.8" marker-end="url(#a)"/>
<text x="220" y="197" font-family="Courier" font-size="9" fill="#185FA5">queue_request()</text>
<!-- phase band -->
<rect x="118" y="222" width="492" height="20" rx="3" fill="#DAEAF8" stroke="#85B7EB" stroke-width="0.5"/>
<text x="364" y="236" text-anchor="middle" font-family="Helvetica" font-size="9" fill="#185FA5">VM exit — notification crossing</text>
<!-- msg 4: signal_queue -> KVM -->
<line x1="185" y1="258" x2="308" y2="258" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<text x="244" y="252" text-anchor="middle" font-family="Courier" font-size="9" fill="#185FA5">signal_queue()</text>
<rect x="306" y="248" width="8" height="24" rx="2" fill="#DAEAF8" stroke="#85B7EB" stroke-width="0.5"/>
<!-- msg 5: notify -> VirtioFSD -->
<line x1="314" y1="260" x2="430" y2="260" stroke="#185FA5" stroke-width="1" marker-end="url(#a)"/>
<text x="370" y="254" text-anchor="middle" font-family="Courier" font-size="9" fill="#185FA5">notify()</text>
<!-- msg 6: await_reply self-call -->
<path d="M185 286 Q214 286 214 300 Q214 314 185 314" fill="none" stroke="#378ADD" stroke-width="0.8" marker-end="url(#a)"/>
<text x="220" y="303" font-family="Courier" font-size="9" fill="#185FA5">await_reply()</text>
<!-- msg 7: read -> Host VFS -->
<line x1="438" y1="344" x2="566" y2="344" stroke="#0F6E56" stroke-width="1" marker-end="url(#t)"/>
<text x="500" y="338" text-anchor="middle" font-family="Courier" font-size="9" fill="#0F6E56">read(...)</text>
<rect x="564" y="344" width="8" height="36" rx="2" fill="#D4F0E5" stroke="#5DCAA5" stroke-width="0.5"/>
<!-- msg 8: read data <- Host VFS (dashed) -->
<line x1="564" y1="390" x2="438" y2="390" stroke="#5DCAA5" stroke-width="1" stroke-dasharray="5 3" marker-end="url(#t)"/>
<text x="500" y="384" text-anchor="middle" font-family="Courier" font-size="9" fill="#0F6E56">read data</text>
<!-- msg 9: forge_response self -->
<path d="M438 416 Q466 416 466 430 Q466 444 438 444" fill="none" stroke="#1D9E75" stroke-width="0.8" marker-end="url(#t)"/>
<text x="472" y="433" font-family="Courier" font-size="9" fill="#0F6E56">forge_response()</text>
<!-- msg 10: queue_response self -->
<path d="M438 462 Q466 462 466 476 Q466 490 438 490" fill="none" stroke="#1D9E75" stroke-width="0.8" marker-end="url(#t)"/>
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

for name, svg in svgs.items():
    path = f"/home/claude/diagrams/{name}.png"
    cairosvg.svg2png(bytestring=svg.encode(), write_to=path, scale=2.0)
    print(f"  {name}.png")

print("All done")
