def solution(price, money, count):
    answer = -1
    mon=0
    for i in range(1,count+1) :
        mon+= price*i
    answer=money-mon
    if answer <0 : return -answer
    else : return 0
