# deepcopy 구현하기
def my_deepcopy(x):
    new = None
    # immutable(불변형)일 때 바로 반환
    if type(x) not in (list, set, dict):
        return x
    # list인 경우
    elif type(x) is list:
        # 새로운 리스트를 하나 생성해서
        new = []
        # 요소를 하나씩 복사 (재귀적으로 진행)
        for item in x:
            new.append(my_deepcopy(item)) #재귀적으로 복사를 진행
    # set 인 경우
    elif type(x) is set:
        pass
    # dict인 경우
    elif type(x) is dict:
        pass
    return new


a = [1, 2, [3 ,[5, 6]]]
b = my_deepcopy(a)

a[2][1][1] = 10
print(b)