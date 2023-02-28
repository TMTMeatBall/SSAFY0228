# 49
# for i in range(1,12):
#     if i<11:
#         print(i)
#     else:
#         print('발사!')
# 50
# cnt = 0
# while cnt < 10:
#     cnt = cnt+1
#     print(cnt)
#     if cnt == 10:
#         print('발사!')
# 51
# a = int(input('카운트다운 몇 초 전인가요?'))
# k=''
# for i in range(a):
#     k = a-i
#     print(k)
#     if k == 1 :
#         print('발사!')
#         break
# 52
# a = int(input())
# sum = 0
# for i in range(a+1):
#     sum += i
#
# print(f'1부터 {a} 까지 모두 더한 합은 {sum}')
# 54
# a = int(input('숫자를 입력하세요 '))
# while a >= 0:
#     print(f'입력된 숫자는 {a}')
#     a = int(input('숫자를 입력하세요 '))#while 문의 반복을 막고 새로 인풋을 받게 한 경우 결과값이 계속 반복되지 않는다
# else:
#     print(f'종료합니다')
# 55
# print('1 2 3 4 5 6 7 8 9 10')
# 56
# a = int(input('첫 번째 숫자를 입력하세요'))
#
# b = int(input('두 번째 숫자를 입력하세요'))
# sum = 0
# result =[]
# if a >= b :
#     print(' ')
# else:
#     for i in range(a,b+1):
#         result.append(i)
#         sum = sum + i
#     print(*result, sep='+', end='')
#     print(f'= {sum}')
# 57
# a = int(input('첫 번째 숫자를 입력하세요'))
# b = int(input('두 번째 숫자를 입력하세요'))
#
#
# def evensum(x, y):
#     sum = 0
#     for i in range(x, y + 1):
#         if not i % 2:
#             sum += i
#     return sum
#
#
# print(f'{a}부터 {b}까지 짝수들만의 합은 {evensum(a, b)}')
# a = int(input('첫 번째 숫자를 입력하세요'))
# b = int(input('두 번째 숫자를 입력하세요'))
# sum = 0
# for i in range(a,b+1):
#     if i%2 == 0:
#         sum += i
# print(f'{a}부터 {b}까지 짝수들만의 합은 {sum}')
# 58
# result = []
# for i in range(1,5):
#     for j in range(4,8):
#         a = i+j
#         result.append(a)
# setresult = set(result)
# print(setresult)
# 59
# color = 256**3
# print(f'가능한 색깔 개수는 {color}')
# color = []
# for red in range(256):
#     for green in range(256):
#         for blue in range(256):
#             a = (red, green, blue)
#             color.append(a)
# colors = set(color) #set(lst)메서드는 lst안의 중복된 요소들을 모두 삭제하고
# #결과를 나열한다
# result = len(colors)
# print(f'가능한 색깔 개수는 {result}')
#60
# for j in range(4):
#     for i in range(4):
#         print('*',end ='')
#     print()
#61
