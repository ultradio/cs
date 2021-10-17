def solution(arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        temp = []
        for i, j in zip(a1, a2):
            temp.append(i+j)            
        answer.append(temp)
    return answer

arr1=[[1,2],[2,3]]
arr2=[[3,4],[5,6]]
# [[4,6],[7,9]]

arr1=[[1],[2]]
arr2=[[3],[4]]
# [[4],[6]]
print(solution(arr1, arr2))

def solution(a, b):
    answer = 0
    temp = 0
    if a > b:
        temp=a
        a=b
        b=temp
        
    for i in range(a, b+1):
        answer += i
    return answer
a=3
b=5
a=5
b=3
#a=-1
#b=2
print(solution(a, b))


def solution(numbers):
    answer = set([])
    from itertools import combinations
    for i, j in combinations(numbers, 2):
        answer.add(i+j)    
    return sorted(list(answer))

numbers=[2,1,3,4,1]
numbers=[5,0,2,7]
numbers=[5,0]
print(solution(numbers))