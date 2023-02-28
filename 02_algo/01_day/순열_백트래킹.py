def backtrack(a,k,input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        for i in range(1, k+1):
            print(a[i], end=' ')

        print()
    else:
        k += 1
        ncandidates = construct_candidates(a,k,input,c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a,k,input)


def construct_candidates(a,k,input,c):
    in_perm = [False] * NMAX
    for i in range(1,k):
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(1, input + 1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates






NMAX = 11
MAXCANDIDATES

def f(i, k):
    if i == k :
        print(bit)
    else:
        bit[i] = 1
        f(i+1, k)
        bit[i] = 0
        f(i+1, k)


A = {1,2,3}
N = len(A)
bit = [0]*N
#bit[ 0 0 0 ] 에서 i번째의 bit에 접근해서 집어넣는다?
