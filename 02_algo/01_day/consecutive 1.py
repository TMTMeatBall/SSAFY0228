# N개의 0과 1로 이뤄진 수열에서 연속한 1의 갯수 중 최대값을 출력하는 프로그램을 작성
# 첫 줄은 테스트 케이스 T
T = int(input())
for tc in range(1,T+1):

    #다음 줄은 수열의 길이 N
    N=map(int,input().split())
    #그 다음 줄은 수열이 공백없이 제공됨
    arr = list(map(int,input().split()))

    def consecutive1(arr):
        max_count = 0
        count = 0
        for i in range(0,len(arr)-1):
            if arr[i] = arr[i+1]:
                count += 1
            else:
                if max_count <count:
                    max_count = count
                    count = 0

