def solution(N):
    quotient = N
    remainder = 0
    answers = []
    
    if N == 0 or N == 1:
        return 0

    while True:
        remainder = quotient % 2
        quotient = quotient // 2
        if remainder == 0:
            answers.insert(0, 0)
        else:
            answers.insert(0, 1)
        
        if quotient == 1:
            answers.insert(0, 1)
            break;
    print(answers)

    answer = 0
    temp = 0
    for a in answers:
        if a == 0:
            temp += 1
        else:
            answer = max(temp, answer)
            temp = 0
    
    return answer

print(solution(1))
print(solution(2))
print(solution(9))
print(solution(529))
print(solution(20))
print(solution(15))
print(solution(32))