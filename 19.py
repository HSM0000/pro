def solution(numbers):
    answer = []
    while True :
        cnt=numbers.pop(0)
        for i in numbers :
            answer.append(i+cnt)
        if not numbers: break 
    answer=set(answer)
    answer=list(answer)
    answer.sort()
    return answer