"""Generate the quaternion axis-angle schematic for notebook 2."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

INK, MUTED, AXIS, ANGLE = '#1a1a1a', '#9a9a9a', '#1f5fa8', '#b03a2e'

fig, ax = plt.subplots(figsize=(6.4, 6.4))
ax.set_xlim(-2.0, 2.4); ax.set_ylim(-2.3, 2.6); ax.set_aspect('equal'); ax.axis('off')


def arrow(p, q, color, lw, style='-|>', ms=16):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=ms,
                                 color=color, lw=lw, shrinkA=0, shrinkB=0))


origin = np.array([-0.6, -0.4])
for d, name in (((1.6, -0.55), 'x'), ((1.25, 0.55), 'y'), ((0, 1.7), 'z')):
    tip = origin + d
    arrow(origin, tip, MUTED, 1.0, ms=10)
    ax.text(*(tip + 0.12 * np.array(d) / np.linalg.norm(d)), name, color=MUTED,
            fontsize=13, style='italic', ha='center', va='center')

u = np.array([np.cos(np.deg2rad(58)), np.sin(np.deg2rad(58))])
start, end = origin - 0.35 * u, origin + 2.75 * u
ax.plot(*zip(start, origin + 2.4 * u), color=AXIS, lw=2.6, solid_capstyle='round')
arrow(origin + 2.3 * u, end, AXIS, 2.6, ms=20)
ax.text(*(end + [0.12, 0.05]), r'axis $\mathbf{u}$', color=AXIS, fontsize=14, va='bottom')

centre = origin + 1.55 * u
n = np.array([-u[1], u[0]])
t = np.deg2rad(np.linspace(200, 480, 120))
ring = centre[:, None] + 0.78 * n[:, None] * np.cos(t) + 0.22 * u[:, None] * np.sin(t)
front = np.sin(t) < 0
ax.plot(*np.where(front, ring, np.nan), color=ANGLE, lw=2.4, zorder=3)
ax.plot(*np.where(~front, ring, np.nan), color=ANGLE, lw=2.4, zorder=1, alpha=0.9)
arrow(ring[:, -6], ring[:, -1], ANGLE, 2.4, ms=18)
ax.text(*(centre - 1.02 * n + [0.05, 0.12]), r'$\psi$', color=ANGLE, fontsize=20,
        ha='center', va='center')

y0 = -1.55
parts = [('q = (', INK), ('x, y, z', AXIS), (',', INK), ('w', ANGLE), (')', INK)]
gap = {'q = (': 0.06, 'x, y, z': 0.07, ',': 0.35, 'w': 0.06}
x = -1.3
renderer = fig.canvas.get_renderer()
spans = {}
for text, color in parts:
    h = ax.text(x, y0, text, color=color, fontsize=20, va='center', ha='left',
                family='DejaVu Sans', style='normal')
    bb = h.get_window_extent(renderer).transformed(ax.transData.inverted())
    spans[text] = (bb.x0, bb.x1)
    x = bb.x1 + gap.get(text, 0)

for key, label, color in (('x, y, z', 'point along\nthe axis', AXIS),
                          ('w', 'how far\nto turn', ANGLE)):
    a, b = spans[key]
    yb = y0 - 0.3
    ax.plot([a, a, b, b], [yb + 0.08, yb, yb, yb + 0.08], color=color, lw=1.4)
    ax.text((a + b) / 2, yb - 0.12, label, color=color, fontsize=11.5,
            ha='center', va='top')

fig.savefig('assets/_images/quaternion_axis_angle.png', dpi=110,
            bbox_inches='tight', facecolor='white')
print('written')
