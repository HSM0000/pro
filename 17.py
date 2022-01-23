def solution(N, stages):
    answer = []
    result=[[0]*2 for i in range(N)]#순서 2중배열
    stages.sort()#배열 정렬
    count=0
    while True :
        cnt=0
        if not stages :
            if len(result) != count:
                for j in range(count,N) :
                    result[j][0]=j+1
                    result[j][1]=0
            break
        if count==N :break
        for i in range(len(stages)):
            if count+1 == stages[i] : cnt=i+1 
        result[count][0]=count+1 #해당 스테이지 입력
        result[count][1]=cnt/len(stages) #해당 스테이지에 실패율 입력
        del stages[0:cnt] # 계산한 스테이지 삭제
        count +=1
    result.sort(key=lambda x:-x[1])# 스테이지 실패율로 정렬
    for i in range(N) :
        answer.append(result[i][0])

    return answer

num =int(input())
numlist=list(map(int,input().split()))
print(solution(num,numlist))
