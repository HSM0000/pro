def solution(s):
    n=int(len(s)/2)
    anwer=''
    if len(s)%2==0 :#짝수
        return s[n-1:n+1]#문자열은 abcd면 0a1b2c3d4처럼 슬라이스 한다
    else : return s[n]

arr=input()
print(solution(arr))