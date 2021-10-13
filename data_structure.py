"""
사용법은 ' """ '으로 코드설명은 ' # ' 으로 주석을 달았다.
"""

찾고자 하는 문자열 A가 문자열 B의 맨 앞에 있는지 여부 검사
"""
some_str = 'abcde'
ok1 = some_str.startswith('ab')
ok2 = some_str.startswith('cde')

print(ok1)
print(ok2)

"""
zip으로 앞뒤 값 비교하기
"""
items = [1,2,3]
for i, j in zip(items, items[1:]):
    if i == j:
        print("same: {}".format((i, j)))
    else:
        print("diff: {}".format((i, j)))
        
"""
문자열 뒤깁기
"""
some_str = 'ABC'
reversed_str = ''.join(reversed(some_str))
print(reversed_str)

"""
리스트 정렬
"""
some_list = [1,2,3]
some_list = sorted(some_list)
print(some_list)

"""
딕셔너리 정럴
"""
some_dict = {'a':1, 'b':2, 'c':3}
some_dict = sorted(some_dict.items(), key = lambda x: x[1])
print(some_dict)

"""
순열 - 순서대로 뽑음
"""
from itertools import permutations
items = ['1','2','3']
items = permutations(items, 2)
items = map(''.join, items)
print(list(items))

"""
조합 - 순열과 다르게 뽑아서 순서를 고려하지 않음
예) 1,2,3,4 중 2개의 숫자를 뽑아 자연수를 만드는 경우
순열은 12,21 가 나왔을 때 조합은 12만 나옴
"""
from itertools import combinations
items = ['1','2','3']
items = combinations(items, 2)
items = map(''.join, items)
print(list(items))

"""
매번 정렬이 필요한 경우
"""
import heapq

some_list = [3,2,1]
heapq.heapify(some_list)
heapq.heappop(some_list)
heapq.heappush(some_list, 4)
print(some_list)