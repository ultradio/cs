
def solution(A):
    _A = []
    for a in A:
        if a > 0:
            _A.append(a)
    print(_A)
    
    A = sorted(set(_A))
    if len(A) == 0 or A[0] > 1:
        return 1

    for a, b in zip(range(A[0], A[0] + len(A)+ 1), A):
        print(a, b)
        if a != b:
            return a

    return A[-1] + 1
 
print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-1, -3]))
print(solution([2]))
print(solution([-1000000, 1000000]))
