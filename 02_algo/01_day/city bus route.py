#5천개의 버스 정류장에 1~5000까지 번호가 지정되어 있다
# 버스 노선은 N개, i 번째 버스 노선은 번호가 Ai 이상이고 Bi이하인 모든 정류장만을 다닌다.
#P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하는 프로그램을 작성
#1번 줄에는 테스트 케이스의 갯수가
#2번 줄에는 첫 번째 테스트 케이스의 노선 갯수 정수N이
#다음 N개의 줄에는 번호 Ai와 Bi가 공백 하나로
#
# import sys
# sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    counts = [0]*5001 #0으로 이뤄진 리스트를 만들고, 이것을 for문을 통해서 인덱싱한다
    for _ in range(N):
        #다음 N개의 줄의 i번쨰 줄에는 두 정수 Ai,Bi가 공백을 통해 제공됨
        Ai, Bi = map(int, input().split())
        for j in range(Ai, Bi+1):
            #counts의 해당 인덱스에 1씩 추가
            counts[j] += 1
    P = int(input())
    #Cj번 버스 정류장을 지날 노선 개수를 추가할 빈 리스트가 필요함
    blanklst = []
    for j in range(P):
        Cj = int(input())
        blanklst.append(counts[Cj])
    result = ' '.join(map(str,blanklst)) #결과값이 1 2 2 1 1 으로 각 공간이 비어있음
    print(f'#{tc} {result}')
#[1] N번 반복하면서 노선입력, 빈도수
