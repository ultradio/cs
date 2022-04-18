def solution(X, Y, D):

    answer = (Y - X) // D
    remainder = (Y - X) % D
    if remainder != 0:
        answer += 1

    return answer

print(solution(10, 85, 30))
print(solution(80, 85, 30))
