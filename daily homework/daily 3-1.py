
text = 'apple,rottenBanana,apple,roTTenorange,Orange'

def fruitreplacer(text):
    
    fruit=text.lower()
    fruit=fruit.replace('rotten','')
    fruit=fruit.split(',')
  
    
    return fruit

print(fruitreplacer(text))


# text = text.lower()
# print(text)
# text = text.replace('rotten','')
# print(text)
# fruits = text.split(',')
# print(fruits)


#rotton 문자열 제거
#소문자로 바꿔주기
#리스트 형태로 바꾸기

# text = ['apple','rottenBanana','apple','roTTenorange','Orange']
# for fruits in ['apple','rottenBanana','apple','roTTenorange','Orange']:
#     fruits = text.lower()
#     print(fruits)
# #???

# a= input('fruitstring: ')

# def fruitreplacer():
#     if type(text) is str:
#         text=text.lower()
#         text=text.split(',')
