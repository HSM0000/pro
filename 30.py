def solution(strings, n):
    strings.sort()
    strings.sort(key= lambda x:x[n])
    return strings

strings=["sun", "bed", "car"]
print(solution(strings,1))
