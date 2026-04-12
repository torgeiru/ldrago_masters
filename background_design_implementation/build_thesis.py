from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    HRFlowable, Image
)
from PIL import Image as PILImage

W, H = A4
L_MARGIN = 3.2*cm
R_MARGIN = 3.2*cm
T_MARGIN = 3.0*cm
B_MARGIN = 3.0*cm

doc = SimpleDocTemplate("/home/claude/thesis_v3.pdf", pagesize=A4,
    leftMargin=L_MARGIN, rightMargin=R_MARGIN,
    topMargin=T_MARGIN, bottomMargin=B_MARGIN,
    title="VirtioFS Driver for IncludeOS", author="Master's Thesis")

BLUE      = colors.HexColor("#378ADD")
DARK_BLUE = colors.HexColor("#185FA5")
GRAY      = colors.HexColor("#5F5E5A")
LGRAY     = colors.HexColor("#888780")
TEXT      = colors.HexColor("#1a1a1a")

def S(n, **k): return ParagraphStyle(n, **k)

body    = S("body",    fontName="Helvetica",            fontSize=11.5, leading=19, spaceAfter=12, spaceBefore=2,  alignment=TA_JUSTIFY, textColor=TEXT)
h1      = S("h1",     fontName="Helvetica-Bold",        fontSize=22,   leading=28, spaceBefore=0, spaceAfter=16, textColor=DARK_BLUE)
h2      = S("h2",     fontName="Helvetica-Bold",        fontSize=15,   leading=20, spaceBefore=26,spaceAfter=10, textColor=DARK_BLUE)
h3      = S("h3",     fontName="Helvetica-Bold",        fontSize=12.5, leading=17, spaceBefore=18,spaceAfter=6,  textColor=DARK_BLUE)
h4      = S("h4",     fontName="Helvetica-BoldOblique", fontSize=11.5, leading=16, spaceBefore=14,spaceAfter=4,  textColor=LGRAY)
bullet  = S("bullet", fontName="Helvetica",             fontSize=11.5, leading=18, spaceAfter=5,  leftIndent=22, textColor=TEXT)
# Shorter, tighter caption
caption = S("caption", fontName="Helvetica-Oblique",   fontSize=8.5,  leading=12, spaceAfter=18, spaceBefore=4, alignment=TA_CENTER, textColor=LGRAY)
chapnum = S("chapnum", fontName="Helvetica-Bold",       fontSize=12,   leading=16, spaceAfter=4,  textColor=BLUE)
bib     = S("bib",     fontName="Helvetica",            fontSize=10,   leading=15, spaceAfter=8,  leftIndent=28, firstLineIndent=-28, alignment=TA_JUSTIFY, textColor=TEXT)
eqstyle = S("eq",      fontName="Helvetica-Oblique",   fontSize=11.5, leading=18, spaceAfter=12, spaceBefore=6, leftIndent=56, textColor=TEXT)

def chapter(n, t):
    return [PageBreak(), Spacer(1, 0.6*cm),
            Paragraph(f"Chapter {n}", chapnum), Paragraph(t, h1),
            HRFlowable(width="100%", thickness=1.8, color=BLUE, spaceAfter=20)]

def sec(t):   return [Paragraph(t, h2)]
def sub(t):   return [Paragraph(t, h3)]
def ssub(t):  return [Paragraph(t, h4)]
def p(t):     return Paragraph(t, body)
def sp(n=8):  return Spacer(1, n)
def bl(items):return [Paragraph(f"&#8226;&#160;&#160;{i}", bullet) for i in items]
def eq(t):    return [Spacer(1,4), Paragraph(t, eqstyle), Spacer(1,4)]

def fig(path, cap, max_w_frac=0.90, max_h_cm=None):
    """Embed image at correct aspect ratio. max_w_frac controls width as fraction
    of text width. max_h_cm caps height so tall diagrams don't fill the page."""
    im = PILImage.open(path)
    px_w, px_h = im.size
    aspect = px_h / px_w

    w = doc.width * max_w_frac
    h = w * aspect

    # If it would be too tall, shrink to fit
    if max_h_cm and h > max_h_cm * cm:
        h = max_h_cm * cm
        w = h / aspect

    img = Image(path, width=w, height=h)
    img.hAlign = "CENTER"
    return [Spacer(1, 10), img, Paragraph(cap, caption)]

# ═══════════════════════════════════════════════════════════════════════
story = []

# ═══════════════════════════════════════════════════════════════════════
#  CHAPTER 1 — BACKGROUND
# ═══════════════════════════════════════════════════════════════════════
story += chapter(1, "Background")

story += sec("1.1  System Emulation and Virtualization")
story += sub("Overview")
story += [
    p("System emulation involves reproducing the behaviour of a complete machine in "
      "software, including its CPU, memory subsystem, chipset, and peripheral devices. "
      "Each component is implemented as a separate subsystem within the emulator. The "
      "CPU emulator executes instructions until an operation requires interaction with "
      "an emulated device, at which point control transfers to the appropriate device "
      "emulation subsystem. This model is known as <b>trap-and-emulate</b>, rooted in "
      "the foundational Popek and Goldberg [1] virtualization paper, which establishes "
      "that sensitive instructions must trap so they can be intercepted and handled by "
      "the virtual machine monitor (VMM)."),
]

story += sub("QEMU and KVM")
story += [
    p("<b>QEMU</b> [2] is an open-source machine emulator supporting full system "
      "emulation across multiple CPU architectures. In pure software mode it uses "
      "dynamic binary translation via its Tiny Code Generator (TCG). When hardware "
      "virtualization extensions are available — Intel VT-x or AMD SVM — QEMU delegates "
      "CPU execution to <b>KVM</b> [3], a Linux kernel module that exposes an API for "
      "building hypervisors. Under KVM, guest instructions execute directly on the host "
      "CPU; only sensitive instructions cause VM exits."),
    sp(),
    p("QEMU interacts with KVM through <font face='Courier'>ioctl</font> calls on "
      "<font face='Courier'>/dev/kvm</font>. vCPUs are managed as ordinary Linux "
      "threads via <font face='Courier'>KVM_RUN</font>, which blocks until the vCPU "
      "hits a sensitive instruction or accesses an MMIO/PMIO region. For "
      "higher-performance signalling, KVM supports "
      "<font face='Courier'>ioeventfd</font> [4]: event file descriptors that deliver "
      "guest-write notifications directly to a waiting user-space thread, bypassing the "
      "QEMU event loop entirely. This mechanism underpins vhost-user and VirtioFSD."),
]

