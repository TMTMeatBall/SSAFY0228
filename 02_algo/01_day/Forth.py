T = int(input())
for tc in range(1,T+1):
    a = list(map(str,input().split()))

    stack =[]
    for i in a:
        if i == '.':
            if len(stack) == 1:
                print(f'#{tc} {stack.pop()}')
            else:
                print(f'#{tc} error')
        elif i.isnumeric():
            stack.append(int(i))
        else:
            if len(stack) < 2:
                print(f'#{tc} error')
                break
            elif len(stack) >=2:
                b = int(stack.pop())
                a = int(stack.pop())

                if i == '+':
                    stack.append(a+b)
                elif i == '-':
                    stack.append(a-b)
                elif i == '*':
                    stack.append(a*b)
                elif i == '/':
                    stack.append(a//b)

#1. 숫자는 스택에 넣는다
#2. 연산자를 만나면 스택에서 두 개를 뽑아서 연산한 후 결과를 스택에 다시 넣는다
#3. '.' 은 스택에서 숫자를 꺼내 출력한다
#4. 형식이 잘못되어 연산이 불가한 경우에는 'error'를 출력한다
#5. 피연산자와 연산자는 여백으로 구분되어 있다
#6. 나눗셈은 언제나 나누어 떨어진다
                # if str(a).isalpha() or str(b).isalpha():
                #     print(f'#{tc} error')