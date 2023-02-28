'''
10
5 10
0000000000
0123456789
0000000000
0000000000
0000000000
'''
t = int(input())
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]  # 공백이 잘려나가니까 split()안씀

print(T)
print(N, M)
print(f'{N} {M}')
print('%d %d' % (N, M))
print('{} {}'.format(N, M))

for i in range(N):
    for j in range(M):
        print(arr[i][j], end='')
    print()

for i in range(N):
    print(*arr[i], sep='')

import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
input().split  # 한 줄 입력 받아서 공백 기준으로 나누고, 정수로 형식 변환

'''
1,13
0000000111 100000110 0000011110 0110000110 0001111001 1110011111 
'''
input().split()  # ['0000000111' ...
for s in input().split():
    # s = s[:: -1]  # '1110000000'
    # hap = 0
    # # 문자열을 순회하면서 1에 대한 값을 발견하면, 합 +=2 ** 자릿수
    # for idx in range(len(s)):
    #     if s[idx] == 1:
    #         hap += 1 << idx

    # print(hap,end=' ') #1
    # result = int(s,2) #2
    # result = int(s) #3
    # result = bin(result)#3

    print(format('%b',int(s))) #4


hex_tabe = '0123456789ABCDEF'
result = ''
for ch in string:
    digit = hex_table.find(ch) #문자 하나를 십진수로
    #십진수 -> 이진수(네자리)
    for i in range(4):
        digit,mod = divmod