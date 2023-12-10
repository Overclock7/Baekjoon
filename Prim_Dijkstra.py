from sys import maxsize # like INF
from heapdict import heapdict

def Prim(graph, start):
    mst = []
    distance = heapdict()
    tree = dict()   
    
    #초기화
    for node in graph.keys():
        distance[node] = maxsize
        tree[node] = None
    distance[start], tree[start] = 0, start

    while len(mst) != len(mygraph):
        current_node, current_key = distance.popitem()
        
        mst.append([tree[current_node], current_node, current_key])
        
        for adjacent, weight in graph[current_node].items():
            if adjacent in distance and weight < distance[adjacent]:
                distance[adjacent] = weight
                tree[adjacent] = current_node
    return mst

def Dijkstra(graph, start):
    S = []
    distance = heapdict()
    tree = dict()   
    
    #초기화
    for node in graph.keys():
        distance[node] = maxsize
        tree[node] = None
    distance[start], tree[start] = 0, start

    while len(mst) != len(mygraph):
        current_node, current_key = distance.popitem()
        
        S.append([tree[current_node], current_node, current_key])
        
        for adjacent, weight in graph[current_node].items():
            if adjacent in distance and (weight + distance[adjacent]) < distance[adjacent]:
                distance[adjacent] = weight + distance[adjacent]
                tree[adjacent] = current_node
    return mst

mygraph = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'D': 9, 'C': 8, 'E': 7},
    'C': {'B': 8, 'E': 5},
    'D': {'A': 5, 'B': 9, 'E': 7, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 7, 'F': 8, 'G': 9},
    'F': {'D': 6, 'E': 8, 'G': 11},
    'G': {'E': 9, 'F': 11}   
}

mst= Prim(mygraph, 'A')
s = Dijkstra(mygraph,'A')
print(mst,'\n',s)