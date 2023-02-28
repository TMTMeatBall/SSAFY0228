
count = 0
def VLR(t):  # 이 VLR 함수 작성 이유? value left right ->전위순회

    global count  # 전역변수 count가 전역에서도 적용되게 하기 위한 코드
    if t != 0:
        count += 1
        VLR(left[t])  # t값은 부모노드 left[t]는 부모의 좌측 자식노드값
        VLR(right[t])  # 부모노드 t 에 관한 우측 자식노드값
    # return count 보통 return count 적어두는게 맞지만, 전역변수로 선언했으므로, 이하의 line[36:38]의 출력방식을 택한다면, return count 없이도 가능하다
    #이상은 자기를 호출하면서 반복하는 재귀 함수
# VLR(3)  # 부모노드 값 3에 대한 left 또는 right 값
# print(count)  # 잘 세어지는지 확인


T = int(input())
for tc in range(1,T+1):
    E, N = map(int, input().split())  # 노드 N을 루트 노드로 하는 간선E
    arr = list(map(int, input().split()))
    left = [0 for _ in range(E+2)]
    right = [0 for _ in range(E+2)]  # 맨 첫 인덱스를 0으로 받아야 노드(1부터 시작하는)와 같이 번호를 쉽게 매길 수 있다.

    for i in range(0, len(arr), 2):  # arr에서 하나 걸라 하나씩 받아야 하므로 step을 2로,0번이 있는 리스트로 받으면서 1의 루트 노드는 좌,우 자식노드
        # 를 0으로 받기 위해 맨 첫 인덱스를 0으로 받고 1부터 시작하기위해

        parent = arr[i]  # arr이 부모-자식 구조로 입력되는 번호쌍으로 이뤄져 있음

        child = arr[i + 1]  # 부모idx값 +1 은 자식 array에서 받는다

        if left[parent] == 0:
            left[parent] = child
        else:
            right[
                parent] = child  # 이게 가능한 이유가, 언제나 순서쌍으로 받고 있기 때문에, 1 3 1 6으로 받으면 처음 3은 죄측에 자식 노드로, 이후에 6은 좌측에 3 있으므로 우측 자식 노드로 6이 들어간다
    count = 0 #함수 VLR이 전역변수count 를 받을 떄에 매번 초기화를 할 필요 있음(안하면 값이 계속 누적될 것)
    VLR(N)
    print(f'#{tc} {count}')
    #print(f'#{tc} {VLR(N)}')의 형태와, count 가 전역 변수이므로, 함수를 돌면서 이미 값이 변했으므로, count 를 누적한 함수를 호출하는 것만으로도, count값이 변하고,
    #이상과 같이 호출하면 똑같이 답을 반환받을 수 있다. line[36,38]
    # count = 0
    #
    #
    # def LRV(t):  # 후위순회
    #     global count
    #     if t != 0:
    #         LRV(left[t])
    #         LRV(right[t])
    #         count += 1



    #dfs bfs 형식 탐색을 가능하지만, 이진트리 형태의 탐색 (전중후) 재귀형태/결과적으로 두 과정이 크게 차이는 없다
