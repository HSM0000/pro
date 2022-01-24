def solution(arr):
    answer=[]
    cnt=0
    count=0
    arr.insert(len(arr),-1)
    for i in arr :
        if i!=arr[cnt] :
            answer.append(arr[cnt])
            cnt=count
        count+=1

    return answer
numlist=list(map(int,input().split()))
print(solution(numlist))