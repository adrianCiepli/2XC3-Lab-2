'''
Implementation and experimentation for Part 1, Experiment 2
'''
from graph import *
import matplotlib.pyplot as plt

def run_experiment(num_nodes):
    num_edges = []
    for i in range(0, num_nodes * 8, num_nodes // 20):
        num_edges.append(i)
    m = 100 # number of graphs for each number of edges

    connected_probabilities = []

    for num_edge in num_edges:
        num_connected = 0
        for _ in range(m):
            G = create_random_graph(num_nodes, num_edge)
            if is_connected(G):
                num_connected += 1
        connected_proportion = num_connected / m
        connected_probabilities.append(connected_proportion)
    
    return num_edges, connected_probabilities
            
# Fix the number of nodes to 100, 200, and 300 on separate runs of this code
num_nodes = 100
num_edges, connected_probabilities = run_experiment(num_nodes)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(num_edges, connected_probabilities)
plt.xlabel('Number of Edges')
plt.ylabel('Probability graph is connected')
plt.title('Connectedness probability vs. number of edges (n = ' + str(num_nodes) + ')')
plt.grid(True)
plt.show()