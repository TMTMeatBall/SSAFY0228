dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]
x = 3
y = 3

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
# if 범위를 벗어났다면,
# break


arr = [0,1,2,3,4,5,6,7,8,9]
print(arr[3:5])

arr[3:5] = [13,14] #대입
print(arr)

arr[3:5] = [33,44,55,66] #갯수가 서로 같지 않아도 대입이 된다!
print(arr)

arr[3:] = [] #이후 범위를 일괄 삭제
print(arr)
arr[3:] = [1]*len(arr[3:])
print(arr)

# arr[3:] = 9
#이건 에러남
arr[3:] = 'hello'
print(arr)

brr = [0,1,2,3,4,5,6,7,8,9]
brr[5:5] = [10,10,10,10,10]
print(brr) #삽입
brr[::2]=[10,12,14,16]

