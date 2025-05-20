import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (2, 3)])
nx.draw_random(G)
plt.show()