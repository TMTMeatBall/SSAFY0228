T = int(input()) #테스트케이스
for tc in range(1,T+1):
    K, N, M = map(int,input().split())
    station = list(map(int,input().split()))
    charge = 0 #충전수
    location = 0 #현위치
    while location + K < N:
    #이동거리 K 이동해도 종착역N에 닿지못할 경우를 True로 반복함
        for step in range(K,0,-1):
            #1차시에 이동가능거리K를 스텝 역순으로 0까지 갈 때에 그 범위 안에 충전소가있는지를 판단
            if location + step in station: # 1 2 3 in station
                charge += 1
                location += step#station위치를 받은 경우 station 리스트에서 뽑아내야 함
                break
        else: #이동해도 주유소가 없다면 step 이 이동하는 것에 대한 else임을 기억하기
            charge = 0 #충전수를 0으로 하고
            break


    print(f'#{tc} {charge}')
