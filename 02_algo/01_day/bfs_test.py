def Bf1(p,t,m,n): #1. 이중 for 문
    for i in range(N-M+1): #왜 N-M+1?
        for j in range(M):
            if t[i+j] != p[j]: #왜 i+j?
                break
            else:
                return i #패턴이 매칭되었을 때의 idx넘버
    return -1
#2. 슬라이싱
    def Bf2(p, t, m, n):  # 1. 이중 for 문
        for i in range(N - M + 1):  # 왜 N-M+1?
            #p 에서 문자열을 M만큼 가져오고
            #t와 비교를 수행한다.
            if p[i:i+M] == t:
                return i
    return -1
#3. 문자열 메소드의 사용
def Bf3(p,t,m,n):
    #문자열의 find 메소드
    return p.find(t) #2 t를 역순탐색은 가능할까?
    p.find(t,3) #5

#4. 해당 p문자열이 t에서 얼마나 사용되는지 셀 수 있을까?
def count1(p,t,M,N):
    #count 할 변수
    cnt = 0
    #while문의 조건
    #idx를 저장할 i변수
    i = -1
    #find 메서드로 i idx를 갱신
    while (i := p.find(t,i)) != -1:
        cnt += 1
    return cnt
# 5. count 메소드 사용하기
def count3(p,t,M,N):
    return p.count(t)
p = 'is'
t = 'This is a book~!'
M = len(p)
N = len(t)
