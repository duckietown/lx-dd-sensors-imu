"""Generate the mass-spring-damper accelerometer schematic for notebook 1."""

import matplotlib as mpl

mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrow, Rectangle

INK, MUTED, ACCENT, FILL = "#1a1a1a", "#767676", "#b03a2e", "#dde5ec"
CASE_L, CASE_R, CASE_T, CASE_B = -0.75, 0.75, 2.00, 0.15
SPRING_X, DAMPER_X = -0.34, 0.34


def spring(ax, x, y_top, y_bot, coils=6, w=0.10, lw=1.3):
    lead = 0.14 * abs(y_top - y_bot)
    ys = np.linspace(y_top - lead, y_bot + lead, 2 * coils + 1)
    xs = [x] + [x + (w if i % 2 else -w) for i in range(len(ys) - 2)] + [x]
    ax.plot([x, x], [y_top, ys[0]], color=INK, lw=lw)
    ax.plot(xs, ys, color=INK, lw=lw)
    ax.plot([x, x], [ys[-1], y_bot], color=INK, lw=lw)


def damper(ax, x, y_top, y_bot, lw=1.3):
    span = y_top - y_bot
    cyl_t, cyl_b = y_top - 0.15 * span, y_top - 0.62 * span
    ax.plot([x, x], [y_top, cyl_t], color=INK, lw=lw)
    # Open-bottomed cylinder: three sides only, which is what makes it a dashpot.
    ax.plot(
        [x - 0.14, x - 0.14, x + 0.14, x + 0.14],
        [cyl_b, cyl_t, cyl_t, cyl_b],
        color=INK,
        lw=lw,
    )
    piston = cyl_b + 0.45 * (cyl_t - cyl_b)
    ax.plot([x - 0.125, x + 0.125], [piston, piston], color=INK, lw=lw + 1.4)
    ax.plot([x, x], [piston, y_bot], color=INK, lw=lw)


def panel(ax, title, stretch, reading, on_table):
    ax.set_xlim(-1.75, 1.75)
    ax.set_ylim(-0.75, 2.45)
    ax.axis("off")
    ax.set_title(title, fontsize=11.5, color=INK, pad=10)

    ax.add_patch(
        Rectangle(
            (CASE_L, CASE_B),
            CASE_R - CASE_L,
            CASE_T - CASE_B,
            fill=False,
            ec=INK,
            lw=2.2,
            joinstyle="miter",
        )
    )

    mass_top = CASE_T - stretch
    ax.add_patch(
        Rectangle(
            (-0.45, mass_top - 0.36),
            0.90,
            0.36,
            facecolor=FILL,
            ec=INK,
            lw=1.6,
        )
    )
    ax.text(
        0,
        mass_top - 0.18,
        "mass",
        ha="center",
        va="center",
        fontsize=10.5,
        color=INK,
    )

    spring(ax, SPRING_X, CASE_T, mass_top)
    damper(ax, DAMPER_X, CASE_T, mass_top)

    if on_table:
        ax.plot([-1.30, 1.30], [CASE_B, CASE_B], color=INK, lw=1.8)
        for xh in np.linspace(-1.24, 1.16, 15):
            ax.plot(
                [xh, xh + 0.12], [CASE_B, CASE_B - 0.18], color=MUTED, lw=1.0
            )
    else:
        ax.add_patch(
            FancyArrow(
                1.16,
                1.55,
                0,
                -0.80,
                width=0.010,
                head_width=0.11,
                head_length=0.15,
                color=MUTED,
                length_includes_head=True,
            )
        )
        ax.text(
            1.26,
            1.15,
            "falls\nfreely",
            fontsize=9,
            color=MUTED,
            ha="left",
            va="center",
        )

    ax.text(
        0, -0.52, reading, ha="center", va="center", fontsize=12, color=ACCENT
    )


fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.8))
panel(
    axes[0],
    "At rest on a table",
    0.80,
    r"ideal reading  $\tilde{f}_z = f_z = +9.81$  m/s$^2$",
    on_table=True,
)
panel(
    axes[1],
    "In free fall",
    0.36,
    r"ideal reading  $\tilde{f}_z = f_z = 0$",
    on_table=False,
)

# Labels, left panel only, all anchored outside the case so no leader crosses it.
lab = {
    "fontsize": 9,
    "color": MUTED,
    "va": "center",
    "arrowprops": {
        "arrowstyle": "-",
        "color": MUTED,
        "lw": 0.9,
        "shrinkA": 2,
        "shrinkB": 2,
    },
}
ax = axes[0]
ax.annotate(
    "box, fixed to\nthe Duckiedrone",
    xy=(CASE_L, 1.80),
    xytext=(-1.72, 2.10),
    ha="left",
    **lab,
)
ax.annotate(
    "spring",
    xy=(SPRING_X - 0.10, 1.55),
    xytext=(-1.72, 1.42),
    ha="left",
    **lab,
)
ax.annotate(
    "damper", xy=(DAMPER_X + 0.14, 1.62), xytext=(0.92, 1.72), ha="left", **lab
)


# The sensor's positive z direction is the same in both panels.
def add_z_axis(ax, x):
    ax.add_patch(
        FancyArrow(
            x,
            0.15,
            0,
            0.62,
            width=0.010,
            head_width=0.10,
            head_length=0.13,
            color=INK,
            length_includes_head=True,
        )
    )
    ax.text(x + 0.06, 0.50, r"$z$", fontsize=12, color=INK, ha="left")


add_z_axis(axes[0], -1.52)
add_z_axis(axes[1], -1.62)
axes[1].add_patch(
    FancyArrow(
        -1.20,
        0.95,
        0,
        -0.62,
        width=0.010,
        head_width=0.10,
        head_length=0.13,
        color=MUTED,
        length_includes_head=True,
    )
)
axes[1].text(-1.14, 0.62, r"$g$", fontsize=12, color=INK, ha="left")

fig.tight_layout()
fig.savefig(
    "assets/_images/mass_spring_damper.png",
    dpi=110,
    bbox_inches="tight",
    facecolor="white",
)
print("written")
