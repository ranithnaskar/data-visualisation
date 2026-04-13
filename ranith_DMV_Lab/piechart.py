import matplotlib.pyplot as plt

# Data for pie chart
labels = ['Python', 'Java', 'C++', 'Others']
sizes = [45, 25, 20, 10]

# Create pie chart
plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90
)

# Equal aspect ratio makes pie circular
plt.axis('equal')

# Title
plt.title('Programming Language Usage')

plt.show()