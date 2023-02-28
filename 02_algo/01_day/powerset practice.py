arr = [1,2,3,4]
bits = [0,0,0,0]
#재귀호출로 만들수있다.
# bits = [0,0,0,1]
# bits = [0,0,1,0]
# bits = [0,0,1,1]
# bits = [0,1,0,0]
#부분집합 만들기
#i는 현재 해당되는 인덱스의 값을 0 또는 1로 바꿔주는 값
#k값은 인덱스의 끝, 배열의 크기(기저조건)
#depth 라는 매개변수를 추가
def fi(i,k,count): #기저조건에는 반복실행 막기 위한 return 필요!
    if i == k :
        if count == 2: #if i ==k:
            for idx, bit in enumerate(bits):
                if bit == 1:
                    print(A[idx], end=', ')
            print()#print(bits)
        return
    #i에 해당되는 인덱스 값을 0 으로 바꿔준다.(그 후에 재귀호출 -> 다음 i+1)
    bits[i] = 0
    f1(i+1,k,count)
    bits[i] = 1
    f1(i+1, k,count+1)

A = [1,2,3,4]

N = len(A)

bits = [0]*N
f1(0,N,0)