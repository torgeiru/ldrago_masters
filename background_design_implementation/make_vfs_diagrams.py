import cairosvg

# Exact same style as virtiofs_init:
# - cx=140, bw=148, bh=42, gap=22 (arrow length between boxes)
# - Error boxes at x=right_edge+gap, same height as main boxes
# - No diamonds — branch label on the arrow itself
# - font-size 11 bold title, 9 Courier sub, 9 label

def make(name, viewH, body):
    svg = f'''<svg width="680" height="{viewH}" viewBox="0 0 680 {viewH}" xmlns="http://www.w3.org/2000/svg">
<defs>
  <marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="#185FA5" stroke-width="1.5" stroke-linecap="round"/>
  </marker>
  <marker id="r" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="#E24B4A" stroke-width="1.5" stroke-linecap="round"/>
  </marker>
  <marker id="g" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="#0F6E56" stroke-width="1.5" stroke-linecap="round"/>
  </marker>
</defs>
<rect width="680" height="{viewH}" fill="white"/>
{body}
</svg>'''
    with open(f"/home/claude/diagrams/{name}.png", "wb") as f:
        f.write(cairosvg.svg2png(bytestring=svg.encode(), scale=2.0))
    print(f"  {name}.png")

CX  = 140   # centre x of main column
X0  = 66    # left edge of main box (CX - 74)
BW  = 148   # box width
BH  = 42    # box height
G   = 22    # arrow gap between boxes
ERX = 230   # error box left x
ERW = 210   # error box width

def B(y, title, sub=None, color="#378ADD", stroke="#185FA5", tc="white", sc="#E6F1FB"):
    cy = y + BH//2 - (6 if sub else 0)
    s = f'<rect x="{X0}" y="{y}" width="{BW}" height="{BH}" rx="7" fill="{color}" stroke="{stroke}" stroke-width="0.5"/>\n'
    s += f'<text x="{CX}" y="{cy}" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="{tc}">{title}</text>\n'
    if sub:
        s += f'<text x="{CX}" y="{y+BH//2+10}" text-anchor="middle" font-family="Courier" font-size="9" fill="{sc}">{sub}</text>\n'
    return s

def ARR(x, y1, y2, color="#185FA5", m="url(#a)"):
    return f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{color}" stroke-width="1" marker-end="{m}"/>\n'

def ARRH(x1, x2, y, color="#185FA5", m="url(#a)"):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{color}" stroke-width="1" marker-end="{m}"/>\n'

def LBL(x, y, t, anchor="middle", color="#185FA5", size=9):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Helvetica" font-size="{size}" fill="{color}">{t}</text>\n'

def ERR(y_mid, label, note="", color="#E24B4A", stroke="#A32D2D", tc="white", mc="url(#r)", lc="#E24B4A"):
    ey = y_mid - BH//2
    s  = ARRH(X0+BW, ERX, y_mid, "#E24B4A", mc)
    s += f'<rect x="{ERX}" y="{ey}" width="{ERW}" height="{BH}" rx="7" fill="{color}" stroke="{stroke}" stroke-width="0.5"/>\n'
    s += f'<text x="{ERX+ERW//2}" y="{y_mid+5}" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="{tc}">{label}</text>\n'
    if note:
        s += LBL(ERX+4, ey-4, note, "start", lc)
    return s

def SUCC(y, label, color="#1D9E75", stroke="#0F6E56"):
    return (f'<rect x="{X0}" y="{y}" width="{BW}" height="{BH}" rx="7" fill="{color}" stroke="{stroke}" stroke-width="0.5"/>\n'
            f'<text x="{CX}" y="{y+BH//2+5}" text-anchor="middle" font-family="Helvetica" font-size="11" font-weight="bold" fill="white">{label}</text>\n')

# ─────────────────────────────────────
#  1. sys_open
# ─────────────────────────────────────
b = ""; y = 20
b += B(y, "Parse path", "fs::Path{p}")
b += ARR(CX, y+BH, y+BH+G); y += BH+G

b += B(y, "Lookup prefix", "VFS::get_mounts()")
b += ERR(y+BH//2, "return -ENOENT", "not found")
b += ARR(CX, y+BH, y+BH+G); y += BH+G

b += B(y, "Alloc File_FD", "FD_map::_open&lt;File_FD&gt;(fs)")
b += ARR(CX, y+BH, y+BH+G); y += BH+G

b += B(y, "fs.open(fd, tail, ...)", "driver open fn ptr")
b += ERR(y+BH//2, "close fd, return err", "result != 0 / throw")
b += ARR(CX, y+BH, y+BH+G); y += BH+G

b += SUCC(y, "return fd")
H = y+BH+20
make("vfs_sys_open", H, b)

# ─────────────────────────────────────
#  2. sys_read/readv/write/writev
# ─────────────────────────────────────
b = ""; y = 20
b += B(y, "fd == 1 or 2?", "write / writev only",
       color="#DAEAF8", stroke="#185FA5", tc="#185FA5", sc="#5F5E5A")
b += ERR(y+BH//2, "os::print() → return", "yes",
         color="#1D9E75", stroke="#0F6E56", tc="white", mc="url(#g)", lc="#0F6E56")
b += ARR(CX, y+BH, y+BH+G); y += BH+G

b += B(y, "FD_map::_get(fd)", "→ File_FD*")
b += ERR(y+BH//2, "return -EBADF", "nullptr")
b += ARR(CX, y+BH, y+BH+G); y += BH+G

b += B(y, "fde-&gt;method(args)", "virtual dispatch")
b += ARR(CX, y+BH, y+BH+G); y += BH+G

b += B(y, "Filesystem fn ptr(fd,...)", "→ driver")
b += ERR(y+BH//2, "return -ENOSYS", "throw")
b += ARR(CX, y+BH, y+BH+G); y += BH+G

b += SUCC(y, "return result")
H = y+BH+20
make("vfs_sys_io", H, b)

# ─────────────────────────────────────
#  3. sys_close
# ─────────────────────────────────────
b = ""; y = 20
b += B(y, "FD_map::_get(fd)", "→ File_FD*")
b += ERR(y+BH//2, "return -EBADF", "nullptr")
b += ARR(CX, y+BH, y+BH+G); y += BH+G

b += B(y, "fde-&gt;close()", "driver close fn ptr")
b += ERR(y+BH//2, "os::panic()", "result != 0")
b += ARR(CX, y+BH, y+BH+G); y += BH+G

b += B(y, "FD_map::close(fd)", "release descriptor")
b += ARR(CX, y+BH, y+BH+G); y += BH+G

b += SUCC(y, "return 0")
H = y+BH+20
make("vfs_sys_close", H, b)

# ─────────────────────────────────────
#  4. sys_unlink
# ─────────────────────────────────────
b = ""; y = 20
b += B(y, "Parse path", "fs::Path{p}")
b += ARR(CX, y+BH, y+BH+G); y += BH+G

b += B(y, "Lookup prefix", "VFS::get_mounts()")
b += ERR(y+BH//2, "return -ENOENT / -ENOSYS", "not found / throw")
b += ARR(CX, y+BH, y+BH+G); y += BH+G

b += B(y, "fs.unlink(tail)", "direct driver call — no fd")
b += ARR(CX, y+BH, y+BH+G); y += BH+G

b += SUCC(y, "return 0")
H = y+BH+20
make("vfs_sys_unlink", H, b)

print("done")
