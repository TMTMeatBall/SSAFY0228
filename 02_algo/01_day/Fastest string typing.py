#첫 번째 줄에 테스트케이스가 주어진다
T = int(input())
for tc in range(1,T+1):
    A,B = input().split()

    len_A = len(A)
    len_B = len(B)
    i = 0 #문장 txt인덱스
    key = 0#총 타이핑 수
    while i < len_A:
        if A[i] == B[0]:
            if A[i:i+len_B] == B:
                key += 1
                i += len_B
            else:
                key += 1
                i += 1
        else:
            key +=1
            i += 1
    print(f'#{tc} {key}')

    # A와 같은요소를 모두 특정 단어로 ㅊ환하고 그 후의 문장의 len을 재면 도지 않을까?
    # 총 길이에서 타이핑 할 수 있는 키를 카운트하고 카운팅 된 횟수만큼 깎고, +1해준다(1회는 사용하므로)
    # print(f'#{tc+1} {len(A)-(len(B)-1)*A.count(B)}')
    #A[i]와 B[0]  이 같을 때에, A[i:i+lenB] == B 이면 총 타이핑 수는 +1을,
    # 텍스트는 i에서 len_B만큼 증가한 데서 다시 연산