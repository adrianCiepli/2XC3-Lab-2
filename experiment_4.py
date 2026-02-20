'''
Part 2: MIS vs MVC Relationship Experiment
'''
from graph import *
import matplotlib.pyplot as plt

def run_experiment(num_nodes):
    edge_values = list(range(0, (num_nodes * (num_nodes - 1)) // 2 + 1, 4))
    m = 200

    mis_avg_sizes = []
    mvc_avg_sizes = []

    for num_edges in edge_values:
        mis_total = 0
        mvc_total = 0
        for _ in range(m):
            G = create_random_graph(num_nodes, num_edges)
            mis_total += len(MIS(G))
            mvc_total += len(MVC(G))
        mis_avg_sizes.append(mis_total / m)
        mvc_avg_sizes.append(mvc_total / m)

    return edge_values, mvc_avg_sizes, mis_avg_sizes

num_nodes = 8
edge_values, mvc_avg_sizes, mis_avg_sizes = run_experiment(num_nodes)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(edge_values, mvc_avg_sizes, marker='o', label='Avg MVC size')
plt.plot(edge_values, mis_avg_sizes, marker='s', label='Avg MIS size')
plt.axhline(y=num_nodes, color='r', linestyle='--', label='n = ' + str(num_nodes))
plt.xlabel('Number of Edges')
plt.ylabel('Average Set Size')
plt.title('MVC and MIS Sizes vs Number of Edges (n = ' + str(num_nodes) + ')')
plt.legend()
plt.grid(True)
plt.show()
