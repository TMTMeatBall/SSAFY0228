#첫 줄에 테스트 케이스 T가 주어진다
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
#N*N크기의 문자열에서 M크기의 회문을 찾기
    #1. N*N크기 문자열 보드 만들기
    # arr = [list(input()) for _ in range(N)] 이것과 이하의 arr2와의 차이는?
    # arr2 = [input() for _ in range(N)]
    #
    # print(arr[3][5])
    # print(arr2[3][5])
#zip 함수로 해결해보기
    arr2d = [list(input()) for _ in range(N)]
    z_arr2d = zip(*arr2d)
    print(arr2d)

    arr = ['e','y','e']
    if arr == reversed(arr):
        pass #회문판단에 reversed 메서드를 사용한 경우