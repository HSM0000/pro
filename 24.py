def solution(s):
    answer = True
    s=s.lower()
    pcount=s.count("p")
    ycount=s.count("y")
    return (pcount==ycount)
