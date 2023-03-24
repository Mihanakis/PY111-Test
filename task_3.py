import networkx as nx
import matplotlib.pyplot as plt
from random import randint


graph = nx.Graph()
massive = "0123456789"
graph.add_nodes_from(massive)
for n in range(10):
    graph.add_edges_from([(str(randint(0, 9)), str(randint(0, 9)))])

lst, count = [], 0
for node in massive:
    tree = sorted(list(nx.dfs_tree(graph, source=node)))
    if tree not in lst:
        lst.append(tree)
        count += 1

print(count)
nx.draw(graph)
plt.show()
