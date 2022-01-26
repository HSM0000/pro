def solution(s):
    if len(s)>6 or len(s)<4: return False 
    if s.isdigit()==True :return True # isdigit 모두 숫자면 True아니면 false반환
    return False

print(solution("11122a"))