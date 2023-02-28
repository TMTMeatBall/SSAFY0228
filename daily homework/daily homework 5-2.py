# ; 연도, 월, 일을 순서대로 입력받는다.
# ; 윤년으로 가면 타임머신에 에러가 생긴다. 윤년을 입력했을 경우 연도를 다시 입력받아야 한다.
# ; 윤년이 아닌 연도를 입력받을 경우, 날짜를 편하게 정할 수 있도록 해당 연도의 달력을 출력하라.
# ; 김코딩은 월요일을 싫어한다. 입력한 날짜가 월요일인 경우 경고 메시지를 출력하라.
# ; 입력이 완료되면 연, 월, 날짜, 그리고 요일을 dictionary에 정리하여 출력하라.
# ; HINT: calendar 모듈을 활용하라.	(공식문서 링크)

# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
# 경고 월요일입니다.
# {'년': 2015, '월': 8, '일': 31, '요일': '월요일'}


import calendar
from datetime import datetime


year = int(input("연도를 입력해주세요: "))
month = int(input("월을 입력해주세요: "))
day = int(input("일을 입력해주세요: "))


while calendar.isleap(year):
    print(f'{year} 윤년. 연도를 다시 입력하시오.')
    year=int(input())


print(calendar.calendar(year))

week_integer = calendar.weekday(year, month, day)

week_dict = {
    0:'월',
    1:'화',
    2:'수',
    3:'목',
    4:'금',
    5:'토',
    6:'일'
}

if week_integer ==0:
    print('경고 월요일 입니다.')


print(week_dict[week_integer] + '요일 입니다.')

ymd = {'년': year, '월': month, '일': day, '요일': week_dict[week_integer]+'요일'}
print(ymd)