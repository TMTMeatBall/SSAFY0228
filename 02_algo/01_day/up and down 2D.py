T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    peaks = []
    result = 0
    for i in range(1, N - 1): #제일 중요한 것. N범위가 가장자리를 포함하지 않게 하는 방법
        for j in range(1, N - 1):  # 8방향의 좌표정보

            if arr[i][j] > arr[i - 1][j - 1] \
                    and arr[i][j] > arr[i - 1][j] \
                    and arr[i][j] > arr[i - 1][j + 1] \
                    and arr[i][j] > arr[i][j - 1] \
                    and arr[i][j] > arr[i][j + 1] \
                    and arr[i][j] > arr[i + 1][j - 1] \
                    and arr[i][j] > arr[i + 1][j] \
                    and arr[i][j] > arr[i + 1][j + 1]:
                peaks.append(arr[i][j])

    if len(peaks) == 0 or len(peaks) == 1:
        result = -1
    else:
        peaks.sort() #sorted 사용 원하면 a = sorted(peaks)로 변수 지정해야 함
        result += abs(peaks[0] - peaks[-1])

    print(f'#{tc} {result}')

# 한 구역을 중심으로 8방으로 높은 경우에만 산의 정상으로 취급
# 가장자리는 정상으로 취급하지 않는다.
# 산이 하나 이하인 경우 -1을 출력하도록 한다.
# arr = [0 for _ in range(N)]
# for i in range(N):
#     arr[i] = list(map(int,input().split()))
#
# arr = []
# for i in range(N):
#     arr.append(list(map(int,input().split())))