story += sub("Vhost-User Architecture")
story += [
    p("QEMU supports offloading device emulation to auxiliary user-space daemons via "
      "the <b>vhost-user</b> protocol [5], sharing the following over a UNIX domain "
      "socket:"),
    sp(4),
]
story += bl([
    "Physical addresses of Virtio queue memory regions — enabling direct shared-memory "
    "access without copying through QEMU.",
    "<font face='Courier'>ioeventfd</font> descriptors for kick notification.",
    "<font face='Courier'>irqfd</font> descriptors for interrupt injection into the guest.",
])
story += [
    sp(4),
    p("<b>VirtioFSD</b> is the principal example, implementing a complete file-system "
      "device in a separate user-space daemon, handling the full request lifecycle — "
      "notification, parsing, processing, and response — without involving QEMU."),
]

story += sec("1.2  Dual Ring Buffer")
story += [
    p("The circular ring buffer is one of the most ubiquitous data structures in "
      "systems programming. It enables lockless access by having one thread enqueue "
      "entries while another dequeues and consumes them — as long as only one producer "
      "and one consumer operate concurrently, no locks are required."),
    sp(),
    p("The <b>dual ring buffer</b> pattern — a term coined here for lack of a standard "
      "abstract name — consists of two circular ring buffers. The first ring buffer "
      "carries requests from client to server; the second carries responses from server "
      "to client. Together they form a lockless request–response channel. This pattern "
      "is the foundational atom of both io_uring and Virtio, and understanding it is "
      "essential for understanding either."),
]

story += sec("1.3  Memory Ordering")
story += sub("The x86 Memory Model")
story += [
    p("The x86 architecture implements a relatively strong memory model known as "
      "<b>Total Store Ordering (TSO)</b>. Under TSO, read and store instructions are "
      "generally not reordered with one notable exception: older stores may be "
      "reordered with younger loads to <i>different</i> memory locations. Critically, the executing CPU "
      "itself still sees a consistent view of its own memory operations — the reordering "
      "is only visible to <i>other</i> CPUs observing the memory bus."),
]

story += sub("The C++ Memory Model")
story += [
    p("The C++ memory model, introduced in C++11, provides a portable abstraction over "
      "hardware memory models. It defines a set of memory orderings that the programmer "
      "can attach to atomic operations to control visibility and synchronization "
      "guarantees across threads:"),
    sp(4),
]
story += bl([
    "<font face='Courier'>memory_order_relaxed</font>: no synchronization or ordering "
    "guarantee beyond atomicity of the operation itself.",
    "<font face='Courier'>memory_order_acquire</font>: no reads or writes in the "
    "current thread can be reordered before this load. Pairs with a release on another "
    "thread to establish a happens-before relationship.",
    "<font face='Courier'>memory_order_release</font>: no reads or writes in the "
    "current thread can be reordered after this store. All prior writes become visible "
    "to any thread that performs an acquire on the same atomic variable.",
    "<font face='Courier'>memory_order_seq_cst</font>: the strongest ordering. "
    "Establishes a single total order of all sequentially consistent operations across "
    "all threads.",
])
story += [
    sp(4),
    p("In the context of the Virtio split queue, the C++ memory model is applied "
      "precisely: a <font face='Courier'>memory_order_release</font> fence is issued "
      "after populating the descriptor chain and before incrementing the available ring "
      "index, ensuring all descriptor writes are visible to the device before it "
      "observes the updated index. A subsequent "
      "<font face='Courier'>memory_order_seq_cst</font> fence precedes the check of "
      "the used ring's notification suppression flag, preventing reordering that could "
      "cause a missed notification."),
]

story += sec("1.4  io_uring")
story += [
    p("io_uring is a modern Linux I/O interface introduced in kernel 5.1, designed to "
      "address the performance inefficiencies of POSIX I/O and earlier asynchronous "
      "I/O mechanisms such as AIO. The primary selling point of io_uring is its ability "
      "to greatly reduce — and in some configurations eliminate entirely — the number "
      "of system calls required to perform I/O."),
    sp(),
    p("io_uring is built on the dual ring buffer pattern described in Section 1.2. It "
      "exposes two shared-memory ring buffers between user space and the kernel: the "
      "<b>submission queue (SQ)</b>, into which the application places I/O requests, "
      "and the <b>completion queue (CQ)</b>, from which the application reads "
      "completions. Because both rings live in shared memory, the application can "
      "submit requests and harvest completions without any system call, provided the "
      "kernel is actively polling the submission queue."),
    sp(),
    p("io_uring supports a polling mode called <b>SQPOLL</b>, in which a dedicated "
      "kernel thread continuously polls the submission queue for new entries. In this "
      "mode, applications can perform I/O with zero system calls for the duration of "
      "the polling window. When the kernel thread has been idle for a configurable "
      "timeout, it sleeps and requires a wakeup syscall "
      "(<font face='Courier'>io_uring_enter</font>) to resume. "
      "<b>IOPOLL</b> is an additional polling mode for completion events, available "
      "only for devices that support it such as NVMe drives with polling queues."),
    sp(),
    p("<b>liburing</b> is a user-space wrapper library around the io_uring API. "
      "io_uring's raw interface involves careful management of ring indices, memory "
      "barriers, and kernel flags; liburing encapsulates this complexity and provides "
      "a higher-level interface that substantially reduces the boilerplate required "
      "when writing io_uring applications."),
    sp(),
    p("The architectural similarity between io_uring and Virtio is not coincidental: "
      "both implement the dual ring buffer pattern over shared memory to decouple "
      "request submission from completion processing, enabling high-throughput "
      "asynchronous I/O without per-operation kernel crossings."),
]

story += sec("1.5  Virtio Standard")

story += sub("Introduction")
story += [
    p("Virtio is a paravirtualization standard for efficient data exchange between "
      "a guest <i>driver</i> and a host <i>device</i>. It separates a <b>control "
      "plane</b> — device discovery, configuration, and feature negotiation — from a "
      "<b>data plane</b> that exchanges bulk data via shared-memory ring structures "
      "called <i>virtqueues</i>."),
]

