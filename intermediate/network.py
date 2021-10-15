def solution(n, computers):
   
    def bfs(graph, root, visited):        
        queue = deque([root])
        while len(queue) > 0:
            node = queue.popleft()
            if not visited[node]:
                visited[node] = True
            
            for i in graph[node]:
                if not visited[i]:
                    queue.append(i)
        return visited
    
    from collections import deque
    answer = 0
    
    graph = {}
    graph = {i: {} for i in range(n)} # !!
    
    for i, computer in enumerate(computers):
        for j, k in enumerate(computer):
            if i != j and k == 1:
                if not graph.get(i, None):
                    graph[i] = set([j])
                else:
                    graph[i].add(j)    

    visited = [False for i in range(n)]    
    for i in range(n): # !!
        if not visited[i]:
            visited = bfs(graph, i, visited)
            answer += 1

    return answer


n = 3
#computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))