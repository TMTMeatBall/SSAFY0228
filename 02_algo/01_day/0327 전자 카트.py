#현재 위치 : now
#현재 위치까지 오는 데 사용한 배터리 양 :e_sum
def patrol(now,e_sum):
    #종료조건 모든방을 다 방문한 경우
    if 0 not in v:
        return
    #재귀 호출
    #현재 위치에서 갈 수 있는 다음 방을 선택함
    #갈 수 있는 다음 방을 어떻게 설정하는가?
    #내가 이전에 방문했던 방이 아니면 갈 수 없는 방
    for next_room in range(n):
        #다븡 방을 방문 한 적이 없고, 다음 방의 번호는 현재 방 번호와는 달라야 한다
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    # 이동하는 데 쓸 배터리 의 양
    e = [list(map(int, input().split())) for _ in range(n)]
    v = [0] * n
    v[0] = 1
    min_value = 10000
