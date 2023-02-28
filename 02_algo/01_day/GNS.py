words = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for tc in range(1,11):

    N, length = map(str,input().split())
    length = int(len(length))
    sentence = list(map(str,input().split()))
    result = []
    for i in range(10):
        for j in sentence:
            if words[i] == j:
                result.append(j)

    print(f'{N}')
    print(*result)