import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Create figure
fig, ax = plt.subplots()

# Labels
labels = ['Python', 'Java', 'C++', 'Others']

# Initial data
sizes = [40, 30, 20, 10]

# Update function
def update(frame):
    ax.clear()
    
    # Generate changing data
    new_sizes = np.random.randint(10, 50, size=4)
    
    ax.pie(
        new_sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90
    )
    
    ax.set_title("Dynamic Pie Chart")

# Create animation
ani = FuncAnimation(
    fig,
    update,
    frames=20,
    interval=1000
)

plt.show()