story += sub("Device Discovery via PCI")
story += [
    p("Virtio devices advertise their register regions through vendor-specific PCI "
      "capabilities, each with a <font face='Courier'>cfg_type</font> identifying the "
      "region and <font face='Courier'>bar</font>, <font face='Courier'>offset</font>, "
      "and <font face='Courier'>length</font> fields locating it. "
      "Four standard capability types are defined:"),
    sp(4),
]
story += bl([
    "<font face='Courier'>VIRTIO_PCI_CAP_COMMON_CFG</font>: device-wide and per-queue configuration registers.",
    "<font face='Courier'>VIRTIO_PCI_CAP_NOTIFY_CFG</font>: queue notification region.",
    "<font face='Courier'>VIRTIO_PCI_CAP_ISR_CFG</font>: interrupt status register.",
    "<font face='Courier'>VIRTIO_PCI_CAP_DEVICE_CFG</font>: device-class-specific registers.",
])

story += [
    p("The control plane governs the full device lifecycle. The specification prescribes "
      "strict ordering: reset (<font face='Courier'>device_status = 0</font>), set "
      "<font face='Courier'>ACKNOWLEDGE</font> and <font face='Courier'>DRIVER</font> "
      "bits, negotiate features, set <font face='Courier'>FEATURES_OK</font> and verify "
      "the device retains it, configure queues, then set "
      "<font face='Courier'>DRIVER_OK</font>. After setup, MMIO is used only for queue "
      "kicks; under KVM each kick delivers an "
      "<font face='Courier'>ioeventfd</font> notification directly to the device thread."),
]

story += ssub("Descriptor Area")
story += [
    p("The descriptor area is an array of <font face='Courier'>virtq_desc</font> "
      "entries each carrying a guest-physical <b>Buffer</b> address, a byte "
      "<b>Len</b>, <b>Flags</b> (NEXT for chaining, WRITE for device-writable "
      "buffers), and a chain <b>Next</b> index. Readable descriptors must precede all "
      "writable descriptors — no interleaving is permitted. This maps directly onto "
      "the FUSE request–response pattern: the FUSE request occupies the readable "
      "section and the response buffer the writable section."),
]

story += ssub("Request Submission — Driver to Device")
story += [
    p("The driver allocates free descriptors, populates them, links them via the "
      "<font face='Courier'>next</font> field, places the head index into the available "
      "ring's <font face='Courier'>ring[]</font>, and increments the available ring's "
      "<font face='Courier'>idx</font> to expose the request. A "
      "<font face='Courier'>memory_order_release</font> fence precedes the counter "
      "advance. The driver then conditionally writes the queue index to the notification "
      "register to kick the device."),
    sp(4),
]
story += fig("/home/claude/diagrams/avail_enqueue.png",
    "Fig. 1.1 — Driver places descriptor chain head index 0 into ring[0].")
story += fig("/home/claude/diagrams/avail_expose.png",
    "Fig. 1.2 — Driver increments idx to 1 (green), exposing the request. "
    "A release fence precedes the increment.")

story += ssub("Request Completion — Device to Driver")
story += [
    p("After processing a request, the device writes a "
      "<font face='Courier'>virtq_used_elem</font> — containing the head descriptor "
      "index and bytes written into writable buffers — and increments the used ring's "
      "<font face='Courier'>idx</font>. The driver detects completion by comparing "
      "<font face='Courier'>_used_ring->idx</font> against its locally maintained "
      "<font face='Courier'>last_used_idx</font>."),
    sp(4),
]
story += fig("/home/claude/diagrams/used_enqueue.png",
    "Fig. 1.3 — Device writes the completed descriptor head index into used ring[0].")
story += fig("/home/claude/diagrams/used_expose.png",
    "Fig. 1.4 — Device increments used idx to 1 (green), signalling completion.")

story += ssub("Notification Mechanisms")
story += [
    p("Both sides can suppress notifications. The driver sets "
      "<font face='Courier'>VIRTQ_AVAIL_F_NO_INTERRUPT</font> to inhibit device "
      "interrupts; the device sets "
      "<font face='Courier'>VIRTQ_USED_F_NO_NOTIFY</font> to inhibit driver kicks. "
      "These flags enable runtime switching between interrupt-driven and polling modes."),
]

story += sec("1.6  FUSE")
story += sub("Protocol")
story += [
    p("FUSE [7] exports file-system operations to a user-space server. Every request "
      "begins with <font face='Courier'>fuse_in_header</font> carrying the opcode, "
      "total length, a monotonically increasing "
      "<font face='Courier'>unique</font> identifier, and the target inode number. "
      "Every response begins with <font face='Courier'>fuse_out_header</font> echoing "
      "<font face='Courier'>unique</font> and an error code."),
]

story += sub("Initialization Handshake")
story += [
    p("Client and server negotiate protocol version via "
      "<font face='Courier'>FUSE_INIT</font>. The client advertises its major and "
      "minor versions; the negotiated minor is the minimum of the two. If the "
      "server's major is lower, the client must re-send adjusted to the server's "
      "major. The response carries "
      "<font face='Courier'>max_write</font> — the maximum payload the server accepts "
      "per write. The client must cache and enforce this limit."),
]

story += sub("File Operations")
story += [
    p("A complete read sequence issues: "
      "<font face='Courier'>FUSE_LOOKUP</font> (path → inode), "
      "<font face='Courier'>FUSE_OPEN</font> (inode → 64-bit file handle), "
      "<font face='Courier'>FUSE_READ</font> (file handle, buffer, offset, length), "
      "<font face='Courier'>FUSE_RELEASE</font> (free file handle), and "
      "<font face='Courier'>FUSE_FORGET</font> (decrement inode reference count). "
      "Writes follow an analogous pattern; "
      "<font face='Courier'>FUSE_CREATE</font> combines lookup and open for new files."),
]

story += sec("1.7  VirtioFS")
story += [
    p("VirtioFS [8] enables a Linux host and its guest VM to share a designated host "
      "directory. The guest runs the VirtioFS kernel driver; on the host "
      "<b>VirtioFSD</b> acts as a remote file-system server. Communication uses the "
      "FUSE protocol transported over Virtio virtqueues. The shared memory regions are "
      "accessible to both sides without copying through QEMU or the kernel, giving "
      "VirtioFS substantially lower latency than network-based protocols such as "
      "NFS or SMB."),
]
story += fig("/home/claude/diagrams/virtiofs_static.png",
    "Fig. 1.5 — Static component overview. User space (blue): Guest VM with VirtioFS "
    "driver and shared memory, VirtioFSD process, and KVM — all inside QEMU. "
    "Kernel space (green): VFS drivers and KVM module.",
    max_w_frac=0.92, max_h_cm=12)

