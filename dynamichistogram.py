import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots()
ax.set_title("Dynamic Histogram")
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")


data = np.random.randn(100)


bars = ax.hist(data, bins=20, color='skyblue', edgecolor='black')[2]

def update(frame):
    ax.clear()
    new_data = np.random.randn(100)
    ax.hist(new_data, bins=20, color='skyblue', edgecolor='black')
    ax.set_title("Dynamic Histogram")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")


ani = FuncAnimation(fig, update, interval=500)

plt.show()