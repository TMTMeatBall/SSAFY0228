string = '6528-*2/+' # -9

operators = {
    '*' : lambda a, b: a*b,
    '/' : lambda a, b: a/b,
    '+' : lambda a, b: a+b,
    '-' : lambda a, b: a-b,
}
#스택변수
stack =[]

#후위 표현식의 문자열을 순회
for ch in string:
    #1. 피연산자(숫자)를 만난다면 stack에 push
    if ch.isnumeric():
        stack.append(ch)
    #2. 연산자를 만난다면 stack에 있는 값을 2개 pop하고 연산을 진행
    else:
        b = int(stack.pop())
        a = int(stack.pop())
        c = operators[ch](a,b)
        stack.append(c)

#stack에 단 하나 남는 요소가 결과값이 될 것
result = stack.pop()
print(result)