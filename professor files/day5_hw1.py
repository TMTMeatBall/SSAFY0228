import calendar

# # 해당연도가 윤년인지 확인해주는 함수
# print(calendar.isleap(2020))

# # 해당연도의 달력을 문자열로 반환해주는 함수
# print(calendar.calendar(2020))


# 해당 년월일 입력값으로 넣으면 해당 요일을 반환 함수
week_num = calendar.weekday(2023, 1, 16)

week_list = ['월', '화', '수', '목', '금', '토', '일']

# print(str(week_list[week_num]) + "요일 입니다.")

if not week_num:
    print('경고 월요일입니다!')

