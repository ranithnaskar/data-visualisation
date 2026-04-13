import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig, ax = plt.subplots()

# Initial data
data = np.random.randn(100)

# Plot initial histogram
bars = ax.hist(data, bins=20, edgecolor='black')

# Set axis limits
ax.set_xlim(-5, 5)
ax.set_ylim(0, 30)

# Update function
def update(frame):
    ax.cla()  # Clear previous histogram
    new_data = np.random.randn(100)
    ax.hist(new_data, bins=20, edgecolor='black')
    ax.set_xlim(-5, 5)
    ax.set_ylim(0, 30)
    ax.set_title("Dynamic Histogram")

# Create animation
ani = FuncAnimation(
    fig,
    update,
    frames=50,
    interval=300
)

plt.show()