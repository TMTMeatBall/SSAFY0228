words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}

words = []
# 위의 딕셔너리를 in- 키워드를 넣어서 부정 단어로 바꿔보라.   
for word , _ in words_dict.items():
    # 앞의 철자가 p, b, m 중 하나라면 im을 붙이고,
    if word[0] in ['p', 'b', 'm']:
        words.append('im' + word)
    elif word[0] == 'l': # 앞의 철자가 l 이라면            il을 붙이고,
        words.append('il' + word)
    elif word[0] == 'r': # 앞의 철자가 r 이라면 ir을 붙인다.
        words.append('ir' + word)
    else: # in을 붙인다.
        words.append('in' + word)

# 최종적으로 오름차순으로 출력하라
print(sorted(words))