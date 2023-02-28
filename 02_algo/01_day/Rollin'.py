T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split()) #N = 요소 M = 회전수
    arr = list(map(int,input().split()))
    #회전수 M에 대해서 앞 -> -> 뒤 요소를 넣는 코드를 작성...
    rear = M % N #rear 의 결과부터 출력하면 된다!
    print(arr[rear])
