
# # 총 몇 잔의 주문이 들어왔는지 확인하세요.
# # 중복을 제거한 메뉴만을 리스트 형식으로 출력하세요. (단, 내림차순 정렬하여 출력하라)
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

print('총 잔의 수: ',sum(menu_dict.values()))
print('메뉴들: ',sorted(menu_dict.keys()))
# orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
# menu=()
# # print('주문량': sum(orders))
# # type(orders)
# orders = orders.split(',')
# print(len(orders))
# list(orders)
# type(orders)
# for value in orders:
#     if value not in menu:
#         result.append(value)
# print(menu)###############왜안돠ㅣㅈ.>?
# orders = orders.split(',')
# orders_dict = dict()
# for order in orders:
#     orders_dict.setdefault(order,0)###setdefalut 몰라!
#     orders_dict[order] += 1
# #dictionary 써보기

# orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
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