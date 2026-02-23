import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots()
ax.set_title("Dynamic Line Graph")
ax.set_xlabel("Time")
ax.set_ylabel("Value")

x_data = []
y_data = []

line, = ax.plot([], [], color="blue", linewidth=2)

ax.set_xlim(0, 50)
ax.set_ylim(-2, 2)

def update(frame):
    x_data.append(frame)
    y_data.append(np.sin(frame * 0.1))  
    
    line.set_data(x_data, y_data)
    
  
    if frame > 50:
        ax.set_xlim(frame - 50, frame)
    
    return line,


ani = FuncAnimation(fig, update, frames=np.arange(0, 200),
                    interval=100, blit=True)

plt.show()