story += [
    p("Queue 0 is the <i>high-priority</i> queue for latency-sensitive messages such "
      "as <font face='Courier'>FUSE_FORGET</font>; queue 1 is the general-purpose "
      "<i>request</i> queue. VirtioFS supports scatter-gather I/O: a single descriptor "
      "chain may reference multiple discontiguous guest buffers."),
]
story += fig("/home/claude/diagrams/virtiofs_sequence.png",
    "Fig. 1.6 — Behavioural sequence of a guest read through the VirtioFS stack. "
    "Blue = guest-side actors; teal = host-side. The driver forges and queues the "
    "request, signals KVM, which notifies VirtioFSD. VirtioFSD reads from the host "
    "VFS, forges the response, and queues it back.",
    max_w_frac=0.82, max_h_cm=14)

story += sec("1.8  IncludeOS")
story += sub("Overview")
story += [
    p("IncludeOS [9] is a lightweight, bootable operating system implemented in C, "
      "C++, and assembly. Unlike conventional operating systems, IncludeOS follows the "
      "<b>unikernel</b> paradigm: it packages an application together with only the "
      "essential libraries and device drivers required for execution. The result is a "
      "single-address-space image with no process isolation, no user/kernel boundary, "
      "and no general-purpose scheduler. This design enables substantial reductions in "
      "both CPU and memory consumption compared to traditional virtual machines. The "
      "virtual address space is configured with identity mapping to physical memory "
      "for the first 512 GiB."),
]

story += sub("PCI PMIO Interface")
story += [
    p("Driver implementations receive a reference to a generic PCI device abstraction "
      "during construction. This abstraction exposes methods for PCI configuration "
      "space access (<font face='Courier'>read16</font>, "
      "<font face='Courier'>read32</font>), capability discovery "
      "(<font face='Courier'>probe_resources</font>, "
      "<font face='Courier'>parse_capabilities</font>), and MSI-X management "
      "(<font face='Courier'>msix_cap</font>, "
      "<font face='Courier'>init_msix</font>, "
      "<font face='Courier'>get_msix_vectors</font>). The "
      "<font face='Courier'>read16</font> and <font face='Courier'>read32</font> "
      "methods facilitate parsing of PCI capability structures, enabling discovery of "
      "device-specific capabilities such as Virtio extensions. Before utilizing MSI-X "
      "functionality, drivers must invoke "
      "<font face='Courier'>probe_resources()</font> and "
      "<font face='Courier'>parse_capabilities()</font> to enumerate available "
      "resources. Following these preparatory calls, "
      "<font face='Courier'>init_msix()</font> configures MSI-X support, and "
      "<font face='Courier'>get_msix_vectors()</font> returns the number of available "
      "interrupt vectors. MSI-X vector identifiers are valid in the range zero to "
      "vector count exclusive."),
]

story += sub("Event-Driven Interrupt Handling")
story += [
    p("IncludeOS implements interrupt handling through an event-driven architecture "
      "based on callback queues. When a hardware interrupt fires, the system executes "
      "the delegate registered for the corresponding event number. A driver registers "
      "a delegate with "
      "<font face='Courier'>Events::get().subscribe()</font>, receiving an event "
      "number. This event number is then configured as the target for a specific "
      "interrupt vector via "
      "<font face='Courier'>setup_msix_vector()</font>. When the configured interrupt "
      "fires, the registered delegate executes asynchronously. Configuring when a "
      "device triggers a vector is device-specific but must involve writing the vector "
      "to a device register."),
]
story += fig("/home/claude/diagrams/includeos_interrupt.png",
    "Fig. 1.8 — IncludeOS interrupt handling. Setup path (dashed): the driver "
    "subscribes a delegate to get an event number, then binds it to an MSI-X vector. "
    "Runtime path (solid): the device fires the vector, the Events API dispatches "
    "to the registered delegate.",
    max_w_frac=0.90, max_h_cm=7)

story += sub("Filesystem Support and MUSL Integration")
story += [
    p("IncludeOS provides filesystem functionality through two complementary "
      "approaches: a POSIX-compatible interface via the MUSL C standard library [10], "
      "and native IncludeOS filesystem abstractions. The filesystem implementation "
      "includes standard file descriptor abstractions for both generic and "
      "filesystem-specific descriptors. Filesystem paths are represented as tokenized "
      "strings using the forward slash as a separator, with utility functions enabling "
      "hierarchical path manipulation."),
    sp(),
    p("IncludeOS integrates MUSL, a minimal implementation of the C standard library "
      "widely adopted in embedded systems development, distinguished by its low memory "
      "overhead. IncludeOS employs a patched version of MUSL that redirects standard "
      "system calls to external functions, enabling customization of system call "
      "behaviour. This patching mechanism, implemented in "
      "<font face='Courier'>src/musl/*.cpp</font>, allows IncludeOS to intercept and "
      "reimplement standard library system calls to align with the unikernel execution "
      "model — making it possible for applications to use VirtioFS transparently "
      "through standard POSIX file I/O without any application-level awareness of the "
      "underlying Virtio transport."),
]

# ═══════════════════════════════════════════════════════════════════════
#  CHAPTER 2 — DESIGN
# ═══════════════════════════════════════════════════════════════════════
story += chapter(2, "Design")
story += [
    p("The VirtioFS driver is structured as three cooperating layers: a virtual "
      "filesystem (VFS) abstraction layer interfacing with the POSIX system-call layer; "
      "a Virtio PCI transport layer managing device initialization and queue operations; "
      "and a VirtioFS device layer composing the two lower layers into a complete "
      "VirtioFS."),
]

story += sec("2.1  Virtual Filesystem Layer")
story += [
    p("The VFS layer is deliberately thin: it performs path-based dispatch and "
      "file-descriptor bookkeeping, delegating all actual I/O to the registered driver. "
      "Four cooperating components form the layer:"),
    sp(4),
]
story += bl([
    "<font face='Courier'>fs::VFS</font> — singleton mount table mapping string "
    "prefixes to <font face='Courier'>fs::Filesystem</font> structs of function "
    "pointers (<font face='Courier'>open</font>, <font face='Courier'>read</font>, "
    "<font face='Courier'>readv</font>, <font face='Courier'>write</font>, "
    "<font face='Courier'>writev</font>, <font face='Courier'>lseek</font>, "
    "<font face='Courier'>close</font>, <font face='Courier'>unlink</font>).",
    "<font face='Courier'>FD_map</font> — file-descriptor allocator issuing integer "
    "descriptors mapped to polymorphic <font face='Courier'>FD</font> objects.",
    "<font face='Courier'>File_FD</font> — concrete file descriptor forwarding each "
    "method call with the descriptor integer to the owning driver's function pointer.",
    "Syscall stubs — outermost layer performing only path decomposition, returning "
    "standard <font face='Courier'>errno</font> values on failure.",
])
story += [
    sp(4),
    p("A path such as <font face='Courier'>VirtioFS0/data/file.txt</font> is split at "
      "the first separator: the leading component selects the driver; the tail is "
      "forwarded. Writes to descriptors 1 and 2 are intercepted before any "
      "<font face='Courier'>FD_map</font> lookup and routed to "
      "<font face='Courier'>os::print</font>."),
]

