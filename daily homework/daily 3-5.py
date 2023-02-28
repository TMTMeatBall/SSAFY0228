# 반복문(for, while)이 동작하는 핵심 원리에 대해 이해한다. 조건문(if)이 동작하는 핵심 원리에 대해 이해한다.
# 문자열의 메소드와 슬라이싱을 사용하여 소금물을 구하는 프로그램을 만든다.
#  소금물의 퍼센트 농도와 소금물의 양을 입력하고, Done을 입력하면 혼합물의 퍼센트 농도와 양이 출력되도록 하시오. 
# 최대 5개의 소금물을 입력할 수 있다. 
# 출력된 혼합물의 퍼센트 농도와 양이 소수점 2자리를 넘어갈 경우, 반올림하여 2번째 자리까지만 나타내시오.

#1. 농도와 양
#2. Done이 입력 되기 전까지
#3. 소숫점 둘째자리까지만 출력하고 이후는 반올림
#4. 5개까지의 소금물을 입력하는 반복문

water_total=0
salt_total=0
text = input('소금물의 농도와 양을 입력:')
while text != 'Done':
    percent, amount = map(int, text.split())
    salt = amount * (percent/100)
    water = amount - salt

    salt_total += salt
    water_total += water
    text = input('소금물의 농도와 양을 입력:')

number = 0.005
print(f'number:{number:.2f}')

