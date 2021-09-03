def solution(lottos, win_nums):
    lottos.sort()
    win_nums.sort()
    count =0
    num=0
    for i in range(6) :
        for j in range(6):
            if lottos[i]== 0 : 
                count +=1 
                break
            if lottos[i]== win_nums[j] :
                num +=1
                break
    if count ==6 :
        answer =[1,6]
    elif count ==0 and num ==0 :
        answer = [6,6]
    else :
        answer = [6-num-count+1,6-num+1]
    return answer