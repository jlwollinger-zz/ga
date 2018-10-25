"""
Demo of a PathPatch object.
"""
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt


fig, ax = plt.subplots()

Path = mpath.Path
path_data = [
    (Path.MOVETO, (1.58, 1)),
    (Path.CURVE4, (0.35, 2)),
    (Path.CURVE4, (-1.75, 3)),
    (Path.CURVE4, (0.375, 4)),
   # (Path.LINETO, (0.85, 5)),
    (Path.CURVE4, (2.2, 6)),
    (Path.CURVE4, (3, 7)),
    (Path.CURVE4, (2.0, 8)),
    (Path.CLOSEPOLY, (1.58, 1)),
    ]
codes, verts = zip(*path_data)
path = mpath.Path(verts, codes)
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
ax.add_patch(patch)

# plot control points and connecting lines
x, y = zip(*path.vertices)
line, = ax.plot(x, y, 'go-')

ax.grid()
ax.axis('equal')
plt.show()