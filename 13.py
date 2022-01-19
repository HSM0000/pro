def solution(absolutes, signs):
    answer=0
    while True :
        if not signs : break
        ab=absolutes.pop(0)
        sign=signs.pop(0)
        answer+=check(ab,sign)
    return answer

def check(num,sign) :
    if sign == "true" :return num
    if sign == "false" : return -1*num


num_list=list(map(int,input().split()))
s=input().split()
answer=solution(num_list,s)
print(answer)