story += sec("2.2  Virtio PCI Layer")
story += [
    p("The Virtio PCI layer is divided into two independent components reflecting the "
      "specification's separation of control-plane initialization and data-plane I/O. "
      "Keeping them separate allows the data plane to be developed and optimized "
      "independently of the slow, one-time PCI configuration path."),
]

story += [
    p("<font face='Courier'>Virtio_control</font> encapsulates the full initialization "
      "sequence — device validation, "
      "capability discovery, reset, status-bit sequencing, and feature negotiation — "
      "completing before returning. Any failure triggers "
      "<font face='Courier'>_virtio_panic</font>, setting "
      "<font face='Courier'>VIRTIO_CONFIG_S_FAILED</font> and halting via "
      "<font face='Courier'>os::panic</font>. "
      "<font face='Courier'>VIRTIO_F_VERSION_1</font> is unconditionally "
      "required; optional features are accepted only if the device advertises them."),
]

story += [
    p("<font face='Courier'>Split_queue</font> implements the split virtqueue, exposing direct control over descriptor chain composition for arbitrary "
      "scatter-gather I/O patterns. At construction it validates "
      "<font face='Courier'>queue_size</font>, allocates the three ring structures with "
      "mandated alignments, registers their physical addresses, and computes the "
      "per-queue notification address. A free-descriptor pool provides O(1) allocation "
      "and reclamation with no dynamic memory allocation on the I/O path."),
]

story += sec("2.3  VirtioFS Device")
story += [
    p("The VirtioFS device driver composes one "
      "<font face='Courier'>Virtio_control</font> and two "
      "<font face='Courier'>Split_queue</font> instances into a POSIX filesystem "
      "interface. Queue 0 is the high-priority queue; queue 1 the request queue. Both "
      "are configured in polling mode "
      "(<font face='Courier'>VIRTIO_MSI_NO_VECTOR</font>)."),
]

story += sub("Initialization Sequence")
story += fig("/home/claude/diagrams/virtiofs_init.png",
    "Fig. 2.2 — VirtioFS constructor initialization sequence. Left (top-down): "
    "Virtio setup. Right (bottom-up): FUSE handshake, version checks, "
    "max_write record, filesystem mount.",
    max_w_frac=0.78, max_h_cm=16)

story += [
    p("Initialization proceeds in three sequential phases. First, "
      "<font face='Courier'>Virtio_control</font> completes PCI negotiation, both "
      "queues are registered, and "
      "<font face='Courier'>set_driver_ok_bit</font> signals readiness. Second, the "
      "<font face='Courier'>FUSE_INIT</font> handshake advertises major version 7 and "
      "minor version 36; version numbers are validated and "
      "<font face='Courier'>max_write</font> is stored, reduced by "
      "<font face='Courier'>FUSE_BUFFER_HEADER_SIZE</font>. Third, an "
      "<font face='Courier'>fs::Filesystem</font> struct is registered with "
      "<font face='Courier'>fs::VFS</font> under "
      "<font face='Courier'>VirtioFS{id}</font>."),
]

story += sub("Synchronous Polling Model")
story += [
    p("All filesystem operations are <i>synchronous and blocking</i>: at most one "
      "request is in flight at any time, and the CPU spins on "
      "<font face='Courier'>has_processed_used</font> until completion. "
      "Busy-waiting in this manner eliminates scheduling latency and maximizes "
      "I/O throughput for the single-threaded unikernel execution model, where "
      "yielding the CPU while waiting for I/O would require a scheduler that "
      "IncludeOS does not provide. Request headers "
      "are stack-allocated; caller-supplied buffers are enqueued directly as Virtio "
      "descriptor tokens, delivering data between caller memory and VirtioFSD without "
      "any intermediate copies."),
]

# ═══════════════════════════════════════════════════════════════════════
#  CHAPTER 3 — IMPLEMENTATION
# ═══════════════════════════════════════════════════════════════════════
story += chapter(3, "Implementation")

story += sec("3.1  Virtual Filesystem Layer")
story += [
    p("The VFS layer sits between the MUSL system call stubs and the registered "
      "filesystem driver. It is responsible for exactly two concerns: path-based "
      "mount dispatch during <font face='Courier'>open</font>, and "
      "file-descriptor-based dispatch for all subsequent I/O. These two concerns "
      "are handled by structurally distinct code paths. Four syscall groups emerge "
      "from the implementation, each with a clearly defined pattern."),
]

story += sub("sys_open")
story += [
    p("<font face='Courier'>sys_open</font> is the only syscall that touches the "
      "mount table. The raw pathname is parsed into an "
      "<font face='Courier'>fs::Path</font> object, which tokenizes the string on "
      "the forward slash separator. The leading component — the mount prefix — is "
      "extracted via <font face='Courier'>path.front()</font> and looked up in "
      "<font face='Courier'>fs::VFS::get_mounts()</font>. If no matching mount "
      "exists, <font face='Courier'>-ENOENT</font> is returned immediately."),
    sp(),
    p("If the prefix resolves, the tail path is reconstructed via "
      "<font face='Courier'>path.pop_front()</font> and "
      "<font face='Courier'>path.to_string()</font> with a trailing separator "
      "stripped. A <font face='Courier'>File_FD</font> object is then allocated "
      "from <font face='Courier'>FD_map::_open&lt;File_FD&gt;(fs)</font>, which "
      "binds the file descriptor to the resolved "
      "<font face='Courier'>fs::Filesystem</font> struct at allocation time — "
      "this binding is the key structural decision: all subsequent I/O on this "
      "descriptor will dispatch through the function pointer table captured here, "
      "with no further mount table involvement. The integer descriptor is retrieved "
      "via <font face='Courier'>fde.get_id()</font> and passed — along with the "
      "tail path, flags, and mode — to the driver's "
      "<font face='Courier'>open</font> function pointer."),
    sp(),
    p("On success (result == 0) the integer descriptor is returned to the caller. "
      "On any failure the descriptor must be explicitly released via "
      "<font face='Courier'>FD_map::close(fd)</font> to avoid leaking it. The "
      "catch block distinguishes two failure modes by inspecting whether "
      "<font face='Courier'>fd</font> is still zero: if so, the "
      "<font face='Courier'>FD_map</font> allocation itself failed "
      "(<font face='Courier'>-ENOENT</font>); otherwise the driver's open function "
      "threw (<font face='Courier'>-ENOSYS</font>)."),
]
story += fig("/home/claude/diagrams/vfs_sys_open.png",
    "Fig. 3.1 — sys_open: path parse, prefix lookup, File_FD allocation, and driver call.",
    max_w_frac=0.92, max_h_cm=20)

