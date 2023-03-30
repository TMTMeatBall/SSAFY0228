# #단순 순열 생성 {1,2,3}을 포함하는 모든 순열을 생성하는 함수
# for i in 1->3
#     for j in 1->3
#         if j != i :
#             for k in 1->3
#                 if k != i and k != j
#                     print(i,j,k)
# for문으로 하기에는 구조가 복잡하다 재귀 형식이 필요한 이유

lst = [1,2,3,4,5]
n=5
#가능한 순열의 경우의 수는 5!
#swap 방식으로 구현해보기
#현재 idx 번째 숫자를 다른 누구와 바꿀건지 정해준다.
def permutation(idx):
    global cnt
    #pruning 안했네~
    #교환횟수를 줄일 수 있는 방법이 있다

    #종료조건
    if idx == n:
        cnt += 1
        #자리를 바꾸고 난 후에 할 일을 적는다.
        print(lst)
        return
    #재귀호출
    #idx번째 숫자와 자리를 바꾼다.
    #다른 숫자는 중복을 피하기 위해서 idx 보다 커야 한다.
    for i in range(idx,n):
        #idx와 자리를 바꿀 i를 정했다.
        lst[idx],lst[i]=lst[i],lst[idx]
        perm(idx + 1)
