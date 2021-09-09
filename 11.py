def solution(numbers):
    answer =0
    arr = [0,1,2,3,4,5,6,7,8,9]
    num= list(set(arr) -set(numbers))
    answer =sum(num)
    return answer
 
numbers =list(map(int, input().split()))
print(solution(numbers))
