def sum(x, y): #새로운 함수를 정의
    # return 매개변수1 + 매개변수2
    return x + y, x, y

result, _ = sum(2, 3)

print(result)
# 단순히 "hello"를 출력하는 함수, (반환값 없음)
def greeting():
    print("hello")

for i in range(4):
    greeting()


# a에 10을 더하는 함수
def sum10(a):
    return a + 10

print(sum10(5))
# a와 b를 더하는 함수
def sum2(a, b):
    return a + b

print(sum2(2, 3))

# a와 b를 스왑해서 반환해주는 함수
def swap(a, b):
    return b, a

x = 10
y = 7
print(x, y)

x, y = swap(x, y)

print(x, y)

# 리스트가 주어지면 그 리스트의 평균을 반환하는 함수
grade = [1,2,3,4,5,6]

def average(a):
    return sum(a) / len(a)

print(average(grade))
