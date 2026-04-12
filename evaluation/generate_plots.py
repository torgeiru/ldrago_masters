#!/usr/bin/env python3
"""
Reconstruct all plots for IncludeOS VirtioFS Evaluation PDF.
Generates Figures 1-8 matching the original master's thesis PDF.
"""

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import stats
from pathlib import Path

# ── paths ──────────────────────────────────────────────────────────────────
BASE = Path("/sessions/festive-quirky-thompson/mnt/virtiofs_benchmarks")
PLOTS = BASE / "plots"
PLOTS.mkdir(exist_ok=True)

# ── colour / style constants ────────────────────────────────────────────────
C_LINUX   = "#1f77b4"   # blue
C_IOURING = "#9467bd"   # purple
C_POLL    = "#d62728"   # red
C_IRQ     = "#2ca02c"   # green

MARKER_LINUX   = "o"
MARKER_IOURING = "D"
MARKER_POLL    = "s"
MARKER_IRQ     = "^"

plt.rcParams.update({
    "font.family": "serif",
    "axes.titlesize": 10,
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "figure.dpi": 150,
})

PATTERNS = [
    ("seq_read",  "Sequential Read"),
    ("seq_write", "Sequential Write"),
    ("rng_read",  "Random Read"),
    ("rng_write", "Random Write"),
]

# ── helpers ─────────────────────────────────────────────────────────────────

def load_posix(folder: Path, pattern: str) -> pd.DataFrame:
    """Load a POSIX/io_uring CSV; return df with chunk_size_kib column."""
    df = pd.read_csv(folder / f"{pattern}_bench.csv")
    df["chunk_size_kib"] = df["chunk_size"] / 1024
    return df


def ci95(series):
    """Return (mean, half-width of 95 % CI) for a pandas Series."""
    n = len(series)
    m = series.mean()
    se = series.std(ddof=1) / np.sqrt(n)
    hw = stats.t.ppf(0.975, df=n - 1) * se
    return m, hw


