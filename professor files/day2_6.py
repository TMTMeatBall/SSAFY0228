orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
orders = orders.split(',')

orders_dict = dict()

for order in orders:
    orders_dict.setdefault(order, 0)
    orders_dict[order] += 1


# print(orders_dict)
total = 0
for key in orders_dict:
    if '아이스' in key:
        total += orders_dict[key]
print('아이스 음료의 잔 갯수: '+ total)

for key in orders_dict:
    print(key, orders_dict[key])


print('총 잔의 수: ',sum(orders_dict.values()))
print('메뉴들: ',sorted(orders_dict.keys()))