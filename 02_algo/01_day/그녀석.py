import heapq

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    heap = []
    arr = list(map(int, input().split()))
    for data in arr:
        heapq.heappush(arr, data)

    # 배열의 직접 구현시에는 0번 인덱스를 쓰지 않기 위해 N+1 등의
    # 추가 조작을 했다
    heap.insert(0, 0)  # 으로 0번 인덱스에 0을 넣어준다
    hap = 0  # 누적합(hop)
    # 마지막 노드부터 위의 조상노드를 탐색하는 과정
    t = len(heap) - 1
    t //= 2
    while t >= 1:
        hap += heap[t]
        t //= 2 #부모 노드로 올라간다

    print(f'{tc} {hap}')