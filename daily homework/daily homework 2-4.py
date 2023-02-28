# 아이스 음료 주문이 몇 개 들어왔는지 확인하세요.
# 메뉴 별 주문 수를 출력하세요.

orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
type(orders)
orders = orders.split(',')
print(orders)

print(orders)
def countice(orders):
    counter = {}
    for letter in orders:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter
countice(orders)
menu_dict = countice(orders)


icetotal = 0
for key in menu_dict:
    if '아이스' in key:
        icetotal += 1
    else:  
        icetotal += 0
print(icetotal)


print('메뉴 별 주문 수: ', countice(orders))
print('아이스 음료들 주문 수: ',icetotal)

print('총 잔의 수: ',sum(menu_dict.values()))
print('메뉴들: ',sorted(menu_dict.keys()))


print(sum(menu_dict.values()))
print(sorted(menu_dict.values()))
# orders = orders.split(',')

# orders_dict = dict()

# for order in orders:
#     orders_dict.setdefault(order, 0)
#     orders_dict[order] += 1


# # print(orders_dict)
# total = 0
# for key in orders_dict:
#     if '아이스' in key:
#         total += orders_dict[key]
# print('아이스 음료의 잔 갯수: '+ total)

# for key in orders_dict:
#     print(key, orders_dict[key])


# print('총 잔의 수: ',sum(orders_dict.values()))
# print('메뉴들: ',sorted(orders_dict.keys()))


orders = orders.split(',')
countice = dict()
total = 0
for key in countice:
    if '아이스' in key:
        total += countice[key]
print('아이스 음료 주문수: ' + total)
print(orders)
def countice(orders):
    counter = {}
    for letter in orders:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter
countice(orders)

print('메뉴 별 주문 수:', sum(countice.values()))