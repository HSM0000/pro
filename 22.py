def solution(d, budget):
    answer = 0
    num=0
    d.sort()
    for i in d :
        num+=i
        if num <= budget :
            answer+=1

    return answer
numlist=list(map(int,input().split()))
num=int(input())
print(solution(numlist,num))