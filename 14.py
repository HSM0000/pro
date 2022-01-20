def solution(array, commands):
    answer = []
    for i in commands :
        array_copy=[]
        array_copy=array[i[0]-1:i[1]]
        array_copy.sort()
        answer.append(array_copy[i[2]-1])
    return answer

num_list=list(map(int,input().split()))
arr=[]
for i in range(1):
    arr.append(list(map(int,input().split())))
print(solution(num_list,arr))