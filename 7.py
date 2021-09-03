def solution(word):
    li=list(word)
    an=0
    num=781
    for i in range(len(li)) :
        if li[i]=='A' :
            an +=0*num+1
        elif li[i]=='E':
            an += 1*num+1
        elif li[i]=='I':
            an += 2*num+1
        elif li[i]=='O':
            an += 3*num+1
        else :
            an += 4*num+1
        num = int(num-1)/5    
            
    answer = int(an)
    return answer

word=input()
print(solution(word)) 