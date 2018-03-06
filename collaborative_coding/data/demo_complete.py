import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
ax.add_patch(
    patches.Rectangle(
        (0.1, 0.1),
        0.8,
        0.8,
        fill=False,      # remove background
        edgecolor = '#1E684A',
    )
)

#ax = fig.add_subplot(111, aspect='equal')
ax.add_patch(
    patches.Rectangle(
        (0.15, 0.15),   # (x,y)
        0.2,          # width
        0.2,          # height
        facecolor="#328D62",
    )
)

ax.add_patch(
    patches.Rectangle(
        (0.15, 0.4),   # (x,y)
        0.2,          # width
        0.2,          # height
        facecolor="#7FB79A",
    )
)

ax.add_patch(
    patches.Rectangle(
        (0.15, 0.65),   # (x,y)
        0.2,          # width
        0.2,          # height
        facecolor="#CCE1D8",
    )
)

ax.add_patch(
    patches.Rectangle(
        (0.4, 0.15),   # (x,y)
        0.2,          # width
        0.2,          # height
        facecolor="#197F50",
    )
)

ax.add_patch(
    patches.Rectangle(
        (0.4, 0.4),   # (x,y)
        0.2,          # width
        0.2,          # height
        facecolor="#66A98A",
    )
)

ax.add_patch(
    patches.Rectangle(
        (0.4, 0.65),   # (x,y)
        0.2,          # width
        0.2,          # height
        facecolor="#B2D4C4",
    )
)

ax.add_patch(
    patches.Rectangle(
        (0.65, 0.15),   # (x,y)
        0.2,          # width
        0.2,          # height
        facecolor="#00713D",
    )
)

ax.add_patch(
    patches.Rectangle(
        (0.65, 0.4),   # (x,y)
        0.2,          # width
        0.2,          # height
        facecolor="#4E9B79",
    )
)

ax.add_patch(
    patches.Rectangle(
        (0.65, 0.65),   # (x,y)
        0.2,          # width
        0.2,          # height
        facecolor="#99C6B1",
    )
)

plt.show()
