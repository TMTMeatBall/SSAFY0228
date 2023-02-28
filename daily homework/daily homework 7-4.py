

# Python에서 예외를 발생시키는 방법 이해
# i.          입력된 수가 짝수라면 2로 나눈다.  
# ii.          입력된 수가 홀수라면 3을 곱하고 1을 더한다.  
# iii.          결과로 나온 수에 같은 작업을 1이 될 때까지 반복한다.
# 예를 들어, 입력된 수가 6이라면 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 이 되어 총 8번 만에 1이 된다.위 작업을 몇 번이나 반복해야하는지 반환하는 함수 collatz()를 작성하시오 
# (단, 작업을 500번을 반복해도 1이 되지 않는다면 –1을 반환하시오.)

a=int(input('작업을 할 원하는 숫자를 입력: '))

def collatz(a):
    cnt=0
    while True:
        if a % 2 == 0:
            a=a/2
            cnt+=1             
        else:
            a=3*a + 1
            cnt+=1


        if a==1:
            break
        
        if cnt>500:
            return -1

    return cnt

print(collatz(a))


# a = 320
# count = 0
# while int(a) % 2 == 0:
#     count += 1
#     print('짝수일때 실행')
#     if count > 5:
#         break
# else:
#     print(a)

# print(collatz(6))

# collatz(6) #=> 8
# collatz(16) #=> 4
# collatz(27) #=> 111
# collatz(626331) #=> -1

