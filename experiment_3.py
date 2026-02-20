'''
Part 2: Approximation Experiments
'''
from graph import *
import matplotlib.pyplot as plt

def run_approx_experiment(num_nodes, edge_values, m):
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

    return approx1_ratios, approx2_ratios, approx3_ratios

num_nodes = 8
edge_values = list(range(1, 29, 3))
m = 1000

print(f"Running Experiment A: {num_nodes} nodes, {m} graphs per edge count...")
a1_ratios, a2_ratios, a3_ratios = run_approx_experiment(num_nodes, edge_values, m)

plt.figure(figsize=(10, 6))
plt.plot(edge_values, a1_ratios, marker='o', label='approx1 (greedy highest degree)')
plt.plot(edge_values, a2_ratios, marker='s', label='approx2 (random vertex)')
plt.plot(edge_values, a3_ratios, marker='^', label='approx3 (random edge)')
plt.axhline(y=1, color='r', linestyle='--', label='Optimal (MVC)')
plt.xlabel('Number of Edges')
plt.ylabel('Approximation Ratio (approx size / MVC size)')
plt.title(f'Approximation Performance vs Number of Edges (n = {num_nodes}, m = {m})')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('experiment_3a.png')
plt.show()

# Experiment B: All 3 approximations on a graph with 6 nodes
num_nodes_b = 6
max_edges_b = (num_nodes_b * (num_nodes_b - 1)) // 2
edge_values_b = list(range(1, max_edges_b + 1, max(1, max_edges_b // 10)))
m_b = 500

print(f"Running Experiment B: {num_nodes_b} nodes, {m_b} graphs per edge count...")
a1_ratios_b, a2_ratios_b, a3_ratios_b = run_approx_experiment(num_nodes_b, edge_values_b, m_b)

plt.figure(figsize=(10, 6))
plt.plot(edge_values_b, a1_ratios_b, marker='o', label='approx1 (greedy highest degree)')
plt.plot(edge_values_b, a2_ratios_b, marker='s', label='approx2 (random vertex)')
plt.plot(edge_values_b, a3_ratios_b, marker='^', label='approx3 (random edge)')
plt.axhline(y=1, color='r', linestyle='--', label='Optimal (MVC)')
plt.xlabel('Number of Edges')
plt.ylabel('Approximation Ratio (approx size / MVC size)')
plt.title(f'Approximation Performance vs Number of Edges (n = {num_nodes_b}, m = {m_b})')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('experiment_3b.png')
plt.show()

# Experiment C: All 3 approximations on a graph with 10 nodes
num_nodes_c = 10
max_edges_c = (num_nodes_c * (num_nodes_c - 1)) // 2
edge_values_c = list(range(1, max_edges_c + 1, max(1, max_edges_c // 10)))
m_c = 500

print(f"Running Experiment C: {num_nodes_c} nodes, {m_c} graphs per edge count...")
a1_ratios_c, a2_ratios_c, a3_ratios_c = run_approx_experiment(num_nodes_c, edge_values_c, m_c)

plt.figure(figsize=(10, 6))
plt.plot(edge_values_c, a1_ratios_c, marker='o', label='approx1 (greedy highest degree)')
plt.plot(edge_values_c, a2_ratios_c, marker='s', label='approx2 (random vertex)')
plt.plot(edge_values_c, a3_ratios_c, marker='^', label='approx3 (random edge)')
plt.axhline(y=1, color='r', linestyle='--', label='Optimal (MVC)')
plt.xlabel('Number of Edges')
plt.ylabel('Approximation Ratio (approx size / MVC size)')
plt.title(f'Approximation Performance vs Number of Edges (n = {num_nodes_c}, m = {m_c})')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('experiment_3c.png')
plt.show()

print("Experiment 3 complete. Graphs saved as experiment_3a.png, experiment_3b.png, experiment_3c.png")
