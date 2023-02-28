import calendar
year = int(input('년도를 입력해주세요: '))

if calendar.isleap(year):
    print(f'{year}는 윤년입니다.')
else:
    print(f'{year}는 윤년이 아닙니다.')