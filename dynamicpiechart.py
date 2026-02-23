import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random


fig, ax = plt.subplots()
ax.set_title("Dynamic Pie Chart")

labels = ["A", "B", "C", "D"]

def update(frame):
    ax.clear()
    

    data = [random.randint(1, 10) for _ in range(4)]
    
    ax.pie(data, labels=labels, autopct='%1.1f%%',
           startangle=90)
    ax.set_title("Dynamic Pie Chart")


ani = FuncAnimation(fig, update, interval=1000)

plt.show()