story += sub("sys_read / sys_readv / sys_write / sys_writev")
story += [
    p("These four syscalls share a common structural pattern. Each follows the "
      "same three-step skeleton: call "
      "<font face='Courier'>FD_map::_get(fd)</font> to retrieve the "
      "<font face='Courier'>File_FD*</font> associated with the integer descriptor; "
      "if non-null, invoke the corresponding virtual method on the "
      "<font face='Courier'>File_FD</font>, which forwards through the "
      "<font face='Courier'>fs::Filesystem</font> function pointer to the driver; "
      "return <font face='Courier'>-EBADF</font> if the pointer is null or "
      "<font face='Courier'>-ENOSYS</font> if the driver throws. The VFS layer "
      "itself contains no I/O logic — all behaviour is entirely delegated."),
    sp(),
    p("<font face='Courier'>sys_write</font> and "
      "<font face='Courier'>sys_writev</font> diverge from this pattern for "
      "file descriptors 1 (stdout) and 2 (stderr). Both check for these reserved "
      "values <i>before</i> any <font face='Courier'>FD_map::_get</font> call and "
      "route output directly to <font face='Courier'>os::print()</font>, bypassing "
      "the VFS entirely. For <font face='Courier'>sys_writev</font>, each "
      "<font face='Courier'>iovec</font> element is printed individually in a loop. "
      "This intercept allows the C standard library output functions to work before "
      "any filesystem driver is registered, and without driver dispatch overhead. "
      "No equivalent intercept exists for "
      "<font face='Courier'>sys_read</font> or "
      "<font face='Courier'>sys_readv</font>, as reading from stdin is not "
      "supported in this configuration."),
]
story += fig("/home/claude/diagrams/vfs_sys_io.png",
    "Fig. 3.2 — sys_read/readv/write/writev: stdout/stderr intercept (write/writev only), "
    "then shared fd dispatch through FD_map, virtual method, and driver function pointer.",
    max_w_frac=0.92, max_h_cm=20)

story += sub("sys_close")
story += [
    p("<font face='Courier'>sys_close</font> follows the same "
      "<font face='Courier'>FD_map::_get</font> lookup as the I/O group, but "
      "diverges in two important ways. First, it checks explicitly for a null "
      "<font face='Courier'>File_FD*</font> and returns "
      "<font face='Courier'>-EBADF</font> rather than relying on the try-catch "
      "path. Second, and more significantly, a non-zero return from the driver's "
      "<font face='Courier'>close</font> method is treated as unrecoverable: "
      "<font face='Courier'>sys_close</font> calls "
      "<font face='Courier'>os::panic()</font> with a diagnostic message rather "
      "than propagating the error upward. The fd is released via "
      "<font face='Courier'>FD_map::close(fd)</font> only after a successful "
      "driver close — ensuring the descriptor is not reissued while the driver "
      "still holds resources associated with it."),
]
story += fig("/home/claude/diagrams/vfs_sys_close.png",
    "Fig. 3.3 — sys_close: explicit null check, driver close with panic on failure, "
    "then descriptor release.",
    max_w_frac=0.92, max_h_cm=16)

story += sub("sys_unlink")
story += [
    p("<font face='Courier'>sys_unlink</font> follows the same prefix-extraction "
      "pattern as <font face='Courier'>sys_open</font> — parse, "
      "<font face='Courier'>front()</font>, "
      "<font face='Courier'>contains()</font>, "
      "<font face='Courier'>pop_front()</font>, "
      "<font face='Courier'>to_string()</font>, strip — but skips fd allocation "
      "entirely and calls the driver's "
      "<font face='Courier'>unlink</font> function pointer directly with the "
      "tail path. It does not use a try-catch with driver dispatch; instead it "
      "uses a <font face='Courier'>submount_exists</font> boolean flag to "
      "distinguish between a missing mount "
      "(<font face='Courier'>-ENOSYS</font>) and a driver-thrown error "
      "(<font face='Courier'>-ENOENT</font>) in the catch block. "
      "<font face='Courier'>sys_unlink</font> is therefore the simplest syscall "
      "in the group: no fd lifecycle, no stdout intercept, just mount resolution "
      "and a direct driver call."),
]
story += fig("/home/claude/diagrams/vfs_sys_unlink.png",
    "Fig. 3.4 — sys_unlink: same prefix lookup as sys_open, direct driver call, no fd lifecycle.",
    max_w_frac=0.92, max_h_cm=16)

story += sec("3.2  Virtio PCI Layer")
story += [
    p("The constructor validates vendor ID "
      "(<font face='Courier'>PCI::VENDOR_VIRTIO</font>) and product ID — 0x1040–0x107F "
      "for modern devices; 0x1000–0x103F legacy devices are rejected. Capability "
      "discovery follows <font face='Courier'>cap_next</font> links checking for "
      "<font face='Courier'>PCI_CAP_ID_VNDR</font>; both 32-bit and 64-bit BARs are "
      "handled. Three regions are recorded: "
      "<font face='Courier'>virtio_pci_common_cfg</font>, device-specific "
      "configuration, and the notification region with its "
      "<font face='Courier'>notify_off_multiplier</font>."),
    sp(),
    p("The driver resets the device, sets "
      "<font face='Courier'>ACKNOWLEDGE</font> and <font face='Courier'>DRIVER</font>, "
      "reads the 64-bit feature word in two 32-bit halves, unconditionally requires "
      "<font face='Courier'>VIRTIO_F_VERSION_1</font>, optionally accepts "
      "<font face='Courier'>VIRTIO_F_INDIRECT_DESC</font> and "
      "<font face='Courier'>VIRTIO_F_EVENT_IDX</font>, writes back the negotiated set, "
      "sets <font face='Courier'>FEATURES_OK</font>, and re-reads "
      "<font face='Courier'>device_status</font> to confirm acceptance."),
]

