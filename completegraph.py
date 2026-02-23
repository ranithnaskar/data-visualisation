# complete_graph_vscode.py

import matplotlib
matplotlib.use('TkAgg')  # Ensures the plot window works in VS Code with Anaconda
import matplotlib.pyplot as plt
import networkx as nx

# Number of nodes in the complete graph
n = 5

# Create a complete graph
G = nx.complete_graph(n)

# Draw the graph
plt.figure(figsize=(6, 6))
nx.draw(
    G,
    with_labels=True,
    node_color='skyblue',
    node_size=800,
    font_size=16,
    font_weight='bold',
    edge_color='gray'
)

# Show the plot
plt.show()
