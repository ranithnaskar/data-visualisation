import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 4, 9, 16, 25]

# Create subplots (2 rows, 1 column)
plt.subplot(2, 1, 1)
plt.plot(x, y1)
plt.title("Line Graph")

plt.subplot(2, 1, 2)
plt.plot(x, y2)
plt.title("Square Values")

plt.show()
