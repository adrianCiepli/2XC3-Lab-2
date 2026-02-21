'''
Part 2: Approximation Experiments
'''
from graph import *
import matplotlib.pyplot as plt

def run_experiment(num_nodes, m):
    edge_values = [1, 5, 10, 15, 20, 25, 30]
    
    approx1_ratios = []
    approx2_ratios = []
    approx3_ratios = []

    for num_edges in edge_values:
        mvc_sum = 0
        a1_sum = 0
        a2_sum = 0
        a3_sum = 0
        for _ in range(m):
            G = create_random_graph(num_nodes, num_edges)
            mvc_size = len(MVC(G))
            mvc_sum += mvc_size
            a1_sum += len(approx1(G))
            a2_sum += len(approx2(G))
            a3_sum += len(approx3(G))

        if mvc_sum == 0:
            approx1_ratios.append(1)
            approx2_ratios.append(1)
            approx3_ratios.append(1)
        else:
            approx1_ratios.append(a1_sum / mvc_sum)
            approx2_ratios.append(a2_sum / mvc_sum)
            approx3_ratios.append(a3_sum / mvc_sum)

    return edge_values, approx1_ratios, approx2_ratios, approx3_ratios

# Graph 1: Approximation performance vs number of edges (n = 8)
edge_values, a1_ratios, a2_ratios, a3_ratios = run_experiment(8, 1000)

plt.figure(figsize=(10, 6))
plt.plot(edge_values, a1_ratios, marker='o', label='approx1 (greedy highest degree)')
plt.plot(edge_values, a2_ratios, marker='s', label='approx2 (random vertex)')
plt.plot(edge_values, a3_ratios, marker='^', label='approx3 (random edge)')
plt.axhline(y=1, color='r', linestyle='--', label='Optimal (MVC)')
plt.xlabel('Number of Edges')
plt.ylabel('Approximation Ratio (approx size / MVC size)')
plt.title('Approximation Performance vs Number of Edges (n = 8)')
plt.legend()
plt.grid(True)
plt.show()

# Graph 2: Effect of number of nodes on approximation performance (fixed edges = 10)
node_values = [5, 6, 7, 8, 9, 10]
fixed_edges = 10

a1_by_nodes = []
a2_by_nodes = []
a3_by_nodes = []

for n in node_values:
    mvc_sum = a1_sum = a2_sum = a3_sum = 0
    for _ in range(500):
        G = create_random_graph(n, fixed_edges)
        mvc_size = len(MVC(G))
        mvc_sum += mvc_size
        a1_sum += len(approx1(G))
        a2_sum += len(approx2(G))
        a3_sum += len(approx3(G))
    ratio = mvc_sum if mvc_sum > 0 else 1
    a1_by_nodes.append(a1_sum / ratio)
    a2_by_nodes.append(a2_sum / ratio)
    a3_by_nodes.append(a3_sum / ratio)

plt.figure(figsize=(10, 6))
plt.plot(node_values, a1_by_nodes, marker='o', label='approx1 (greedy highest degree)')
plt.plot(node_values, a2_by_nodes, marker='s', label='approx2 (random vertex)')
plt.plot(node_values, a3_by_nodes, marker='^', label='approx3 (random edge)')
plt.axhline(y=1, color='r', linestyle='--', label='Optimal (MVC)')
plt.xlabel('Number of Nodes')
plt.ylabel('Approximation Ratio (approx size / MVC size)')
plt.title('Approximation Performance vs Number of Nodes (fixed edges = 10)')
plt.legend()
plt.grid(True)
plt.show()

# Graph 3: Worst-case approximation ratio vs number of edges (n = 8)
# Uses random sampling (1000 graphs per edge count) to estimate worst-case
edge_values = [1, 5, 10, 15, 20, 25, 30]

a1_worst = []
a2_worst = []
a3_worst = []

for num_edges in edge_values:
    a1_max = a2_max = a3_max = 1.0
    for _ in range(1000):
        G = create_random_graph(8, num_edges)
        mvc_size = len(MVC(G))
        if mvc_size > 0:
            a1_max = max(a1_max, len(approx1(G)) / mvc_size)
            a2_max = max(a2_max, len(approx2(G)) / mvc_size)
            a3_max = max(a3_max, len(approx3(G)) / mvc_size)
    a1_worst.append(a1_max)
    a2_worst.append(a2_max)
    a3_worst.append(a3_max)

plt.figure(figsize=(10, 6))
plt.plot(edge_values, a1_worst, marker='o', label='approx1 (greedy highest degree)')
plt.plot(edge_values, a2_worst, marker='s', label='approx2 (random vertex)')
plt.plot(edge_values, a3_worst, marker='^', label='approx3 (random edge)')
plt.axhline(y=1, color='r', linestyle='--', label='Optimal (MVC)')
plt.xlabel('Number of Edges')
plt.ylabel('Worst-Case Approximation Ratio')
plt.title('Worst-Case Approximation Ratio vs Number of Edges (n = 8)')
plt.legend()
plt.grid(True)
plt.show()
