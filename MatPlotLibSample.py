import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt


fig, ax = plt.subplots()

Path = mpath.Path
path_data = [
    (Path.MOVETO, (1.58, -2.57)),
    (Path.MOVETO, (0.35, -1.1)),
    (Path.MOVETO, (-1.75, 2.0)),
    (Path.MOVETO, (0.375, 2.0)),
    (Path.MOVETO, (0.85, 1.15)),
    (Path.MOVETO, (2.2, 3.2)),
    (Path.MOVETO, (3, 0.05)),
    (Path.MOVETO, (2.0, -0.5)),
    (Path.MOVETO, (1.58, -2.57)),
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