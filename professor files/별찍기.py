# 전공자쪽에서 별찍기 반복문 연습

"""
*
**
***
****
*****
"""
for i in range(5): # [0, 5)
    for j in range(i + 1): # 1, 2, 3, 4, 5
        print('*', end='')
    print()

# 문자열 곱하기를 사용했을 때
# for i in range(5):
#     print('*' * (i+1))


"""
*****
****
***
**
*
"""
for i in range(5): # [0, 5)
    for j in range(5 - i): # 5, 4, 3, 2, 1
        print('*', end='')
    print()

"""
    *
   **
  ***
 ****
*****
"""
for i in range(5): # [0, 5)
    for j in range(5 - i): # 5, 4, 3, 2, 1
        print(' ', end='')
    for j in range(i + 1): # 1, 2, 3, 4, 5
        print('*', end='')
    print()

"""
  *
 ***
*****
 ***
  *
"""
for i in range(3): # [0, 3)
    for j in range(2 - i):
        print(' ', end='')
    for j in range(i * 2 + 1): # 1, 3, 5
        print('*', end='')
    print()

for i in range(2):
    for j in range(i + 1):
        print(' ', end='')
    for j in range(3 - i * 2): # 3, 1
        print('*', end='')
    print()