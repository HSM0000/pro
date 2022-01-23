def solution(n):
    answer = mo(n)
    return answer

def mo(n) :
    for i in range(2,n):
        if n%i==1 :return i
    if i+1==n :return n
