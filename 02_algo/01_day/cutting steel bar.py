T = int(input())
for tc in range(1,T+1):
    a = list(input())
    stack = []
    cnt = 0
    for i in range(len(a)): #i 가 리스트로 받은 인풋을 돌면서
        if a[i] == '(': #열린 괄호를 찾은 경우에
            stack.append('(') #stack에 추가하고
        elif a[i] == ')':#닫힌 괄호를 찾은 경우에는,
            if a[i-1] == '(':#바로 앞의 것이 열린 괄호면 (레이저)
                stack.pop() #가장 마지막 stack 요소를 pop 해서 삭제하고
                cnt += len(stack) #stack의 요소들 수(막대기)만큼 cnt에 더한다
            else:
                stack.pop()#닫힌 괄호의 바로 앞의 것도 닫힌 괄호인 경우에는(다른 막대기)
                cnt += 1#막대기 조각 +1
    print(f'#{tc} {cnt}')

