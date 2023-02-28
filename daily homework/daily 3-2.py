text = input('전달받을 문자열: ')
length = len(text)\
# len('문자열') : 문자열의 길이를 반환
# 짝수라면, 'abcd' -> 4//2 -> 2
if length %2 == 0 :
    mid = length // 2
    print(text[mid-1:mid+1])
else:
    print(text[length //2 ])