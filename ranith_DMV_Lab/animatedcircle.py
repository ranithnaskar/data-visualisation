import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig, ax = plt.subplots()

# Set equal aspect ratio and limits
ax.set_aspect('equal')
ax.set_xlim(-2, 3)
ax.set_ylim(-2, 1)

# Create a point (circle)
point, = ax.plot([], [], 'ro', markersize=8)

# Radius of the circle
r = 1

# Initialization function
def init():
    point.set_data([], [])
    return point,

# Update function
def update(frame):
    x = r * np.cos(frame)
    y = r * np.sin(frame)
    point.set_data(x, y)
    return point,

# Create animation
ani = FuncAnimation(
    fig,
    update,
    frames=np.linspace(0, 2*np.pi, 100),
    init_func=init,
    interval=50,
    blit=True
)

plt.show()