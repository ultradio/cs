"""
출발노드에서 목적지 노드로 가는 최단 경로를 구한다.
"""
import heapq

def dijkstra(graph, start_node, end_node):
    dists = {} # {'A': [0, 'A'], 'B': [inf, 'A']}
    for node in graph:
        dists[node] = [float('inf'), start_node]
        
    queue = []
    dists[start_node] = [0, start_node]
    heapq.heappush(queue, dists[start_node])

    while len(queue) > 0:
        curr_dist, curr_node  = heapq.heappop(queue)
        if dists[curr_node][0] < curr_dist:
            continue
        
        for adj_node, w in graph[curr_node].items():
            dist = curr_dist + w
            if dist < dists[adj_node][0]:
                dists[adj_node] = [dist, curr_node]
                heapq.heappush(queue, [dist, adj_node])
    
    return dists

graph = {    
         'A': {'B': 8, 'C': 1, 'D': 2},
         'B': {},
         'C': {'B': 5, 'D': 2},
         'D': {'E': 3, 'F': 5},
         'E': {'F': 1},
         'F': {'A': 5}
         }

dists = dijkstra(graph, 'A', 'F')
print(dists)

def shortest_path(dists, start_node, end_node):
    path = end_node
    path_output = end_node

    while path != start_node:
        path = dists[path][1]
        path_output += '->' + path
    
    return path_output  
    
path_output = shortest_path(dists, 'A', 'F')
print(path_output)