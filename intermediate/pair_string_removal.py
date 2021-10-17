def solution_fail(s):
    answer = -1
    s_array=list(s)

    while True:
        trans_s = ''.join(s_array)        
        for i in range(len(s_array) -1):
            if s_array[i] == s_array[i+1]:                
                del s_array[i:i+2]
                break

        if trans_s == ''.join(s_array):
            answer = 0
            break
        if len(s_array) <= 0:
            answer = 1
            break

    return answer

def solution(s):
    answer = -1    
    stack = [s[0]]
    
    for v in s[1:]:
        if len(stack) > 0 and v == stack[-1]:
            stack.pop()
        else:
            stack.append(v)
    answer =  0 if len(stack) else 1
    return answer

s = 'baabaa'
s = 'cdcd'
print(solution(s))