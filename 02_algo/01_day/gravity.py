# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# [입력]
#
# 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
T = int(input())
for tc in range(1, T + 1):

    # 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 100 )
    N = int(input())
    # 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 100 )
    arr = list(map(int, input().split()))
    # 로직 처리
    # 9 <- N
    # 7 4 2 0 0 6 0 7 0 <- arr
    # 가장 큰 카운트 값을 가지는 변수
    mxCnt = -1
    # // 리스트의 인덱스 변수
    mxIdx = -1
    # 카운트 변수 cnt
    # cnt=0
    #  arr 리스트에서 인덱스 순회 i:0 -> N-1
    for i in range(N):
        cnt = 0
        # arr j : i+1 -> N-1
        for j in range(i + 1, N):
            if arr[i] > arr[j]:  # 카운트 1 증가
                cnt += 1
            if mxCnt < cnt:  # 가장 큰 인덱스 갱신
                mxCnt = cnt
                mxIdx = i
    #     arr
    # [출력]
    #
    # 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
    print(f'#{tc} {mxCnt}')
