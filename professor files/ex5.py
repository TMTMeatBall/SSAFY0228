# 구구단 출력하기
for dan in range(2, 10): # [2, 10)
    for i in range(2, 10): # [2, 10]
        print(dan, 'x', i, '=', dan* i)
    print()

# x, y 정수가 주어졌을 때 짝수만 출력하기
x = 1
y = 100

if x % 2 != 0:
    x += 1

for i in range(x, y+1, 2): #[x , y]
    print(i)

# Q6. 1~100까지의 수 중에서 홀수와 홀수의 합을 실행 결과와 같이 출력하는 프로그램을 작성하시오. (1+3+5+...+99)
# 1+3+5+7+9+11+13+15+...=합

# hap = 0
# for i in range(1, 100, 2):
#     print(i, end='')
#     if i != 99:
#         print('+', end='')
#     else:
#         print('=', end='')
#     hap += i
# print(hap)

# print(*list(range(1, 100, 2)), sep='+', end='')
# print('=', end='')
# print(sum(range(1, 100, 2)))