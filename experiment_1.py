'''
Implementation and experimentation for Part 1, Experiment 1
'''
from graph import *
import matplotlib.pyplot as plt

def run_experiment(num_nodes):
    num_edges = []
    for i in range(0, num_nodes * 3 // 2, num_nodes // 20):
        num_edges.append(i)
    m = 100 # number of graphs for each number of edges

    cycle_probabilities = []

    for num_edge in num_edges:
        with_cycle = 0
        for _ in range(m):
            G = create_random_graph(num_nodes, num_edge)
            if has_cycle(G):
                with_cycle += 1
        cycle_proportion = with_cycle / m
        cycle_probabilities.append(cycle_proportion)
    
    return num_edges, cycle_probabilities
            
# Fix the number of nodes to 100, 300, and 500 on separate runs of this code
num_nodes = 500
num_edges, cycle_probabilities = run_experiment(num_nodes)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(num_edges, cycle_probabilities)
plt.xlabel('Number of Edges')
plt.ylabel('Probability graph contains a cycle')
plt.title('Cycle probability vs. number of edges (n = ' + str(num_nodes) + ')')
plt.grid(True)
plt.show()