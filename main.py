import subprocess
import parsers
import matplotlib.pyplot as plt
import networkx as nx

# ping, ipconfig, pathping, route


# Команда, которую вы хотите выполнить
command = "pathping ulstu.ru"

# Выполнение команды
result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='cp866')

ips = parsers.parse_pathping(result)
edges = []
for i in range(len(ips) - 1):
    edges.append((ips[i], ips[i + 1]))

G = nx.Graph()
G.add_nodes_from(ips)
G.add_edges_from(edges)

pos = nx.kamada_kawai_layout(G)

options = {
    'node_color': 'yellow',
    'node_size': 8500,
    'width': 1,
    'arrowstyle': '-|>',
    'arrowsize': 30,
}

nx.draw(G, pos, with_labels=True, arrows=True, **options)

ax = plt.gca()
ax.collections[0].set_edgecolor("#000000")

plt.show()
