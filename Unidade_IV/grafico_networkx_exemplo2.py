import networkx as nx
import matplotlib.pyplot as plt


G = nx.complete_bipartite_graph(3, 3)
pos = nx.shell_layout(G)

nx.draw_networkx_nodes(G, pos,
                       nodelist = [0, 1, 2],
                       node_color = '#FF9000',
                       node_size = 500,
                       alpha=0.8)
nx.draw_networkx_nodes(G, pos,
                       nodelist = [3, 4, 5],
                       node_color = '#00C0F0',
                       node_size = 500,
                       alpha = 0.8)

nx.draw_networkx_edges(G, pos, width = 1.0, alpha = 0.5)

labels = {}
labels[0] = r'$A$'
labels[1] = r'$L$'
labels[2] = r'$E$'
labels[3] = r'$C1$'
labels[4] = r'$C2$'
labels[5] = r'$C3$'
nx.draw_networkx_labels(G, pos, labels, font_size = 16)
plt.axis('off')
plt.show()