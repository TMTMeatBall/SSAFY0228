#두 개의 문자열 str1 과 str2
#문자열 2 안에 문자열 1과 일치하는 부분이 있다면 1 없다면 0을 반환한다
#첫 줄에 테스트 케이스의 갯수 T가 주어진다
T = int(input())
for tc in range(1,T+1):

    N = input()
    M = input()

    result = 0
    def isinside(N,M):

        if N in M:
            return 1
        else:
            return 0

    print(f'#{tc}', isinside(N,M))