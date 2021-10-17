def solution(priorities, location):
    answer = 0
    
    if len(priorities) == 1 and location == 0:
        return 1

    from collections import deque
    queue = deque()
    for i, p in enumerate(priorities):
        queue.append((i, p))
    
    #print(queue)    
    printed = []
    max_prior = max([x[1] for x in queue])
    while len(queue) > 0:
        i, p = queue.popleft()
        #print("i={}, p={}, max_prior={}".format(i, p, max_prior))
        if max_prior == p:
            if len(queue) > 0:
                max_prior = max([x[1] for x in queue])
            printed.append((i, p))
            if i == location:
                break
        else:
            queue.append((i, p))
    #print(printed)
    answer = len(printed)
    return answer



priorities = [2, 1, 3, 2]
location = 2

priorities = [1]	
location = 0


priorities = [1, 1, 9, 1, 1, 1]	
location = 0

print(solution(priorities, location))

