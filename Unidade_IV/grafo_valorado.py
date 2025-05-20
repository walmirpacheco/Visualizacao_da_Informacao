import matplotlib.pyplot as plt
import networkx as nx


G = nx.read_gml('Unidade_III/graph.gml')
pos = nx.shell_layout(G)

nx.draw_networkx_nodes(G, pos,
                       node_color = '#00C0C0',
                       node_size = 500,
                       alpha = 0.8)

nx.draw_networkx_edges(G, pos, width = 1.0, alpha = 0.5)

labels = nx.draw_networkx_labels(G, pos, font_size = 10)
edge_lagels = nx.draw_networkx_edge_labels(G, pos, font_size = 10)

plt.axis('off')
plt.show()