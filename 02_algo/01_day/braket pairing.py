for tc in range(1,11):
    N = int(input())
    a = input().split()
    stack = []
#인풋을 받다가 닫는 형태가 나온 순간, 스택에서 싹 다 pop 해서 빼주고, 다시 스택에 넣어서
#다시 쭉쭉쭉