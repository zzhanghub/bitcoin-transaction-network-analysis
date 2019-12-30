import numpy as np 
if __name__ == "__main__":
    for k in range(50):
        graph = {}
        graph_node = {}
        node_id = 0
        with open('data/data_block%d.csv' % (k+1), 'r') as f:
            lines = f.readlines()
        for line in lines:
            addr_in, addr_out, val = line.split(',')
            if addr_in not in graph_node.keys():
                graph_node[addr_in] = node_id
                node_id += 1
            if addr_out not in graph_node.keys():
                graph_node[addr_out] = node_id
                node_id += 1
            if addr_in in graph.keys():
                if addr_out in graph[addr_in].keys():
                    graph[addr_in][addr_out] += float(val)
                else:
                    graph[addr_in][addr_out] = float(val)
            else:
                graph[addr_in] = {addr_out : float(val)}

        with open('data/graph_%d.txt' % (k+1), 'w') as f:
            for addr_in in graph.keys():
                for addr_out in graph[addr_in].keys():
                    id_in = graph_node[addr_in]
                    id_out = graph_node[addr_out]
                    val = graph[addr_in][addr_out]
                    f.write(str(id_in) + ' ' + str(id_out) + ' ' + str(val) + '\n')

        with open('data/mapping_%d.txt' % (k+1), 'w') as f:
            for key in graph_node.keys():
                f.write(str(key) + ' ' + str(graph_node[key]) + '\n')

        print('parsing %d done.' % (k+1))