story += [
    p("Despite being the data-plane component, "
      "<font face='Courier'>Split_queue</font> performs a significant amount of "
      "control-plane register work in its constructor — this is an important nuance. "
      "On construction it writes to "
      "<font face='Courier'>queue_select</font> to target the correct per-queue "
      "register set in <font face='Courier'>virtio_pci_common_cfg</font>, reads back "
      "<font face='Courier'>queue_size</font>, computes and stores the notification "
      "address from <font face='Courier'>queue_notify_off</font> and "
      "<font face='Courier'>notify_off_multiplier</font>, assigns "
      "<font face='Courier'>queue_msix_vector</font> and suppresses config interrupts "
      "by writing <font face='Courier'>VIRTIO_MSI_NO_VECTOR</font> to "
      "<font face='Courier'>config_msix_vector</font>, writes the physical addresses "
      "of the descriptor table, available ring, and used ring to "
      "<font face='Courier'>queue_desc</font>, "
      "<font face='Courier'>queue_driver</font>, and "
      "<font face='Courier'>queue_device</font> respectively, and finally sets "
      "<font face='Courier'>queue_enable = 1</font> to activate the queue. "
      "After construction, no further "
      "<font face='Courier'>virtio_pci_common_cfg</font> accesses occur — all "
      "subsequent I/O proceeds through pre-computed pointers to the three ring "
      "structures and the notification register."),
    sp(),
    p("The three ring structures are allocated with the alignment requirements "
      "mandated by the specification: 16 bytes for the descriptor table, 2 bytes "
      "for the available ring, and 4 bytes for the used ring. The per-queue "
      "notification address is computed as:"),
]
story += eq("notify_addr  =  notify_region_base  +  queue_notify_off  ×  notify_off_multiplier")
story += [
    p("The free-descriptor pool is a <font face='Courier'>std::vector</font> of "
      "indices pre-allocated with "
      "<font face='Courier'>reserve(_QUEUE_SIZE)</font> and initialized to "
      "[0, queue_size), providing O(1) allocation (pop from back) and reclamation "
      "(push to back) with no dynamic memory allocation on the I/O path. The "
      "number of currently available descriptors can be queried via "
      "<font face='Courier'>free_desc_space()</font>, and the total queue capacity "
      "via <font face='Courier'>desc_space_cap()</font>."),
    sp(),
    p("<b>Enqueue</b> accepts a <font face='Courier'>VirtTokens</font> vector. Each "
      "<font face='Courier'>VirtToken</font> pairs a "
      "<font face='Courier'>VirtBuffer</font> — a "
      "<font face='Courier'>std::span&lt;uint8_t&gt;</font> over a guest-physical "
      "buffer — with a 16-bit flags word. One descriptor is allocated per token; "
      "all but the last have <font face='Courier'>VIRTQ_DESC_F_NEXT</font> ORed "
      "into their flags and their <font face='Courier'>next</font> field filled with "
      "the following descriptor's index, forming a chain. The head index is placed "
      "into the available ring at position "
      "<font face='Courier'>_avail_ring->idx &amp; (queue_size - 1)</font>. A "
      "<font face='Courier'>memory_order_release</font> fence is then issued before "
      "incrementing <font face='Courier'>_avail_ring->idx</font>, guaranteeing all "
      "descriptor writes are globally visible before the device observes the updated "
      "index. A subsequent <font face='Courier'>memory_order_seq_cst</font> fence "
      "precedes the check of "
      "<font face='Courier'>_used_ring->flags</font> for notification suppression "
      "(<font face='Courier'>VIRTQ_USED_F_NOTIFY</font>); if the device has not "
      "suppressed kicks, <font face='Courier'>_notify_device()</font> writes the "
      "queue index as a 16-bit value to the pre-computed notification register "
      "address."),
    sp(),
    p("<b>Dequeue</b> reads one <font face='Courier'>virtq_used_elem</font> at "
      "position <font face='Courier'>_last_used_idx &amp; (queue_size - 1)</font>, "
      "optionally returning the <font face='Courier'>len</font> field to the caller "
      "via an output pointer to indicate how many bytes the device wrote into "
      "writable buffers. It then walks the descriptor chain from "
      "<font face='Courier'>used_elem.id</font>, reconstructing one "
      "<font face='Courier'>VirtToken</font> per descriptor and returning each "
      "index to the free pool, until a descriptor without "
      "<font face='Courier'>VIRTQ_DESC_F_NEXT</font> is reached. "
      "<font face='Courier'>_last_used_idx</font> is incremented before returning "
      "the token vector. Whether a completed entry is available can be checked "
      "in advance with "
      "<font face='Courier'>has_processed_used()</font>, which returns true when "
      "<font face='Courier'>_last_used_idx == _used_ring->idx</font> — the volatile "
      "qualifier on <font face='Courier'>_used_ring->idx</font> ensures the "
      "comparison always reads the device-updated value from memory."),
    sp(),
    p("Notification suppression is controlled by two inline methods. "
      "<font face='Courier'>suppress()</font> writes "
      "<font face='Courier'>VIRTQ_AVAIL_F_NO_INTERRUPT</font> into the available "
      "ring's <font face='Courier'>flags</font> field, requesting that the device "
      "refrain from sending completion interrupts — used when the driver intends to "
      "poll <font face='Courier'>has_processed_used()</font> directly. "
      "<font face='Courier'>unsuppress()</font> clears this by writing "
      "<font face='Courier'>VIRTQ_AVAIL_F_INTERRUPT</font>, re-enabling interrupt "
      "delivery. These methods allow the upper-layer driver to switch between "
      "polling and interrupt-driven modes at runtime without reconfiguring MSI-X "
      "vector assignments."),
]

story += sec("3.3  VirtioFS Device Driver")
story += sub("Initialisation")
story += [
    p("All members are constructed via member-initializer syntax. "
      "<font face='Courier'>Virtio_control</font>'s constructor completes PCI "
      "negotiation before returning; "
      "<font face='Courier'>set_driver_ok_bit</font> is called immediately. The "
      "<font face='Courier'>FUSE_INIT</font> request is submitted as a two-token "
      "chain (readable request | writable response buffer); the driver spins on "
      "<font face='Courier'>has_processed_used</font>. The daemon's major version must "
      "match exactly; its minor must meet or exceed the driver's minimum. "
      "<font face='Courier'>max_write</font> is stored reduced by "
      "<font face='Courier'>FUSE_BUFFER_HEADER_SIZE</font> (4096 bytes). Finally an "
      "<font face='Courier'>fs::Filesystem</font> struct is registered under "
      "<font face='Courier'>VirtioFS{id}</font>."),
]

