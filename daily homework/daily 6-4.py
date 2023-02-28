#1. 가장 많이 입장한 세 사람을 출력
#2. 입장 횟수 != 퇴장 횟수 인 사람을 출력
#3. collection 모듈의 counter 객체를 사용


entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']

from collections import Counter
#딕셔너리화
entry_record_dict = Counter(entry_record)
exit_record_dict = Counter(exit_record)

print('입장 기록이 많은 Top3')
for name, count in entry_record_dict.most_common(3):
    print(f'{name} {count}회')
# for item in entry_record_dict.most_common(3): for구문 사용시
#     print(f'{item[0]} {item[1]}회')

entry_record_dict.subtract(exit_record_dict)

print()

print('출입 기록이 수상한 사람 목록')

for name, diff in entry_record_dict.items():
    #diff 가 0 이 아닌 값을
    if diff>0:
        print(f'이 {name}은 입장 기록이 {diff}회 더 많아 수상합니다.')
    elif diff<0:
        print(f'이 {name}은 퇴장 기록이 {-diff}회 더 많아 수상합니다.')

# for name, diff in entry_record_dict.items():
#     if diff > 0:
#         print(f'{name}은 입장 기록이 {diff}회 더 많아 수상합니다.')
#     elif diff < 0:
#         print(f'{name}은 입장 기록이 {-diff}회 더 많아 수상합니다.')

# print(Counter(entry_record).most_common(3))
# # key 값 , value 값
# print( f' 가장 많이 입장한 사람은:', {key},{value},'회')
# print('가장 많이 입장한 사람은: ', Counter(entry_record).most_common(3),'회')


# #서로 Counter 해서
# Counter(entry_record)
# Counter(exit_record)
# #비교한 숫자가 다른 사람
