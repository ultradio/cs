

def solution(A):
    A = sorted(A)
    print(A)
    if len(A) == 0:
        return 1

    for a, b in zip(A[0:], range(1, len(A)+1)):
        print (a, b)
        if a != b:
            return b

    return A[-1] + 1

print(solution([2, 3, 1, 5]))
print(solution([1]))
print(solution([2]))
print(solution([1, 2]))
print(solution([2, 3]))
print(solution([]))
