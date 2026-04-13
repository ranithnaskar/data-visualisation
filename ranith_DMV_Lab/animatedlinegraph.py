import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig, ax = plt.subplots()

# Set axis limits
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)

# Initialize empty line
line, = ax.plot([], [], lw=2)

# Data lists
x_data = []
y_data = []

# Initialization function
def init():
    line.set_data([], [])
    return line,

# Animation function (called repeatedly)
def update(frame):
    x_data.append(frame)
    y_data.append(np.sin(frame))
    line.set_data(x_data, y_data)
    return line,

# Create animation
ani = FuncAnimation(
    fig,
    update,
    frames=np.linspace(0, 10, 100),
    init_func=init,
    blit=True,
    interval=100
)

plt.show()