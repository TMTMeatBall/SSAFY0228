
# 삽입 (enqueue)
def enqueue(item):
    # 완전 이진 트리... 맨 마지막에 값을 추가...
    global hsize
    hsize += 1
    H[hsize] = item


    c = hsize
    p = c // 2

    # 힙(heapify)의 형태... 자리바꾸기...
    while p and H[p] > H[c]:
        H[p], H[c] = H[c], H[p]
        c = p
        p = c // 2

# 삭제 (dequeue)
def dequeue():
    global hsize
    # 루트 노드에서 값을 뺀다.
    tmp = H[1]
    # 마지막에 넣었던 노드를. 해당 루트 노드 위치로 넣어준다.
    H[1] = H[hsize]
    hsize -= 1

    # 자리바꾸기를 진행....

    p = 1
    c = p * 2 # 왼쪽 자식먼저...

    while c <= hsize:
        # 왼쪽 자식과 오른쪽 자식을 비교해서 더 작은 값 선택해서
        if H[c] > H[c + 1]: #오른쪽 자식을 교체 대상...
            c += 1
        if H[p] > H[c]: # 부모 자식을 비교
            H[p], H[c] = H[c], H[p]
            p = c
            c = p * 2
        else:
            break

    # 원래 있던 루트 노드 반환
    return tmp
#
#
H = [0] * 101 # 힙
hsize = 0 # 힙의 사이즈

enqueue(10)
# print(H[1:hsize+1])
enqueue(20)
# print(H[1:hsize+1])
enqueue(30)
# print(H[1:hsize+1])
enqueue(40)
# print(H[1:hsize+1])
enqueue(50)
# print(H[1:hsize+1])
item = dequeue()
print(item)
print(H[1:hsize+1])
item = dequeue()
print(item)
print(H[1:hsize+1])
item = dequeue()
print(item)
print(H[1:hsize+1])
item = dequeue()
print(item)
print(H[1:hsize+1])


# random 값까지
# import random
# # heapq 를 사용해서 min-heap 최소힙... (함수)
# from heapq import heapify, heappop, heappush
#
# pq = [random.randint(1, 101) for _ in range(10)]
# heapify(pq) # pq 요소는 최소힙에 맞게 정렬...
# print('pq:', pq)
#
# item = heappop(pq)
# print('item pop', item)
# print('pq:', pq)
#
# heappush(pq, 50)
# print('pq:', pq)