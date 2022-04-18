
def solution(A):
    total_sum = sum(A)
    left_sum = 0
    right_sum = 0
    answer = 10000000

    for i, a in enumerate(A[:-1]):
        print(i, a)
        left_sum = left_sum + A[i]
        right_sum = total_sum - left_sum
        answer = min(answer, abs(left_sum - right_sum))
        print(left_sum, right_sum, answer)
    
    return answer


print(solution([3, 1, 2, 4, 3]))
print(solution([-1000, 1000]))
