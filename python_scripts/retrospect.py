import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
graph = {}

graph_node = {}
vis = []
node_id = 0

print('Start loading 100 blocks data for retrospect...')
with open('data/data.csv', 'r') as f:
    lines = f.readlines()
    for line in lines:
        addr_in, addr_out, val = line.split(',')
        if addr_in not in graph_node.keys():
            graph_node[addr_in] = node_id
            node_id += 1
        if addr_out not in graph_node.keys():
            graph_node[addr_out] = node_id
            node_id += 1
        if graph_node[addr_in] in graph.keys():
            if addr_out in graph[graph_node[addr_in]].keys():
                graph[graph_node[addr_in]][graph_node[addr_out]] += float(val)
            else:
                graph[graph_node[addr_in]][graph_node[addr_out]] = float(val)
        else:
            graph[graph_node[addr_in]] = {graph_node[addr_out] : float(val)}

print('Start loading 100 blocks done!')
# G = nx.DiGraph()
f = open('data/retrospect_res.txt', 'w')


def parse_node(node, t):
    if t > 8:
        return 
    vis.append(node)
    if node in graph.keys():
        for key in graph[node].keys():
            # G.add_node(node)
            # G.add_edge(node, key, weight=graph[node][key])
            f.write(str(node) + ' ' + str(key) + '\n')
            if key not in vis:
                parse_node(key, t=t+1)
# while(True):
#     nodeID = np.random.randint(0, len(graph_node.keys()))
#     if nodeID in graph.keys():
#         break
    # 486694
# print('parse ID: %d' % nodeID)
hash = [key for key in graph_node.keys() if graph_node[key] == 484494]
print('Start retrospect node index 486694, with hash %s.' % hash[0])
parse_node(486694, t=0)
f.close()

# pos = nx.spring_layout(G)
# nx.draw(G, with_labels=True)
# nx.draw_networkx_edge_labels(G, pos=pos ,edge_labels=nx.get_edge_attributes(G, 'weight'))
# plt.show()

