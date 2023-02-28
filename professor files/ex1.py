# x = 2 #정수 2
# y = 3 #정수 3
# z = 1.2 #실수 1.2

# # 더하기
# print(x + y)

# #빼기
# print(x - y)

# #곱하기
# print(x * y)


# # 나누기
# print(x / y)

# # 나누기를 했을 때의 몫
# print(y // x)


# # 나머지 연산
# print(x % y)

# # x의 y제곱
# print(x ** y)



# # 리스트 실습
# #주어진 성적 리스트
grade = [60, 55, 70, 80, 92, 40, 60]
# print(41 in grade)

# 평균값
# print(sum(grade) / len(grade))


# # 번외. average 함수를 정의해서 사용
# def average(grade):
#     return sum(grade) / len(grade)

# print(average(grade))

# # 성적 리스트를 출력
# print(grade)
# # 1. 커스텀으로 출력
# #print(grade[0], grade[1], grade[2], ...)
# print(*grade)
# print(*grade, sep=', ')

# # 마지막 성적을 삭제
# # del grade[len(grade) - 1]
# grade.pop()
# print(grade)

# # 세번째 성적을 삭제
# grade.remove(grade[2])
# # grade = grade[0:2] + grade[3:] # 슬라이드
# print(grade)

# # 마지막에 새로운 성적 50을 추가
# grade.append(50)
# print(grade)

# # 세번째에 새로운 성적 100 추가
# grade.insert(2, 100)
# print(grade)

# # 모든 성적을 5씩 높히기
# for i in range(len(grade)):
#     grade[i] += 5 # 5씩 높이겠다

# # enumerate 내장 함수
# # for idx, num in enumerate(grade):
# #     grade[idx] = num + 5

# # 리스트 컴프리헨션 (심화)
# # grade = [i+5 for i in grade]


# # 내장 함수 사용하기 (번외)
# # 성적 리스트의 길이 출력하기
# print(len(grade))

# # 성적을 오름차순으로 정렬하기
# print(sorted(grade))


# # 성적을 내림차순으로 정렬하기
# print(sorted(grade, reverse=True))

# 전화번호부 딕셔너리
phone = {'홍길동' : '010-1111-2222', '김남길': '010-2222-3333', '김철수' : '010-3333-4444'}
print(phone)

# 홍길동의 전화번호를 '010-1234-1234' 로 바꾸기
phone['홍길동'] = '010-1234-1234'
print(phone)

# 새로운 전화번호를 하나 추가
phone['신짱구'] = '010-9999-9999'
print(phone)

phone.update({'신병만' : '010-8888-8888'})
print(phone)

# 전화번호부에 등록되어있는 이름들을 전부 출력해보세요
print(phone.keys())

# 전화번호부의 등록된 번호들 출력
print(phone.values())

# 홍길동 전화번호를 삭제
del phone['홍길동']
print(phone)

# 모든 전화번호를 삭제
phone.clear()
print(phone)

# (번외) '홍길동' 이 딕셔너리에 있는지 참/거짓
print('홍길동' in phone)


# 성적
grade = 50

# 성적이 60점 미만이면 과락, 아니면 통과 출력

# 권장o
if 60 > grade: # 60점 미만이라면
    print('과락')
else:
    print('통과')

# 권장x
if 60 > grade:
    print('과락')
if 60 <= grade:
    print('통과')

# 성적이 90점 이상이면 'A'
# 성적이 90점 미만 80점 이상이면 'B'
# 성적이 80점 미만 70점 이상이면 'C'
# 성적이 70점 미만 60점 이상이면 'D'
# 성적이 60점 미만이면 'F'
# if ~ elif ~ else

if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')


# 60이상 80미만인 경우 '우수'
if 60 <= grade < 80:
    print('우수')
    
# 번외 (이렇게도 표현이 가능)
if 60 <= grade and grade < 80:
    print('우수')


# #주어진 성적 리스트
grade = [60, 55, 70, 80, 92, 40, 60]

# 성적 중에서 가장 큰 값을 가져오기
mx = grade[0] #최대값
for i in grade:
    if i > mx:
        mx = i
print(mx)

# 성적 중에서 가장 작은 값을 가져오기
mn = grade[0] #최소값
for i in grade:
    if i > mn:
        mn = i
print(mn)

# 성적 중에서 과락이 있는 성적을 확인하고 출력하기 (조건문 + 반복문)
for i in grade:
    if 60 > i:
        print("과락 점수 : ", i)


# 성적들을 각각 'A', 'B', 'C', 'D', 'F' 출력하기
for i in grade:
    if i >= 90:
        print('A')
    elif i >= 80:
        print('B')
    elif i >= 70:
        print('C')
    elif i >= 60:
        print('D')
    else:
        print('F')


# 성적들을 각각 'A', 'B', 'C', 'D', 'F' 새로운 리스트 만들기
m = [] # 성적 리스트
for i in grade:
    if i >= 90:
        m.append('A')
    elif i >= 80:
        m.append('B')
    elif i >= 70:
        m.append('C')
    elif i >= 60:
        m.append('D')
    else:
        m.append('F')

print(m)

ex = ['F'] *6 + ['D', 'C', 'B', 'A'] 
for i in grade:
    print(ex[i // 10])