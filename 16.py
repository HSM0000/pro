def solution(n):
    rev=''
    answer = 0
    while n>0:
        n,mod=divmod(n,3)
        rev += str(mod)
    answer=int(rev,3)
    return answer

num=int(input())
print(solution(num))