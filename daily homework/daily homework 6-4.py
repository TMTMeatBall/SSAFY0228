# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 
#1.문자열 배열을 받을 것
#2. 단어들을 애너그램 단위로 그룹핑할것
#3.그런 일을 하는 함수 group_anagrams를 작성할 것.

text =  ['eat','tea','tan','ate','nat','bat']

# type(text) #리스트

# def group_anagram(text):
#     if len(a) == len(b)

#1.서로 단어 안의 철자 수가 같은지를 체크
#2.text안의 문자열을 전부 쪼개서 정렬했을 때, 동일할 것
#3.애너그램 단위 그룹핑->딕셔너리화 (anagram(key):original(value))
#4.출력은 리스트로 나와야 하므로 같은 애너그램이 나올 때마다 value에 원소를 추가한다.
sorted(text) #sorted는 문자열도 사용가능하다
sorted(text[0])#를 모든 text내 문자열 str에 사용하고, 그 애너그램 키를 비교하여 같은 경우, value인 original words에 추가한다

def group_anagrams():

