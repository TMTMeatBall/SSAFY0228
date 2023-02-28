import sys
sys.stdin = open('input.txt','r')

def max_index(lst):
    max = lst[0]#빈 리스트에는 0을 넣어서 빈리스트를 만든다
    max_idx = 0
    for i in range(len(lst)):
        if max <lst[i]:
            max = lst[i]
            max_idx = i
    return max_idx
def min_index(lst):
    min = lst[0]
    min_idx = 0
    for j in range(len(lst)):
        if min > lst[j]:
            min=list[j]
            min_idx = j
    return min_idx

for tc in range(1,11):
    c = int(input())

    boxes = list(map(int,input().split()))
    for i in range(c):
        mx_idx = max_index(boxes)
        mn_idx = min_index(boxes)

        boxes[mx_idx] -= 1
        boxes[mn_idx] += 1
    print(f'#{tc} {max(boxes)-min(boxes)}')