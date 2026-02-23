import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 10, 1)
y = np.random.randint(1, 10, size=len(x))


plt.step(x, y, where='mid', color='blue', linewidth=2)

plt.title("Stair (Step) Plot Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.grid(True)
plt.show()