def summarise(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate to per-chunk-size mean ± 95 % CI of throughput_mibps."""
    rows = []
    for cs, grp in df.groupby("chunk_size_kib"):
        m, hw = ci95(grp["throughput_mibps"])
        rows.append({"chunk_size_kib": cs, "mean": m, "hw": hw})
    return pd.DataFrame(rows).sort_values("chunk_size_kib")


def plot_band(ax, summ, color, label, marker, linestyle="-", alpha=0.15):
    x = summ["chunk_size_kib"]
    y = summ["mean"]
    hw = summ["hw"]
    ax.plot(x, y, color=color, label=label, marker=marker,
            markersize=4, linewidth=1.5, linestyle=linestyle)
    ax.fill_between(x, y - hw, y + hw, color=color, alpha=alpha)


def finish_ax(ax, title, xlabel="Chunk size (KiB)", ylabel="Throughput (MiB/s)"):
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, alpha=0.3, linewidth=0.5)
    ax.set_xlim(left=0)


# ── Fig 1 – RQ1 combined ────────────────────────────────────────────────────

def fig_rq1_combined():
    print("Generating rq1_combined …")
    fig, axes = plt.subplots(2, 2, figsize=(9, 6.5))
    fig.suptitle("RQ1 - VirtioFS I/O Throughput: Linux POSIX vs IncludeOS",
                 fontsize=11, fontweight="bold", y=1.01)

    for (key, title), ax in zip(PATTERNS, axes.flat):
        df_linux = summarise(load_posix(BASE / "linux_posix_results", key))
        df_poll  = summarise(load_posix(BASE / "includeos_posix_results", key))
        df_irq   = summarise(load_posix(BASE / "includeos_posix_irq_results", key))

        plot_band(ax, df_linux, C_LINUX,   "Linux POSIX",         MARKER_LINUX)
        plot_band(ax, df_poll,  C_POLL,    "IncludeOS Polling",   MARKER_POLL)
        plot_band(ax, df_irq,   C_IRQ,     "IncludeOS IRQ (MSI-X)", MARKER_IRQ)
        finish_ax(ax, title)

    # shared legend below
    handles = [
        mpatches.Patch(color=C_LINUX,   label="Linux POSIX"),
        mpatches.Patch(color=C_POLL,    label="IncludeOS Polling"),
        mpatches.Patch(color=C_IRQ,     label="IncludeOS IRQ (MSI-X)"),
    ]
    fig.legend(handles=handles, loc="lower center", ncol=3,
               bbox_to_anchor=(0.5, -0.03), frameon=True)

    fig.tight_layout()
    fig.savefig(PLOTS / "rq1_combined.pdf", bbox_inches="tight")
    plt.close(fig)


# ── Fig 2 – RQ1 peak bar ────────────────────────────────────────────────────

def fig_rq1_peak_bar():
    print("Generating rq1_peak_bar …")

    configs = {
        "Linux POSIX":         BASE / "linux_posix_results",
        "IncludeOS Polling":   BASE / "includeos_posix_results",
        "IncludeOS IRQ (MSI-X)": BASE / "includeos_posix_irq_results",
    }
    colors = [C_LINUX, C_POLL, C_IRQ]

    seq_patterns = [("seq_read", "Seq Read"), ("seq_write", "Seq Write")]
    rnd_patterns = [("rng_read", "Rnd Read"), ("rng_write", "Rnd Write")]

    fig, (ax_seq, ax_rnd) = plt.subplots(1, 2, figsize=(9, 4))
    fig.suptitle("RQ1 - Peak Throughput Comparison", fontsize=11,
                 fontweight="bold")

    def plot_group(ax, patterns, subtitle):
        n_cfg   = len(configs)
        n_pat   = len(patterns)
        width   = 0.2
        x       = np.arange(n_pat)

        for i, (cfg_name, folder) in enumerate(configs.items()):
            peaks = []
            for key, _ in patterns:
                df = load_posix(folder, key)
                peaks.append(df.groupby("chunk_size_kib")["throughput_mibps"]
                              .mean().max())
            offset = (i - (n_cfg - 1) / 2) * width
            ax.bar(x + offset, peaks, width=width * 0.9,
                   color=colors[i], label=cfg_name)

        ax.set_title(subtitle)
        ax.set_xticks(x)
        ax.set_xticklabels([p[1] for p in patterns])
        ax.set_ylabel("Peak Throughput (MiB/s)")
        ax.set_ylim(bottom=0)
        ax.grid(True, axis="y", alpha=0.3)

    plot_group(ax_seq, seq_patterns, "Sequential – Peak")
    plot_group(ax_rnd, rnd_patterns, "Random – Peak")

    handles = [mpatches.Patch(color=c, label=n)
               for n, c in zip(configs.keys(), colors)]
    fig.legend(handles=handles, loc="lower center", ncol=3,
               bbox_to_anchor=(0.5, -0.06), frameon=True)

    fig.tight_layout()
    fig.savefig(PLOTS / "rq1_peak_bar.pdf", bbox_inches="tight")
    plt.close(fig)


# ── Fig 3 – RQ2 combined ────────────────────────────────────────────────────

def fig_rq2_combined():
    print("Generating rq2_combined …")
    fig, axes = plt.subplots(2, 2, figsize=(9, 6.5))
    fig.suptitle("RQ2 - Linux POSIX vs io_uring SQPOLL",
                 fontsize=11, fontweight="bold", y=1.01)

    for (key, title), ax in zip(PATTERNS, axes.flat):
        df_posix   = summarise(load_posix(BASE / "linux_posix_results",   key))
        df_iouring = summarise(load_posix(BASE / "linux_iouring_results",  key))

        plot_band(ax, df_posix,   C_LINUX,   "Linux POSIX",          MARKER_LINUX)
        plot_band(ax, df_iouring, C_IOURING, "Linux io_uring (SQPOLL)",
                  MARKER_IOURING, linestyle="--")
        finish_ax(ax, title)

    handles = [
        mpatches.Patch(color=C_LINUX,   label="Linux POSIX"),
        mpatches.Patch(color=C_IOURING, label="Linux io\_uring (SQPOLL)"),
    ]
    fig.legend(handles=handles, loc="lower center", ncol=2,
               bbox_to_anchor=(0.5, -0.03), frameon=True)

    fig.tight_layout()
    fig.savefig(PLOTS / "rq2_combined.pdf", bbox_inches="tight")
    plt.close(fig)


# ── Fig 4 – RQ2 speedup ─────────────────────────────────────────────────────

def fig_rq2_speedup():
    print("Generating rq2_speedup …")
    fig, axes = plt.subplots(2, 2, figsize=(9, 6))
    fig.suptitle("RQ2 - io_uring SQPOLL Speedup over Linux POSIX",
                 fontsize=11, fontweight="bold", y=1.01)

    for (key, title), ax in zip(PATTERNS, axes.flat):
        df_posix   = summarise(load_posix(BASE / "linux_posix_results",   key))
        df_iouring = summarise(load_posix(BASE / "linux_iouring_results",  key))

        merged = pd.merge(df_posix[["chunk_size_kib", "mean"]],
                          df_iouring[["chunk_size_kib", "mean"]],
                          on="chunk_size_kib", suffixes=("_p", "_io"))
        speedup = merged["mean_io"] / merged["mean_p"]

        ax.plot(merged["chunk_size_kib"], speedup, color=C_IOURING,
                marker=MARKER_IOURING, markersize=4, linewidth=1.5)
        ax.axhline(1.0, color="grey", linestyle="--", linewidth=1,
                   label="Parity (×1.0)")
        ax.set_title(title)
        ax.set_xlabel("Chunk size (KiB)")
        ax.set_ylabel("Speedup (io_uring / POSIX)")
        ax.grid(True, alpha=0.3, linewidth=0.5)
        ax.set_xlim(left=0)
        ax.legend(fontsize=7)

    fig.tight_layout()
    fig.savefig(PLOTS / "rq2_speedup.pdf", bbox_inches="tight")
    plt.close(fig)


# ── Fig 5 – all systems combined ────────────────────────────────────────────

def fig_all_systems():
    print("Generating all_systems_combined …")
    fig, axes = plt.subplots(2, 2, figsize=(9, 6.5))
    fig.suptitle("All Systems – VirtioFS I/O Throughput Overview",
                 fontsize=11, fontweight="bold", y=1.01)

    for (key, title), ax in zip(PATTERNS, axes.flat):
        df_linux   = summarise(load_posix(BASE / "linux_posix_results",        key))
        df_iouring = summarise(load_posix(BASE / "linux_iouring_results",       key))
        df_poll    = summarise(load_posix(BASE / "includeos_posix_results",     key))
        df_irq     = summarise(load_posix(BASE / "includeos_posix_irq_results", key))

        plot_band(ax, df_linux,   C_LINUX,   "Linux POSIX",           MARKER_LINUX)
        plot_band(ax, df_iouring, C_IOURING, "Linux io_uring (SQPOLL)",
                  MARKER_IOURING, linestyle="--")
        plot_band(ax, df_poll,    C_POLL,    "IncludeOS Polling",     MARKER_POLL)
        plot_band(ax, df_irq,     C_IRQ,     "IncludeOS IRQ (MSI-X)", MARKER_IRQ)
        finish_ax(ax, title)

    handles = [
        mpatches.Patch(color=C_LINUX,   label="Linux POSIX"),
        mpatches.Patch(color=C_IOURING, label="Linux io\_uring (SQPOLL)"),
        mpatches.Patch(color=C_POLL,    label="IncludeOS Polling"),
        mpatches.Patch(color=C_IRQ,     label="IncludeOS IRQ (MSI-X)"),
    ]
    fig.legend(handles=handles, loc="lower center", ncol=4,
               bbox_to_anchor=(0.5, -0.03), frameon=True)

    fig.tight_layout()
    fig.savefig(PLOTS / "all_systems_combined.pdf", bbox_inches="tight")
    plt.close(fig)


# ── Figs 6–8 – RQ3 c63dec ───────────────────────────────────────────────────

def load_c63(folder: Path) -> pd.Series:
    df = pd.read_csv(folder / "c63dec_bench.csv")
    # time in seconds
    df["time_s"] = df["time_ms"] / 1000.0
    return df


def fig_rq3_boxplot():
    print("Generating rq3_c63dec_boxplot …")
    df_linux = load_c63(BASE / "linux_c63dec_results")
    df_poll  = load_c63(BASE / "includeos_c63dec_results")
    df_irq   = load_c63(BASE / "includeos_c63dec_irq_results")

    # all 30 runs (0-29)
    data = [df_linux["time_s"].values,
            df_poll["time_s"].values,
            df_irq["time_s"].values]
    labels = ["Linux POSIX", "IncludeOS Polling", "IncludeOS IRQ (MSI-X)"]
    colors = [C_LINUX, C_POLL, C_IRQ]

    fig, ax = plt.subplots(figsize=(6, 4.5))
    bp = ax.boxplot(data, labels=labels, patch_artist=True,
                    flierprops=dict(marker="o", markersize=5, linestyle="none"))

    for patch, color in zip(bp["boxes"], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    for median in bp["medians"]:
        median.set_color("black")
        median.set_linewidth(1.5)

    ax.set_title("RQ3 – c63 Video Decode Time (WWE stream, runs 1–29)",
                 fontsize=10, fontweight="bold")
    ax.set_ylabel("Decode time (s)")
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    fig.savefig(PLOTS / "rq3_c63dec_boxplot.pdf", bbox_inches="tight")
    plt.close(fig)


def fig_rq3_bar():
    print("Generating rq3_c63dec_bar …")
    df_linux = load_c63(BASE / "linux_c63dec_results")
    df_poll  = load_c63(BASE / "includeos_c63dec_results")
    df_irq   = load_c63(BASE / "includeos_c63dec_irq_results")

    configs = [
        ("Linux POSIX",          df_linux["time_s"], C_LINUX),
        ("IncludeOS Polling",    df_poll["time_s"],  C_POLL),
        ("IncludeOS IRQ (MSI-X)", df_irq["time_s"], C_IRQ),
    ]

    means, cis, colors, names = [], [], [], []
    for name, s, c in configs:
        m, hw = ci95(s)
        means.append(m)
        cis.append(hw)
        colors.append(c)
        names.append(name)

    linux_mean = means[0]

    fig, ax = plt.subplots(figsize=(5.5, 4.5))
    x = np.arange(len(names))
    bars = ax.bar(x, means, yerr=cis, capsize=4,
                  color=colors, alpha=0.85,
                  error_kw=dict(elinewidth=1.2, ecolor="black"))

    # speedup labels above IncludeOS bars
    for i in [1, 2]:
        speedup = linux_mean / means[i]
        ax.text(x[i], means[i] + cis[i] + 0.05,
                f"×{speedup:.2f}", ha="center", va="bottom",
                color=colors[i], fontsize=9, fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(names, fontsize=8)
    ax.set_ylabel("Mean decode time (s)")
    ax.set_title("RQ3 – Mean c63 Decode Time ± 95% CI",
                 fontsize=10, fontweight="bold")
    ax.set_ylim(bottom=0)
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    fig.savefig(PLOTS / "rq3_c63dec_bar.pdf", bbox_inches="tight")
    plt.close(fig)


def fig_rq3_timeseries():
    print("Generating rq3_c63dec_timeseries …")
    df_linux = load_c63(BASE / "linux_c63dec_results")
    df_poll  = load_c63(BASE / "includeos_c63dec_results")
    df_irq   = load_c63(BASE / "includeos_c63dec_irq_results")

    fig, ax = plt.subplots(figsize=(7.5, 4.5))

    for df, color, marker, label in [
        (df_linux, C_LINUX,   MARKER_LINUX,   "Linux POSIX"),
        (df_poll,  C_POLL,    MARKER_POLL,    "IncludeOS Polling"),
        (df_irq,   C_IRQ,     MARKER_IRQ,     "IncludeOS IRQ (MSI-X)"),
    ]:
        ax.plot(df["run_number"], df["time_s"], color=color,
                marker=marker, markersize=5, linewidth=1.5, label=label)

    ax.set_xlabel("Run number (0 = cold start)")
    ax.set_ylabel("Decode time (s)")
    ax.set_title("RQ3 – c63 Decode Time per Run (including cold start)",
                 fontsize=10, fontweight="bold")
    ax.legend(loc="upper right")
    ax.grid(True, alpha=0.3)
    ax.set_xlim(left=-0.5)
    fig.tight_layout()
    fig.savefig(PLOTS / "rq3_c63dec_timeseries.pdf", bbox_inches="tight")
    plt.close(fig)


# ── run everything ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    fig_rq1_combined()
    fig_rq1_peak_bar()
    fig_rq2_combined()
    fig_rq2_speedup()
    fig_all_systems()
    fig_rq3_boxplot()
    fig_rq3_bar()
    fig_rq3_timeseries()
    print("\nAll plots saved to", PLOTS)
