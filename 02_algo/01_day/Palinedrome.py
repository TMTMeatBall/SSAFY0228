#첫 줄에 테스트 케이스 T가 주어진다
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
#N*N크기의 문자열에서 M크기의 회문을 찾기
    #1. N*N크기 문자열 보드 만들기
    arr = [list(input()) for _ in range(N)]

    palindrome=[]
    for i in range(0,N):#행
        for j in range(0,N-M+1):#열
            # char = ''
            # for cj in range(j,j+M):
            #     char += arr[cj][i]
            # if char == char[::-1]:
            #     palindrome.append(char)
            if arr[i][j:j+M] == arr[i][j:j+M][::-1] and len(arr[i][j:j+M])==M: #i행의 j열부터 회문M만큼의 범위로 잡힌 구문이, 그 역순과 같다면,
                palindrome = arr[i][j:j+M] #palindrome 리스트에 추가. 이것은 가로 회문을 의미
                #palindrome.append(arr[i][j:j+M]) 경우 arr 이 이미 리스트이므로, append해서 리스트 안의 리스트를 만들 이유는 없다.
    for j in range(0,N): #열
        for i in range(0,N-M+1):#행
            char = '' #char을 문자열로 놓고했으므로 join 메서드를 사용하지 않아도 결과물이 나쁘지 않다.
            for ci in range(i,i+M):
                char += arr[ci][j]
            if char == char[::-1]:
                palindrome.append(char)
            # if arr[j][i:i+M] == arr[j][i:i+M][::-1] and len(arr[j][i:i+M])==M: #거꾸로? 가 안ㄴ? 가?
            #     palindrome.append(arr[j][i:i+M])

    print(f'#{tc}', ''.join(palindrome))
#join 메서드가 에러를 뱉어낼 때