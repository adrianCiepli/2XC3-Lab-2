from collections import deque
import random

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes():
        return len()

#Sample Graph where only node=8 is unreachable (was NOT included in original graph.py) - uncomment to use it using CTRL ?
# test_graph = Graph(9)
# test_graph.add_edge(0,1)
# test_graph.add_edge(0,2)
# test_graph.add_edge(1,2)
# test_graph.add_edge(1,3)
# test_graph.add_edge(2,3)
# test_graph.add_edge(2,4)
# test_graph.add_edge(3,5)
# test_graph.add_edge(3,6)
# test_graph.add_edge(4,7)
# test_graph.add_edge(6,7)

#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False

#BFS that returns path from node1 to node2
def BFS2(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    pred = {node1: None}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                # build the result path from predecessor array, use current_node in reverse now
                pred[node] = current_node
                current_node = node
                path = [node2]
                while pred[current_node] != None:
                    path.append(pred[current_node])
                    current_node = pred[current_node]
                return path[::-1]
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                pred[node] = current_node
    
    # if we got here then node2 was not found
    return []

#BFS that returns predecessor dictionary to all nodes from node1
def BFS3(G, node1):
    Q = deque([node1])
    marked = {node1 : True}
    pred = {}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                pred[node] = current_node
    
    return pred

#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False

#DFS that returns path from node1 to node2
def DFS2(G, node1, node2):
    S = [node1]
    marked = {}
    pred = {node1: None}
    for node in G.adj:
        marked[node] = False
    marked[node1] = True
    while len(S) != 0:
        current_node = S.pop()
        for node in G.adj[current_node]:
            if not marked[node]:
                # change pred of node only the first time you see it
                pred[node] = current_node
                S.append(node)
                marked[node] = True
            if node == node2:
                # build the result path from predecessor array, use current_node in reverse now
                current_node = node2
                path = [node2]
                while pred[current_node] != None:
                    path.append(pred[current_node])
                    current_node = pred[current_node]
                return path[::-1]
                
    return []

#DFS that returns predecessor dictionary to all nodes from node1
def DFS3(G, node1):
    S = [node1]
    marked = {}
    pred = {}
    for node in G.adj:
        marked[node] = False
    marked[node1] = True
    while len(S) != 0:
        current_node = S.pop()
        for node in G.adj[current_node]:
            if not marked[node]:
                # change pred of node only the first time you see it
                pred[node] = current_node
                S.append(node)
                marked[node] = True       
    return pred

def has_cycle(G):
    Q = deque([])
    marked = {}
    pred = {}
    for node in G.adj:
        marked[node] = False
    
    # Ensures we search through all nodes even if components are disconnected from each other
    for node in G.adj:
        if not marked[node]:
            Q.append(node)
            pred[node] = None
            marked[node] = True
            while len(Q) != 0:
                current_node = Q.popleft()
                for node in G.adj[current_node]:
                    if not marked[node]:
                        Q.append(node)
                        marked[node] = True
                        pred[node] = current_node
                    elif node != pred[current_node]:
                        return True
    
    return False

# Uses a BFS with a count to see if every node is reachable from start
def is_connected(G):
    if len(G.adj) == 0:
        return True
    count = 1
    node1 = 0
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                count += 1
    return count == len(G.adj)

# NOTE: we do not have self-loop edges in this graph as a design choice
# Returns a graph with i nodes and j edges, and should NOT create a graph with "multiples" of the same edge
def create_random_graph(i, j):
    G = Graph(i)
    edges_added = 0
    # Maximum possible edges with no self-loop edge: i*(i-1)
    # each undirected edge gets counted twice for both directions so int-divide by 2 for unique edges only
    max_edges = (i * (i - 1)) // 2
    
    # If you want more edges than possible, then we just make the maximum
    if j > max_edges:
        j = max_edges
    
    while edges_added < j:
        node1 = random.randint(0, i - 1)
        node2 = random.randint(0, i - 1)
        
        # Avoid self-loops and duplicate edges
        if node1 != node2 and not G.are_connected(node1, node2):
            G.add_edge(node1, node2)
            edges_added += 1
    
    return G

#Use the methods below to determine minimum vertex covers

def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy

def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True

def MVC(G):
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover


