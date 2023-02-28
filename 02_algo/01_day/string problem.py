#총 10개의 테스트 케이스가 주어진다

for _ in range(1,11):
    tc = input()
    pat = input()
    text = input()
    total=text.count(pat)

    print(f'#{tc} {total}')