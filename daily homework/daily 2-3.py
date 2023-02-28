# # 하나의 문장을 입력받아, 그 문장에 끝말잇기 규칙을 적용시켜보려 한다. 
# # 세 단어가 입력으로 주어졌을 때 그 끝말잇기가 옳으면 Pass, 옳지 않으면 Fail을 출력하시오. 
# # 예를 들어 saFe eMotion Nail 인 경우, pass를 출력한다.


text = 'saFe eMotion Nail'
text = text.lower()
a,b,c = text.split()
if b[0]== a[-1] and b[-1] == c[0]:
    print('Pass')
else:
    print('Fail')



# str_lst = input('문자열을 입력하세요. : ')


# text = 'saFe eMotion Nail'
# text = text.lower()

# a,b,c = text.split()

# if a[-1] == b[0] and b[-1] == c[0]:
#     print('Pass')
# else:
#     print('Fail')



# text = 'saFe eMotion Nail'
# text = text.lower()

# a,b,c = text.split()

# for idx in range(len(words)):
#     if words[idx][-1] != word[idx+1][0]:
#         print('Fail')
#         break

# if is_flag:
#     print



# def wordgame(text):
#     for idx in range(len(words)):
#         if words[idx][-1] != word[idx+1][0]:
#             print('Fail')
#         break
#     return True

#     if isvalid=True

    

