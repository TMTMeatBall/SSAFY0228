#버스 노선의 일반 광역 급행 구분
#모든 정류장은 1~1000번호
#A~B까지의 운행 반드시 시작,종점에는 정차
#급행은 A가 짝수인 경우, 모든 짝수 번호에 정차하고, A가 홀수라면 A,B사이의 모든 홀수 역에 정차
#광역급행은 A가 짝수인 경우에 4의 배수에, A가 홀수라면 A,B사이의 3의 배수이면서 10의 배수가 아닌 번호 정류장에 정차
#버스 종류, 출발, 도착 정류장에 대한 정보가 있을 때, 최대 몇 개의 노선이 같은 정류장에 정차하는가? 알아볼 수 있는 프로그램
#첫 줄은 테스트케이스
#2줄은 노선의 수
#N개의 줄에 걸쳐  버스타입(1.일반,2.급행,3.광역급행) 과 각 버스의 출발 정류장 번호A 종점 정류장 번호B가 빈칸으로 구분되어 주어진다.
T= int(input())
for tc in range(1,T+1):
    N = int(input())
    bus_lst = [0]*1001 #빈 리스트 쓸 때 안에 넣을 요소를 적어주기
    for i in range(1,N+1):
        bus, stst, edst = map(int,input().split())
        if bus == 1:
            for j in range(stst,edst+1):
                bus_lst[j] += 1
        elif bus == 2:
            for k in range(stst,edst+1):
                if stst % 2 == 0 and k % 2 == 0:
                    bus_lst[k] += 1
                if stst % 2 != 0 and k % 2 != 0 :
                    bus_lst[k] += 1
        elif bus == 3:
            for l in range(stst,edst+1):
                if stst % 2== 0 and l % 4 ==0:
                    bus_lst[l] +=1
                if stst % 2 != 0 and l%3==0 and l% 10 !=0:
                    bus_lst[l] += 1

    print(f'#{tc} {max(bus_lst)}')