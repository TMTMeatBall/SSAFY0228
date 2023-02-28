#1. 문자열을 전달 받아 해당 문자열의 모음 갯수를 반환하는 count_vowels 함수를 작성하시오.
# count_vowels('apple') #=> 2
# count_vowels('banana') #=> 3

# a=input('문자열을 입력: ')
# def count_vowels(string):
#     count=0 #카운트를 할 변수
#     #string -> 문자열을 하나씩 가져온다
#     for ch in string: 
#         if ch in 'aeiou':
#             count+=1
#     return count

print(count_vowels(a))


a='qwionsadvn;aowe;a'
def count_vowels(string):
    count=0
    for ch in string:#for 구분이므로 하나씩 쪼개서 다 넣는 것은 같다
        if ch in 'a''e''i''o''u':
            count+=1
    return count

print(count_vowels(a))