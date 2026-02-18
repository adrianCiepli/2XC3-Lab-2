'''
Part 2: MIS vs MVC Relationship Experiment
'''
from graph import *
import matplotlib.pyplot as plt

print("MIS vs MVC Relationship\n")

num_nodes = 8
edge_values = list(range(0, 29, 4))
m = 200

mis_avg_sizes = []
mvc_avg_sizes = []
sum_checks = []

for num_edges in edge_values:
    mis_total = 0
    mvc_total = 0
    all_sum_to_n = True
    for _ in range(m):
        G = create_random_graph(num_nodes, num_edges)
        mvc = MVC(G)
        mis = MIS(G)
        mis_total += len(mis)
        mvc_total += len(mvc)
        if len(mis) + len(mvc) != num_nodes:
            all_sum_to_n = False
    mis_avg_sizes.append(mis_total / m)
    mvc_avg_sizes.append(mvc_total / m)
    sum_checks.append(all_sum_to_n)
    print(f"Edges={num_edges:3d} | Avg MVC={mvc_total/m:.2f} | Avg MIS={mis_total/m:.2f} | Sum={mvc_total/m + mis_total/m:.2f} | MIS+MVC=n? {all_sum_to_n}")

print(f"\nlen(MIS) + len(MVC) = {num_nodes} holds for ALL tested graphs: {all(sum_checks)}")

plt.figure(figsize=(10, 6))
plt.plot(edge_values, mvc_avg_sizes, marker='o', label='Avg MVC size')
plt.plot(edge_values, mis_avg_sizes, marker='s', label='Avg MIS size')
plt.axhline(y=num_nodes, color='r', linestyle='--', label=f'n = {num_nodes}')
plt.xlabel('Number of Edges')
plt.ylabel('Average Set Size')
plt.title(f'MVC and MIS Sizes vs Number of Edges (n = {num_nodes})')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('experiment_4a.png')
plt.show()

print("\nDirect Inspection\n")
for num_edges in [5, 10, 15, 20]:
    G = create_random_graph(num_nodes, num_edges)
    mvc = set(MVC(G))
    mis = set(MIS(G))
    all_nodes = set(range(num_nodes))
    complement_of_mvc = all_nodes - mvc

    print(f"Edges={num_edges}")
    print(f"  MVC = {sorted(mvc)}")
    print(f"  MIS = {sorted(mis)}")
    print(f"  V \\ MVC = {sorted(complement_of_mvc)}")
    print(f"  V \\ MVC is independent set? {is_independent_set(G, list(complement_of_mvc))}")
    print(f"  len(MIS) == len(V \\ MVC)? {len(mis) == len(complement_of_mvc)}")
    print()

print("Conclusion: The complement of a minimum vertex cover is always a maximum independent set.")
print("The exact nodes may differ (multiple optimal solutions can exist), but the SIZES always satisfy:")
print("  len(MIS) + len(MVC) = n")
print("This is because every edge must have at least one endpoint in the vertex cover,")
print("so no two nodes outside the cover can share an edge — making them independent.")
