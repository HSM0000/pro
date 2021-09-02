def solution(numbers, target):
    
    answer = dfs(0,numbers,target)
    return answer

def dfs(idx,numbers,target) :
    answer =0
    if idx == len(numbers) :
        if sum(numbers) == target :
            return 1
        else :
            return 0
    else :
        answer += dfs(idx+1,numbers,target)
        numbers[idx] *= -1
        answer += dfs(idx+1,numbers,target)
    return answer
    