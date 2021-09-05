def solution(new_id):
    an = new_id.lower()# 1단계
    cnt=0
    an= list(an)
    while True :#2단계
        if an[cnt]<'0' or '9'<an[cnt]<'a'or an[cnt]>'z' :
            if an[cnt]!='.'and an[cnt]!='-'and an[cnt]!='_' :
                del an[cnt]
            else :    
                cnt +=1
        else :    
            cnt +=1
        if cnt == len(an) :
            break
    cnt=0
    while True :#3단계
        if cnt >= len(an)-1 :
            break
        if an[cnt] == '.' :
            if an[cnt+1] == '.' :
                del an[cnt+1]
            else :
                cnt=cnt+1
        else :
                cnt=cnt+1
    if an[0]=='.' :#4단계
        del an[0]
    if len(an)!=0 :
        if an[len(an)-1] == '.' :
            del an[len(an)-1]
    if len(an) ==0 :#5단계
        an.append('a')
    if len(an)>=16 :#6단계
        del an[15:]
        if an[len(an)-1] == '.' :
            del an[len(an)-1]
    if len(an)<=2 :#7단계
        cnt=len(an)-1
        while True :
            an.append(an[cnt])
            cnt +=1
            if len(an)== 3: break
    answer = ''.join(an)
    return answer

new_id=input()
print(solution(new_id))