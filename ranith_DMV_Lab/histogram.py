import matplotlib.pyplot as plt

data = [12, 15, 14, 10, 18, 20, 22, 19, 17, 16, 14, 13, 11, 21, 23]

plt.hist(data, bins=5, edgecolor='black')

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')

plt.show()

