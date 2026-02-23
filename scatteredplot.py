import matplotlib.pyplot as plt
import numpy as np


x = np.random.rand(50) * 100
y = np.random.rand(50) * 100
colors = np.random.rand(50)
sizes = np.random.rand(50) * 500


plt.scatter(x, y, c=colors, s=sizes, alpha=0.7, cmap='viridis')

plt.title("Scatter Plot Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.colorbar(label="Color Intensity")

plt.show()