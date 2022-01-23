def solution(left, right):
    answer = 0
    for i in range(left,right+1) :
        answer += check(i)

    return answer

def check(num) :
    cnt=0
    for i in range(1,num+1) :
        if num%i==0 :
            cnt+=1
    if cnt %2==0 : #짝수
        return num
    else : return -num