#입력 케이스가 10개로 고정
import sys
sys.stdin = open('input.txt','r')#시스템 내 내부 파일 참조 필요한 경우  open()메서드로 'input.txt' 파일을 'r' (read)함



for tc in range (1,11): #1~10

    #테스트케이스 1번줄에는 건물의 갯수가
    N = int(input())
    # b[i-2], b[i-1] () , b[i+1],b[i+2]
    #다음엔 건물들의 높이가
    buildings = list(map(int,input().split()))
    result=0
    # 빌딩을 순회한다. i : [2, N-2) 맨 왼쪽 오른쪽은 제외하므로
    for i in range(2, N-2):
    #     diff1 = buildings[i] - buildings[i-2]
    #     diff2 = buildings[i] - buildings[i-1]
    #     diff3 = buildings[i] - buildings[i+1]
    #     diff4 = buildings[i] - buildings[i+2]
    #     #높이차가 이 중에서 0초과일 경우에 조망권이 확보됨
    #     if diff1 > 0 and diff2 >0 and diff3>0 and diff4>0:
    #         result += min(diff1, diff2, diff3, diff4)
        mx = max(buildings[i-2],buildings[i-1],buildings[i+1],buildings[i+2])
        if buildings[i] >mx:



            result  += buildings[i] - mx
    print(f'#{tc} {result}')







