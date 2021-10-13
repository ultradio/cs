
n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
graph = {}
root = 1

def solution(n, edge):
    graph = {}    
    for [n1, n2] in edge:
        if not graph.get(n1, None):
            graph[n1] = dict({n2:1})
        else:
            graph[n1][n2] = 1        
        if not graph.get(n2, None):
            graph[n2] = dict({n1:1})
        else:
            graph[n2][n1] = 1
    
    import heapq
    
    dists = {}
    start_node = 1    
    for node in graph:
        dists[node] = [float('inf'), start_node]
    
    queue = []
    dists[start_node] = [0, start_node]
    heapq.heappush(queue, dists[start_node])
    
    while len(queue) > 0:
        curr_dist, curr_node = heapq.heappop(queue)
        if dists[curr_node][0] < curr_dist:
            continue
        
        for adj_node, w in graph[curr_node].items():
            dist = curr_dist + w
            if dists[adj_node][0] > dist:
                dists[adj_node] = [dist, curr_node]
                heapq.heappush(queue,[dist, adj_node] )   
    answer = 0    
    max_dist = max(dists.items(), key=lambda x: x[1][0])[1][0]
    for i, [d, n] in dists.items():
        if max_dist == d:
            answer += 1
    return answer


solution(n, vertex)