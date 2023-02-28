# words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# # 문자열 배열을 받아 애너그램 단위로 그룹핑하라
# # 단어를 리스트로 변환 -> 정렬
# # 먼저 len(a)==len(b)로 단어 길이 같은지를 먼저 판단하고
# # for 구문으로 

# #저장가능한 배열 하나를 만들기
# #그룹핑 된 애너그램 리스트 groups를 만들자

# groups = []

# for i in range(len(words)):
#     if checks[i] == True:
#     group = set()
#     groups.append(group)
#     group.add(words[i])
#     for j in range(i+1, len(words)):
#         if len(words[i] != len(words[j])):
#             continue
#         a= sorted(list(words[i]))
#         b= sorted(list(words[j]))
#         for k in range(len(a)):
#             if a[k] != b[k]:
#                 break
#         else:#a 와 b는 같은 애너그램 그룹에 속한다.


            

words = ['abc', 'bac', 'aaa', 'ccc', 'cab', 'cba']
checks = [False] * len(words) # [False,False,False,False,False,False]

#그룹핑된 애너그램 리스트
groups = []

for i in range(len(words)):
    group = set()
    groups.append(group)
    group.add(words[i])
    for j in range(i+1, len(words)):
        if checks[j] or len(words[i]) != len(words[j]):
            continue
        a = sorted(list(words[i]))
        b = sorted(list(words[j]))
        for k in range(len(a)):
            if a[k] != b[k]:
                break
        else: # a와 b는 같은 애너그램 그룹에 속한다
            group.add(words[j])
            checks[j] = True

#다른 방법
for word in words:
    key = ''.join(sorted(word)) #aet
    if anagrams.get(key): #== None
        anagrams[key] = []
    anagrams[key].append(key)

print(list(anagrams.values()))

import collections

words = ['eat', 'tea', 