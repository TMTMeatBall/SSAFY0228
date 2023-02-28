# arr 배열 안에 10 이하의 요소만 있는가를 파악하는 코드 작성
arr =[1,3,5,6,7,8,9]
# arr = list(input())
# cnt = 0
# for i in arr:
#     if i < 10 :
#         cnt += 1
# #cnt 변수와 arr 배열의 크기가 같다묜?
# if cnt == len(arr):
#     print('모든 요소는 10 미만이에요!')
# else:
#     print('요소 중에 10 이상인 값이 있네요!')


#2. 함수를 만들어서 체크하는 방법
#arr 배열을 순회하면서 10 이상의 값이 있다면 바로 False 를 반환하도록, 그렇지 않다면 True 를 반환하도록
# def check(arr):
#     for i in arr:
#         if i > 10:
#             return False
#
#     return True
#
# if check(arr):
#     print('다들 10 미만의 값!')
# else:
#     print('10 이상의 값이 있!음!')
#for~else문
#for 문이 (break)문이나 제어문에 의해 강제적으로 종료되지 않는 경우,
#정상적으로 종료된다면, else문의 코드 블럭을 실행!

for i in arr:
    if i > 10:
        break
else:
    print('10미만의 값만 존재')

print('코드 종료함!')