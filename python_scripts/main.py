import numpy as np
import hashlib

def md5hash(key):
    key = str.encode(str(key))
    m = hashlib.md5()
    m.update(key)
    return m.hexdigest()

def getJoccard(Hash_1, Hash_2):
    num_same = 0
    for i in range(len(Hash_1)):
        if Hash_1[i] in Hash_2:
            num_same += 1
    for i in range(len(Hash_2)):
        if Hash_2[i] in Hash_1:
            num_same += 1
    # Joccard = (num_same + 0.) / float(len(Hash_1) + len(Hash_2) - num_same)
    Joccard = (num_same + 0.) / float(len(Hash_1) + len(Hash_2))
    return Joccard

def getHashList(Dgraph, nnodes, iterations=30):
    '''
    Dgraph: directed graph, {{}}
    '''

    graph = [[] for i in range(nnodes)]
    for u, v in enumerate(Dgraph):
        if u == v:
            continue
        if v not in graph[u]:
            graph[u].append(v)
        if u not in graph[v]:
            graph[v].append(u)
    val = md5hash('1')
    Hash = [val for i in range(nnodes)]
    
    for _ in range(iterations):
        new_Hash = [val for i in range(nnodes)]
        for i in range(nnodes):
            tmp_hash_list = [Hash[i]]
            for j in graph[i]:
                tmp_hash_list.append(Hash[j])
            tmp_hash_list.sort()
            key = ''
            for k in tmp_hash_list:
                key += k
            new_Hash[i] = md5hash(key)
        for i in range(nnodes):
            Hash[i] = new_Hash[i]
    
    return Hash


graph = {}

graph_node = {}
vis = []
node_id = 0

with open('./data_block1.csv', 'r') as f:
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

print('Data loading done. Number of nodes: %d' % len(list(graph_node.keys())))
hash1 = getHashList(graph, len(list(graph_node.keys())))

graph = {}

graph_node = {}
vis = []
node_id = 0

with open('./data_block2.csv', 'r') as f:
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

print('Data loading done. Number of nodes: %d' % len(list(graph_node.keys())))
hash2 = getHashList(graph, len(list(graph_node.keys())))

print(getJoccard(hash1, hash2))