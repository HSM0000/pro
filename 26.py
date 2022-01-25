import datetime

def get_days(mm,dd) :
    days=['MON','TUE','WED','THU','FRI','SAT','SUN']
    return days[datetime.date(2016,mm,dd).weekday()]
def solution(a, b):
    answer = get_days(a,b)
    return answer