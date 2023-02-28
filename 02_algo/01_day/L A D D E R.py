import sys
sys.stdin = open('input.txt','r')

for i in range(10):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    #10*10 크기 이차원 배열, 바닥까지 가장 짧은 이동거리를 갖는 시작점 x (복수인 경우 가장 큰x좌표)를 반환
#좌/우 를 만나면 무조건 방향을 꺾는다. 그 외엔 직진함


T = 10

arr =[]

si, cnt, dj = 0, 0, 0

ci, cj = si, sj
while ci < 99:








    if mn >= cnt:
