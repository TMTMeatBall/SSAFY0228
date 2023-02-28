# [0] q, visited 및 필요변수를 만든다
# 1238. Contact
# 연락 시작하는 사람의 정보를 제공
# 가장 나중에 받는 사람 중 번호가 가장 큰 사람
# bfs : 가장 마지막 큐에서 꺼낸
# 그림 배열 정보를 통해 시작 지점으로부터 얼마나 떨어져 있는지를 기록할 필요 있슴
# queue v에 필요한 flag를 생성하고
# queue 초기데이터를 삽입, v 표시하고 필요처리함
# while q:
# q에서 한개를 꺼냄
# if v[ans] < v[c] or v[ans] == v[c]
# and ans<c
# 4방향/8방향/미방문 *조건이 맞았을 때에,
# q삽입,v표시
# 템플릿을 지키고, 조건에 따른 확산을 필요에 따라 확인
# while부분에서 변경하면서 조건을 맞춰 준다
def bfs(s):
    # [0] q, v 필요 flag의 생성
    q = []
    v = [0] * 101
    ans = s
    # [1] queue 에 초기데이터 삽입, v표시
    q.append(s)
    v[s] = 1
    while q:
        c = q.pop(0)  # queue니까 가장 앞에서 꺼냄
        # [2] q에서 한개 꺼냄 + 필요시 정답처리
        if v[ans]<v[c] or v[ans] == v[c] and ans<c:
            ans = c

        # [3] 4/8방향 연결 등의 반복처리
        for n in adj[c]:
            if v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1
    return ans


T = 10
for tc in range(1, T + 1):
    N, S = map(int, input().split())
    a = list(map(int, input().split()))
    # 인접리스트의 연결상태 저장 필요
    adj = [[] for _ in range(101)]
    # 0번 인덱스는 비운다(bfs의 노드 번호의 최초값이 1번이므로)
    for i in range(0, len(a), 2):
        s, e = a[i], a[i + 1]
        adj[s].append(e)

    ans = bfs(s)
    print(f'#{tc} {ans}')