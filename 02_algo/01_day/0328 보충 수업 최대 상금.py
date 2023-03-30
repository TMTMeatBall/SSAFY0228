#우승하면 최대 상금을 받는다.
#주어진 횟수만큼은 교환해야 한다.
#순열로 띄우고, 교환식으로 나가다가. 횟수가 끝난 시점에서 가장 큰






T = int(input())

def perm(cnt):
    global answer
    #교환횟수가 끝난 시점에서 최대 상금을 구하기
    if cnt == change:
        max(answer,int("".join(num)))
        return


#재귀
#교환횟수 남았으면 바꿔줌
#동일위치 교환도 가능함
#교환위치 2개를 계속 정해줘야 한다
#앞은 i, 뒤는 j 로 놓고 해보자
    for i in range(len(num)-1):
        for j in range(i+1,len(num)):
            #자리를 바꿔보기
            num[i],num[j] = num[j],num[i]
            #자리바꾼 상태로 다음 자리 바꾸러 가보기
            perm(cnt+1)
            num[i],num[j] = num[j],num[i]


for tc in range(1,T+1):
    num,change = input().split()
    num = list(num)
    change = int(change)
    #순열 구할때 경우 수는 자리 바꿀 시에 문자열의 길이만큼만 바꾸면 모든 경우 수를 다 구할 수 있다
    #교환 횟수가 문자열의 길이보다 클 때에 굳이 더 진행필요 업ㅈㅅ다
    #문자열 길이만큼 교환하고, 남은 교환횟수가 짝홀
    if change > len(num):
        if change
        if 씨발! 존나못해먹겠내! 왜케이해가안대애애앵애애애애앵
        #남은 횟수가 홀수, 남은 횟수가 짝수

    answer = 0
    perm(0)
    print(f'#{tc} {answer}')
#교환횟수 cnt == 제시된 교환수 변수와 같아진 시점에서 종료조건