numbers = [4,4,7,8,10,4]

# sum_of_reqeat_number(numbers) 함수 작성
# 리스트 안에 하나만 있는 숫자만 합산을 해서 반환

def sum_of_repeat_number(numbers):
    numbers_dict = dict()
    for number in numbers:
        numbers_dict.setdefault(number, 0)
        numbers_dict[number] += 1

    # 키-값 쌍 중에 값(카운트) 1인 키만을 다 더한다.
    total = 0
    for key, val in numbers_dict.items():
        if val == 1:
            total += key
    
    return total

print(sum_of_repeat_number(numbers))