#별 찍기 문제의 핵심은 한 줄씩, 빈 칸이 몇 개이며 별은 몇 개인지를 파악하는 게 우선

for i in range(5): # [0, 5)
    for j in range(i + 1): # 1, 2, 3, 4, 5
        print('*', end='')
    print()


for i in range(5): #[0,5)
    for j in range(5-i):
        print('*', end='')
    print()


for i in range(5):
    for j in range(4-i):
        print(' ',end='')
    for i in range(i+1):
        print('*', end='')
    print()
    ##고치기

for i in range(3):
    for j in range(2-i):
        print(' ', end='')
    for i in range(i*2+1):
        print('*',end='')
    print()

for i in range(2):
    for j in range(i+1):
        print(' ',end='')
    for i in range(3-i*2):
        print('*',end='')
    print()
#예제1
for i in range(6):
    for j in range(5-i):
        print(' ',end='')
    for i in range(2*i-1):
        print('*', end='')
    print()

#예제2
for i in range(6):
    for j in range(5-i):
        print(' ', end='')
    for i in range(2*i-1):
        print('*', end='')
    print()

for i in range(6):
    for j in range(i):
        print(' ',end='')
    for i in range(9-2*i):
        print('*', end='')
    print()

#예제3
for i in range(6):
    for j in range(i):
        print(' ', end='')
    for i in range(9-i*2):
        print('*',end='')
    print()

for i in range(4):
    for j in range(4-i):
        print(' ',end='')
    for i in range(3+2*i):
        print('*',end='')
    print()


#밑줄이 1부터 시작하는 코드

for i in range(4):
    for j in range(i):
        print(' ',end='')
    for i in range(9-2*i):
        print('*', end='')
    print()
for i in range(5):
    for j in range(4-i):
        print(' ',end='')
    for i in range()

for i in range(3):
    for j in range(5):
        print('*', end='')
    print()

# print(('*'*n + '\n'))

name = 'kim'
score = 4.5
print(f'helo,{name}! 성적은 {score+3}')

5, 3 = map(int, input().strip().split(' '))
answer = ('*'*5 +'\n')*3
print(answer)



n = 4
m = 5


print((('*')*n + ('\n'))*m, end=3*'\n\n\n')

n = 4
m = 5


print((('*')*n + ('\n'))*m)