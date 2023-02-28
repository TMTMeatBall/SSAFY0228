# # 목표 - 전중후위 순회를 작성하기
def LVR(v):
    # 재귀로 호출하기
    if v:  # v값이 0이 아닌 때에, or if v > 0:
        LVR(left[v])
        print(visit[v], end='')
        LVR(right[v])


def VLR(v):
    if v:
        print(visit[v], end='')
        VLR(left[v])
        VLR(right[v])


def LRV(v):
    if v:
        LRV(left[v])
        LRV(right[v])
        print(visit[v], end='')


# N = int(input())
# visit = [0] * (N + 1)  # visit
# left = [0] * (N + 1)
# right = [0] * (N + 1)
# 전위는 VLR
# 중위는 LVR
# 후위는 LRV
# (1) 이진 트리를 중위 순회하면서, 방문한 정점의 이름을 출력하는 유사코드를 완성하라
# 방문한 정점, v(정점),vleft,vright로 표현하면서 각 행에 주석 형식으로 간단한 설명을 첨가한다
# (2) 다음의 트리를 정점 A부터 전위순회할 때에, 정점의 방문순서는 다음과 같다.ABCDE 루트노드인 A부터 중위순회,후위순회했을 경우의
# 결과값을 출력하시오
# LVR =
T = 1
for tc in range(1, T + 1):  # 10개 케이스
    N = int(input())  # node 의 갯수
    left = [0] * (N + 1)  # 좌측 자식노드
    right = [0] * (N + 1)  # 우측 자식노드
    visit = [0] * (N + 1)  # 데이터의 visit판단 이상이 선VLR 중LVR 후LRV따지는 1차원 배열
    for _ in range(N):
        arr = list(input().split())  # arr은 번호에 따라 부여된 해당 노드의 값을 N만큼 돌면서 띄운다

        p = int(arr[0])  # p는 그런 돌고 있는 매 경우의 arr에서의 부여된 노드번호를 받는다

        ch = arr[1]  # ch는 돌고 있는 매 경우의 arr에서의 부여된 노드의 특정값을 받는다
        visit[p] = ch  # 방문했을 때의 노드번호에서의 visit값이 해당 특정값으로 저장하는 것으로
        # visit의 인덱스값=해당 노드인덱스에서의 노드 부여값
        if len(arr) == 4:  # [정점번호,정점정보,죄측자식노드,우측자식노드]
            # 좌측 자식노드 우측 자식노드 모두 받은 arr순회의 특정 경우에,
            left[p] = int(arr[2])
            right[p] = int(arr[3])
        elif len(arr) == 3:
            left[p] = int(arr[2])

    print(f'#{tc}', end='')
    LVR(1)  # 루트노드의 노드번호값인 1에서의 출력값을 낸다.
    print()
    VLR(1)
    print()
    LRV(1)
    print()