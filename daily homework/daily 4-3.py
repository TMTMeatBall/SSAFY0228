numbers = [1, 1, 3, 3, 0, 1, 1]

before = None
for idx in range(len(numbers)-1,-1,-1):
    if before == numbers[idx]:
        del numbers[idx]
        continue
    before = numbers[idx]

print(numbers)

#이해해보기

