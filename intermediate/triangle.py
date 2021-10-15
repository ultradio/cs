def solution(triangle):
    cache = []
    for i, values in enumerate(triangle):
        temp = []
        for j, value in enumerate(values):
            temp.append(-1)
        cache.append(temp)

    for i, values in enumerate(triangle):
        for j, value in enumerate(values):
            if i == 0:
                cache[0][0] = triangle[0][0]
                continue

            if j == 0:
                cache[i][j] = cache[i-1][0] + triangle[i][j]
            elif j == len(values)-1:
                cache[i][j] = cache[i-1][-1] + triangle[i][j]
            else:
                cache[i][j] = max(cache[i-1][j-1] + triangle[i][j], cache[i-1][j] + triangle[i][j])
    
    answer = 0
    for values in cache:
        answer = max(max(values), answer)
    
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))