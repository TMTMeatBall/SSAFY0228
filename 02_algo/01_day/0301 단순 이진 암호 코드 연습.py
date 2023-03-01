dic = {'0001101': 0,
       '0011001': 1,
       '0010011': 2,
       '0111101': 3,
       '0100011': 4,
       '0110001': 5,
       '0101111': 6,
       '0111011': 7,
       '0110111': 8,
       '0001011': 9,}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    bin_code = ''
    for i in range(N):
        for j in range(M - 1, 54, -1):
            if arr[i][j] == '1':
                bin_code = arr[i][j - 55:j + 1]
                break
        if bin_code != '':
            break
    decode = [0] * 8
    for i in range(8):
        decode[i] = dic[bin_code[i * 7:i * 7 + 7]]

    calc = sum(decode[0:8:2]) * 3 + sum(decode[1:8:2])
    result = 0
    if calc % 10 == 0:
        result = sum(decode)
    print(f'#{tc} {result}')

    # 1. 이 문제의 암호 코드란, 010101로 된 56자의 코드를 말함
    # 2. 56개 숫자를 받고, 7개씩 끊은 뒤에, 그것들을 저장한 자연수 딕셔너리로 변환한 후
    # 3. if 홀수자리합*3 + 짝수자리합 %10 ==0 : 면 올바른 코드
