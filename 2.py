num =int(input())
count=0
list=[0 for i in range(num)]
while num !=0 : #받은 횟수만큼 돌리기
    x1,y1,r1,x2,y2,r2 = map(int,input().split())#좌표와 거리  입력
    if x1 == x2 and y1 == y2 :#좌표가 같은경우
        if r1 == r2 :#거리가 같아 무한
            list[count]= -1
        else :#거리가 달라 겹치는게 없음
            list[count] = 0
    else :#그외 나머지 
        a=((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1))#좌표사이거리
        b= (r1+r2)*(r1+r2) # 거리
        if a==b or a==(r2-r1)*(r2-r1) :#겹치는 구간이 한곳이라면 좌표사이의 거리가 r1+r2의 거리와 같다
            list[count]=1
        elif a > b:# 좌표사이의 거리가 거리합보다 커서 닿지가 않음
            list[count]=0
        elif a < (r2-r1)*(r2-r1) :
            list[count]=0
        else :#2개 겹침
            list[count]=2
    count=count+1
    num = num -1

#결과
for i in list :
    print(i)