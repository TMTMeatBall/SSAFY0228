#후위표기법의 코드구현
string = input()
stack = []
result = []
for ch in string:
    if ch.isnumeric(): #string 을 도는 순간순간의 ch요소가 숫자인가? True;인 경우에는 바로 result 리스트에 append한다.
        result.append(ch)
    elif ch == '(':
        stack.append(ch)
    elif ch == '*' or ch == '/':
        #만약에 top에 이미 같은 우선순위의 연산자가 있다면, pop해준다.
        #그 후에 자기 자신은 stack 에 push
        if len(stack) > 0 and (stack[-1] == '*' or stack[-1] == '/') : #len(stack)>0 을 필수  조건으로 추가하는 이유는 idxerror를 방지하기 위함
            # and 에서 False여도 or 이 강제로 True로 보고 코드를 실행하고 있으므로 and의 TF여부에 따라 실행/실행하지 않음을 따라가도록 괄호를 넣어주자
            a = stack.pop()
            result.append(a)
        stack.append(ch)
    elif ch == '+' or ch == '-':
        # if len(stack) > 0 and stack[-1] == '-' or stack[-1] == '+':
        while len(stack) > 0 and stack[-1] in ['+', '-', '*', '/']:
            a = stack.pop()
            result.append(a)
        stack.append(ch)
    elif ch == ')': #else:
        #여는 괄호가 stack에 나올 때까지 pop한다
        while len(stack)>0 and stack[-1] != '(':
            a = stack.pop()
            result.append(a)
        a = stack.pop()
        result.append(a)
#stack 에 남아있는 연산자들을 모두 뺀다
while len(stack)>0:
    a = stack.pop()
    result.append(a)

print(*result)
# 중복되는 코드를 어떻게 해야 줄일 수 있을까
#각 토큰에 대해서 isp, icp를 이용한 딕셔너리 형태로 기록
for ch in string:
    #1. 피연산자의 지정
    if ch.isnumeric():
        result.append(ch)
    #2.닫는 괄호 ')'
    elif ch == ')':
        #여는 괄호'('가나올 때까지 pop해준다
        a=stack.pop()
        result

    else: # '-' '+' '*' '.' '('
        #우선순위가 현재 넣을 자신ch보다 같거나 높은 것을 stack 에서 제거
        while len(stack) > 0 and icp[stack[-1]] >= isp[ch]:
            a=stack.pop()
            result.append(a)
        #자기자신을 stack 에 넣어준다
        stack.append(ch)