# a=input('주민번호를 입력:')
# def de_identify(a):
#     if a.find('-'):
#         a.strip('-')
#     print(a[:6]+'*'*7)

#     else:
#         print(a[:6]+'*'*7)
#     return a



# a='950122-1234567'
# if a.find('-') !=-1:
#     a=a.replace('-','')
# print(a[:6]+'*'*7)



a=input('주민등록번호를 입력: ')
def de_indentify(a):
    if a.find('-') !=-1:
        a=a.replace('-','')
    return a[:6]+'*'*7 #return 에서는 최종 식을 정리한다
print(de_indentify(a)) #정의된 함수를 print한다 또는
a=de_indentify(a)#순차계산하므로 a또는 다른 객체에 지정할 수 있다.

#1.주민등록번호 중 '-' 있는 경우, 그것을 지운다
#2.a[:6]