story += sub("Inode Resolution")
story += [
    p("<font face='Courier'>_lookup_inode</font> sends a three-token "
      "<font face='Courier'>FUSE_LOOKUP</font> chain: request header (readable) | "
      "null-terminated path (readable) | response buffer (writable). The returned "
      "inode number, file handle, and seek offset are stored in "
      "<font face='Courier'>_fd_info_map</font> keyed by the POSIX descriptor integer, "
      "eliminating repeated lookups for an open file."),
]

story += sub("Open, Create, and Close")
story += [
    p("<font face='Courier'>_open_exist</font> calls "
      "<font face='Courier'>_lookup_inode</font> then issues "
      "<font face='Courier'>FUSE_OPEN</font>, storing the file handle with initial "
      "seek offset zero. <font face='Courier'>_open_creat</font> issues "
      "<font face='Courier'>FUSE_CREATE</font> against the root inode, combining "
      "lookup and open in one round-trip. <font face='Courier'>close</font> sends "
      "<font face='Courier'>FUSE_RELEASE</font> on the request queue, removes the "
      "descriptor from <font face='Courier'>_fd_info_map</font>, then sends "
      "<font face='Courier'>FUSE_FORGET</font> on the high-priority queue to promptly "
      "decrement the daemon's inode reference count."),
]

story += sub("Read and Write")
story += [
    p("All read and write operations deliver caller buffers directly to VirtioFSD "
      "via Virtio descriptor chains with no intermediate copy. "
      "Figures 3.2 and 3.3 show the descriptor layouts."),
]
story += fig("/home/claude/diagrams/read_chain.png",
    "Fig. 3.2 — FUSE read chain: request header (readable) | response header "
    "(writable) | caller buffer (writable). Bytes read = "
    "fuse_out_header.len − sizeof(fuse_out_header).",
    max_w_frac=0.92, max_h_cm=6)
story += fig("/home/claude/diagrams/write_chain.png",
    "Fig. 3.3 — FUSE write chain: request header (readable) | caller buffer "
    "(readable, capped at _max_write) | fuse_write_out (writable).",
    max_w_frac=0.92, max_h_cm=6)

story += [
    p("The scatter-gather variants <font face='Courier'>readv</font> and "
      "<font face='Courier'>writev</font> append one "
      "<font face='Courier'>VirtToken</font> per "
      "<font face='Courier'>iovec</font> element, exploiting descriptor chaining to "
      "fill or drain discontiguous caller buffers with no aggregation buffer."),
]

story += sub("Seek, Unlink, and Registration")
story += [
    p("<font face='Courier'>lseek</font> updates "
      "<font face='Courier'>_fd_info_map</font>'s offset for "
      "<font face='Courier'>SEEK_SET</font> and "
      "<font face='Courier'>SEEK_CUR</font> without issuing any Virtio operations — "
      "all offset state is authoritative in the driver. "
      "<font face='Courier'>unlink</font> issues "
      "<font face='Courier'>FUSE_UNLINK</font> with the path pointer offset by one "
      "byte to strip the leading separator added by the VFS layer."),
    sp(),
    p("Driver registration is performed by a file-scope constructor annotated with "
      "<font face='Courier'>__attribute__((constructor))</font>, calling "
      "<font face='Courier'>hw::PCI_manager::register_vfs</font> with vendor ID "
      "<font face='Courier'>VENDOR_VIRTIO</font> and product ID 0x105a, supplying "
      "<font face='Courier'>VirtioFS_device::new_instance</font> as the factory. "
      "At boot, the PCI manager invokes this factory for any matching device, "
      "triggering the full three-phase initialization. This requires no modification "
      "to the existing PCI enumeration code."),
]

# ═══════════════════════════════════════════════════════════════════════
#  BIBLIOGRAPHY
# ═══════════════════════════════════════════════════════════════════════
story += [
    PageBreak(), Spacer(1, 0.6*cm),
    Paragraph("Bibliography", h1),
    HRFlowable(width="100%", thickness=1.8, color=BLUE, spaceAfter=20),
]
refs = [
    "[1]  G. J. Popek and R. P. Goldberg, 'Formal requirements for virtualizable third "
    "generation architectures,' Commun. ACM, vol. 17, no. 7, pp. 412–421, Jul. 1974.",
    "[2]  F. Bellard, 'QEMU, a fast and portable dynamic translator,' in Proc. USENIX "
    "ATC, Anaheim, CA, 2005. https://www.qemu.org",
    "[3]  A. Kivity et al., 'KVM: the Linux virtual machine monitor,' in Proc. Linux "
    "Symposium, Ottawa, vol. 1, 2007, pp. 225–230.",
    "[4]  KVM project, 'ioeventfd,' Linux kernel docs, 2024. "
    "https://www.kernel.org/doc/html/latest/virt/kvm/api.html",
    "[5]  QEMU project, 'Vhost-user protocol specification,' 2024. "
    "https://qemu-project.gitlab.io/qemu/interop/vhost-user.html",
    "[6]  OASIS, Virtual I/O Device (VIRTIO) Version 1.3, OASIS Standard, 2024. "
    "https://docs.oasis-open.org/virtio/virtio/v1.3/virtio-v1.3.html",
    "[7]  M. Szeredi, 'FUSE: Filesystem in Userspace,' Linux kernel docs, 2024. "
    "https://www.kernel.org/doc/html/next/filesystems/fuse.html",
    "[8]  V. Goyal et al., 'Virtio-fs: A shared file system for virtual machines,' "
    "in Proc. USENIX ATC, 2020. https://virtio-fs.gitlab.io",
    "[9]  A. Bratterud et al., 'IncludeOS: A minimal, resource efficient unikernel "
    "for cloud services,' in Proc. IEEE CloudCom, Vancouver, 2015, pp. 250–257.",
    "[10] R. Fellows et al., 'musl libc,' 2024. https://musl.libc.org",
]
for r in refs:
    story.append(Paragraph(r, bib))
    story.append(sp(4))

def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 9.5)
    canvas.setFillColor(LGRAY)
    canvas.drawCentredString(W/2, 1.6*cm, str(doc.page))
    canvas.restoreState()

doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print(f"Built — {doc.page} pages")
