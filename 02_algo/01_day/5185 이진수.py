T = int(input())
interpreter = {'A': '10', 'B': '11', \
               'C': '12', 'D': '13', \
               'E': '14', 'F': '15'}

for tc in range(1, T + 1):
    N, hex_num = input().split()

    result = ''

    for i in hex_num[::-1]:
        if i in interpreter:
            i = interpreter[i]

        i = int(i)

        for _ in range(4):
            result = str(i % 2) + result
            i //= 2
    print(f'#{tc} {result}')
# for t in range(1, int(input()) + 1):
#     a, b = input().split()
#     print(f'#{t} {bin(int(b, 16))[2:]:0>{len(b) * 4}}')


# T = int(input())
# for tc in range(1,T+1):
#     N = float(input())
#     result = ''
#     #소수점을 이진수로?
#     #소수부에 2를 곱해서 그 결과가 1로 떨어질 때까지 반복
#     while !=
