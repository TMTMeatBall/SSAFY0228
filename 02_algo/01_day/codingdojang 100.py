#61

# for i in range(5):
#     for j in range(i+1):
#         print('*',end='')
#     print()
#62
# for i in range(5):
#     for j in range(i+1):
#         print(' ',sep='*' ,end='')
#     print()
#66
input('하나의 문자열을 입력하세요:')
result =[]
for i in range(len(input())):
    if i != 'a':
        result.append(i)
    else:
        continue

    print(result)

