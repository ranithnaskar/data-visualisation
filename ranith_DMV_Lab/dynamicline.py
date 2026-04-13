import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig, ax = plt.subplots()

# Set axis limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 100)

# Initialize empty line
line, = ax.plot([], [], lw=2)

# Data lists
x_data = []
y_data = []

# Initialization function
def init():
    line.set_data([], [])
    return line,

# Update function
def update(frame):
    x_data.append(frame)
    y_data.append(frame * frame)
    line.set_data(x_data, y_data)
    return line,

# Create animation
ani = FuncAnimation(
    fig,
    update,
    frames=np.linspace(0, 10, 50),
    init_func=init,
    interval=200,
    blit=True
)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Dynamic Line Graph")
plt.show()