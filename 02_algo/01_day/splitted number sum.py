N = input()

a = list(N)

total = 0

for i in range(len(a)):
    total = total + int(a[i])
print(total)