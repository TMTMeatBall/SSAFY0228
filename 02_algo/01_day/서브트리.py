# 주어진 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 갯수를 알아내는 프로그램을 작성
# 1. 부모가 없는 노드가 전체의 루트 노드가 된다
# 2.
N = int(input())
left = [0 for _ in range(N + 1)]  # == [0]*(N+1)
right = [0 for _ in range(N + 1)]

# 부모-자식
arr = list(map(int, input().split()))

# 부모 자식을 순회한다
for i in range(0, len(arr), 2):
    # 부모 i, 자식 i+1
    # 왼쪽 지식이 있는지 여부 -> 없으면 왼쪽, 있으면 오른쪽
    p = arr[i]
    c = arr[i + 1]

    if left[p] == 0:
        left[p] = c

    else:
        right[p] = c

# 카운트 변수 (전역)
count = 0


# 순회
def VLR(t):
    global count  # 해야 전역변수인 cnt가 에러나지 않는다
    if t != 0:
        count += 1
        VLR(left[t])  # 왼쪽
        VLR(right[t])  # 오른쪽


VLR(3)
print(count)

count = 0


def LVR(t):
    global count
    if t != 0:
        LVR(left[t])
        count += 1
        LVR(right[t])

LVR(3)
print(count)

count = 0
def LRV(t):
    global count
    if t != 0:
        LRV(left[t])
        LRV(right[t])
        count += 1

LRV(3)
print(count)
