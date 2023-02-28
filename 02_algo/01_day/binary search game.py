def binary_search(arr, P, key):
    count = 0
    start = 1  #0
    end = P    #1
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == key:
            count += 1
            return count
        elif arr[middle] > key:
            count += 1
            end = middle
        else:
            start = middle
            count += 1
    return count
#왜 start = middle +1 이 아니고 왜 end = middle -1 이 아닐까?
#위의 문제의 start=middle, end=middle 의 경우에는 start = 0,end =1 인 경우에 무한 루프가 생기는 경우가 발생한다..
#이것을 해결하기 위해서 보통 start = middle +1 , end = middle-1을 적용하는 것인데, 이 경우는 특별하게 그런 루프가 발생하지 않도록 start 와 end를 지정하고 있다.
# #책의 전체 쪽수/두 사람이 찾을 쪽 번호/이진탐색/누가 먼저 찾는가?
# #첫 줄에 테스트 케이스 갯수 T가 주어진다
T = int(input())
for tc in range(1,T+1):
    #테스트 케이스 별로 책의 전체 쪽 수 P,A,B, 찾을 쪽 번호 Pa,Pb가 주어진다
    P, Pa, Pb = list(map(int,input().split()))
    a = [x for x in range(P)]

    def result():
        if binary_search(a, P, Pa) < binary_search(a, P, Pb):
            return 'A'
        elif binary_search(a, P, Pa) > binary_search(a, P, Pb):
            return 'B'
        else:
            return '0'

    print(f'#{tc} {result()}')
