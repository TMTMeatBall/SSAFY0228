import sys
sys.stdin= open('input.txt','r')

def max_index(lst):
    mx = lst[0]
    mx_idx = 0
    for i in range(len(lst)):
        if mx < lst[i]:
            mx = lst[i]
            mx_idx = i
    return mx_idx

def min_index(lst):
    mn = lst[0]
    mn_idx = 0
    for i in range(len(lst)):
        if mn > lst[i]:
            mn = lst[i]
            mn_idx = i
    return mn_idx

for tc in range(1,11):
    #입력
    c= int(input())
#1
    boxes = list(map(int,input().split()))#상자들의 높이 리스트
    #처리
    #for i :[0,덤프수)
    for i in range(c):
    #최댓값 상자의 인덱스
        mx_idx = max_index(boxes)
    #최솟값 상자의 인덱스
        mn_idx = min_index(boxes)
    #최댓값 -1 최솟값 +1
        boxes[mx_idx] -=1
        boxes[mn_idx] +=1
    #출력
    #최대최소 찾고 값의 차를 출력
    print(f'#{tc} {max(boxes)-min(boxes)}')
# #2
#     #로직
#     #박스 리스트를 sort()오름차순으로 정렬
#     boxes.sort()
#     #최좌측은 최소 최우측은 최대
#     # boxes[0],boxes[-1]
#     for i in range(c):
#         boxes[0] +=1
#         boxes[-1] -= 1
#         boxes.sort()
#     #출력
#     print(f'#{tc} {boxes[-1] - boxes[0]}')
