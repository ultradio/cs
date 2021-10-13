"""
Divide & Conquer
풀려는 문제가 클 경우 그 문제를 작은 문제들로 나누고(Divide),
그 문제를 푼 뒤(Conquer) 다시 합쳐나가는(Combine) 방식이다.
"""

"""
Recusion

n번째 피노나치 수를 리턴
f(1) = 1
f(2) = 1
f(3) = f(1) + f(2)
f(3) = f(2) + f(3)
"""
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1) # !!
    
for i in range(1, 11):
    print(fib(i))  
"""
Memozation
분활 정복법과 비슷하며, 차이점은 부분 문제를 메모하면서 재귀적으로 푼다.
"""
def fib_memo(n, cache):
    if n == 1 or n == 2:
        cache[n] = 1
        return 1
    else:
        if not cache.get(n, None):
            cache[n] = fib_memo(n-2, cache) + fib_memo(n-1, cache)
        return cache.get(n)

cache = {} # !!
for i in range(1, 11):
    print(fib_memo(i, cache))

"""
Tabulation
분할 정복법과 비슷하며, 차이점은 테이블 방식으로 정리하면서 문제를 반복문으로 푼다.
Memoization과 차이점은 재귀 대신 반복문을 사용하는 것이다.
"""
def fib_tab(n):
    cache = {1:1, 2:1} # !!
    for i in range(1, n):
        if not cache.get(i, None):
            cache[i] = cache.get(i-2) + cache.get(i-1)
    return cache.get(n-2) + cache.get(n-1)

print(fib_tab(10))

"""
완전 탐색
모든 경우의 수를 다 해본다.
"""

def fib_iter(n):
    series = [0,1,1] # !!
    for i in range(3, n):
        next_element = series[i-2] + series[i-1]
        series.append(next_element) # !!
    return series[n-2] + series[n-1]

print(fib_iter(10))