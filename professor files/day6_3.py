def count_vowels(text):
    count = 0 # 문자열의 모음 갯수
    # text의 문자를 하나씩 순회 가져온다
    for t in text:
    # 'aeiou' 이 안에 속한 문자라면 
        if t in 'aeiou':
            count += 1 # 카운트 +1
    return count

print(count_vowels("yellow"))