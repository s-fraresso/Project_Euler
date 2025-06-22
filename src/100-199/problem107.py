from heapq import heapify, heappop

def read_network(path):
    with open(path, 'r') as f:
        network = [line.strip().split(',') for line in f.readlines()]        
    edges = []
    nb_vertices = len(network)
    for i in range(nb_vertices):
        for j in range(i + 1, nb_vertices):
            if network[i][j] != '-':
                edges.append((int(network[i][j]), i, j)) # edge = (weight, start, end)
    return edges, nb_vertices


def find_root(x, parent):
    r = x
    while parent[r] != r:
        r = parent[r]
    return r


def kruskal(edges, nb_vertices):
    heapify(edges) # first element will always be the lighest edge
    parent = list(range(nb_vertices)) # at the start each node is its own parent
    final_edges = []
    while len(final_edges) < nb_vertices - 1: # we stop when final_edges is a tree
        edge = heappop(edges) # select the lightest available edge
        x, y = edge[1], edge[2]
        rx, ry = find_root(x, parent), find_root(y, parent) # roots of x and y's respective CC
        if rx == ry: # adding this edge would make the tree cyclic
            continue
        parent[ry] = rx
        final_edges.append(edge)
    return final_edges, nb_vertices


edges, nb_vertices = read_network("input_files\\0107_network.txt")
original_weight = sum(edge[0] for edge in edges)
optimal_edges, nb_vertices = kruskal(edges, nb_vertices)
print(original_weight - sum(edge[0] for edge in optimal_edges))