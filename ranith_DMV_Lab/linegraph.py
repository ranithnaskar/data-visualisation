import matplotlib.pyplot as plt

x = list(map(float, input("Enter X values (space-separated): ").split()))
y = list(map(float, input("Enter Y values (space-separated): ").split()))

if len(x) != len(y):
    print("Error: X and Y must have the same number of values.")
else:
    
    plt.plot(x, y, marker='o')
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Line Graph from User Input")
    plt.grid(True)
    plt.show()
