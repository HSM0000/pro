import itertools
def solution(nums):
    answer = 0
    #세개이상의 값을 더하기
    total=itertools.combinations(nums,3)
    total_list=[]
    for i in total :
        total_list.append(sum(i))
          
    #1과 자기자신 빼고 나누면서 나눠지는 것이 없으면 카운트
    for i in total_list:
        for j in range(2,i+1):
            if i%j==0 :break
        if j== i : answer+=1

    return answer

num_list=list(map(int,input().split()))
answer=solution(num_list)
print(answer)