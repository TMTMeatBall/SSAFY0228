grain_lst = [('고구마', 3000), ('감자', 2000), ('옥수수', 4500), ('토란', 1300)]
grain_dict = dict(grain_lst) # key 작물명, value 작물 가격
grain_names = list(grain_dict.keys())
grain_prices = list(grain_dict.values())
max_price = max(grain_prices) # 가장 높은 가격
idx = grain_prices.index(max_price)
print("최대가격의 작물 이름은 : ",grain_names[idx])
