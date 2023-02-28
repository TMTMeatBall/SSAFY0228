def fn_d(n):
    # 각 자릿수를 더하는 과정
    # total = sum(map(int, str(n))) + n
    total = sum([int(i) for i in str(n)]) + n
    return total

def is_selfnumber(n):
    # fn_d함수를 사용해서 만들 수 없는 수다.
    for i in range(1, n + 1):
        if fn_d(i) == n:
            return False
    return True

print(is_selfnumber(1))
print(is_selfnumber(3))
print(is_selfnumber(5))
print(is_selfnumber(7))
print(is_selfnumber(9))
print(is_selfnumber(20))
print(is_selfnumber(31))
print(is_selfnumber(101))
print(is_selfnumber(102))


a, *b = 1, 2, 3, 4

a, b = {'name': '홍길동', 'phone': '010-0000-1111'}

