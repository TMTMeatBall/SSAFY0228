# a = ['a', 'b', 'c']
# b = ['a', 'b', 'c', 'd', 'e', 'f']

# def is_include(a, b):
# 	for item in a:
# 		if item not in b:
# 			return False
# 	return True

# if is_include(a, b):
# 	print('a 리스트는 a 리스트에 속해있다')
# else:
# 	print('안속해있데요?')

# a = {'a', 'b', 'c'}
# b = {'a', 'b', 'c', 'd', 'e', 'f'}

# if a.issubset(b):
#     print("a ⊆ b")


a_list = ['a','a','b','b','b', 'c','c']
# 중복을 제거해서 다시 리스트 a_list에 할당


#1. for문을 순회해서 새로운 중복이 없는 리스트를 만든다.
# def unique(items):
#     items = sorted(items)
#     result = []
#     for item in items:
#         if result[-1] != item:
#             result.append(item)

#     return result

# a_list = unique(a_list)

#2. set을 이용해서 중복을 제거하는 방법
a_list = ['a','a','b','b','b', 'c','c']
# a_set = set(a_list)
# a_list = list(a_set)
a_list = list(set(a_list))

#3. dict.fromkeys 메소드를 만드는 방법 (번외)
a_dict = dict.fromkeys(a_list, None)
a_list = list(a_dict.keys())