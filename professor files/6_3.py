# 1. 문자열을 전달 받아 해당 문자열의 
# 모음 갯수를 반환하는 count_vowels 함수를 작성하시오.
def count_vowels(string):
    count = 0 # 카운트를 할 변수
    # string -> 문자열을 하나씩 가져온다. 
    for ch in string:
        # 'aeiou'이 문자 안에 속한 알파벳이라면 카운트해라!
        if ch in ('a', 'e', 'i', 'o', 'u'):
            # 카운트를 1해준다.
            count += 1
    return count
            





result = count_vowels('hello') # 2
print(result)

