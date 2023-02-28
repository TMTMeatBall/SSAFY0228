for tc in range(1,11):
    length = int(input())
    arr = [[0 for j in range(8)] for i in range(8)]
    result = 0
    #열은 가로를 나누는 세로줄, 행은 세로를 나누는 가로선 10행 5열은 5*10 column = 5, row = 10
    #가로
    for i in range(0,8):
        for j in range(0,8-length+1):
            if arr[i][j:j+length] == arr[i][j:j+length][::-1]:
                result += 1

    #세로
    for i in range(0,9-length):

        for j in range(0,8):
            #세로로 뽑아낸 요소들을 넣어줄 변수 생성
            sero = ''
            for k in range(length):
                sero += arr[k+i][j]
            if sero == sero[::-1]:
                result += 1

    print('#{tc} {result}')