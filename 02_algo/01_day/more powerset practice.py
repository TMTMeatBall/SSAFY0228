def f1(i,k,total):
    if total > 10:
        return
    if i == k:
        if total == 10:
            for i in range(k):
                if bits[idx]:
                print(A[idx],end=' ')
            print()
        return

        for idx, bit in enumerate(bits):
            if bit ==1:
                total += A[idx]
            if total == 10:
                for idx, bit in enumerate(bits):
                    if bit:
                        print(A[idx], end=' ')
                print()
            return
        bits[i] = 0
        f1(i +1, k, total)

A = [1,2,3,4,5,6,7,8,9,10]
N = len(A)
bits = [0] * N
f1(0,N)
f2(0,N,0)