def solution(progresses, speeds):
    answer = []
    days = []
    pre_day = -1
    import math
    for p, s in zip(progresses, speeds):
        day = math.ceil((100 - p)/s)
        if pre_day > day:
            days.append(pre_day)
        else:
             days.append(day)
             pre_day = day
    
    #print(days)
    pre_day = -1
    count = 1 # !!
    for i, day in enumerate(days[:-1]):
        if day == days[i+1]:
            count+=1
        else:
            answer.append(count)
            count = 1
    answer.append(count) # !!
    #print(answer)
    return answer


#progresses = [93, 30, 55]
#speeds = [1, 30, 5]

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]	
print(solution(progresses, speeds))