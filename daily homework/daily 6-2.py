grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
# sorted(grain_lst, key=lambda x:x[1],reverse=True)[0]
# grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
# sorted(grain_lst, key=lambda x:x[1],reverse=True)[0]
# sorted(grain_lst, key=lambda x: x[1])[0]
# grain_dict =dict(grain_lst) #key작물명  value작물가격
# grain_names = list(grain_dict.keys())
# grain_prices = list(grain_dict.values())
# max_price = max(grain_prices)
# idx = grain_prices.index(max_price)
# print('최대가격의 작물 이름은:',grain_names[idx])

# list(map(lambda x: x ** 2, range(5)))     # 파이썬 2 및 파이썬 3
# [0, 1, 4, 9, 16]

# for x in range(0,5):
#     x**2
# print(x)

# for i in range(4,8):
#     print(i)

#1.가장 높은 가격을 가진 작물의 이름을 출력하기

sorted(grain_lst, key=lambda x:x[1],reverse=True)[0]#딕셔너리 또한 key[0] value[1]방식으로 계속된다
grain_dict = dict(grain_lst)
grain_names = list(grain_dict.keys())
grain_prices = list(grain_dict.values())
max_price = max(grain_prices)
idx = grain_prices.index(max_price)
print('최대가격의 작물 이름은: ',grain_names[idx])