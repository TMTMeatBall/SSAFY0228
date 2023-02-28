# T = int(input())
# for tc in range(1,T+1):
#     N= map(int,input().split())
#     print(f'#{tc}{}')


def prime_factor(x):
    list_1 = []
    d = 2
    while d <= x:
        if x % d == 0:
            list_1.append(d)
            x = x/d
        else:
            d = d+1
    count = 0
    count_list = []
    for idx, num in enumerate(list_1):
        if idx < len(list_1)-1:
            count += 1

            if list_1[idx] != list_1[idx+1]:
                count_list.append(count)
                count = 0

            if list_1[idx] == list_1[-1]:
                count_list.append(count)

    result = ''
    for i in count_list:

        result += str(i)
        result += ' '

    return result
print(prime_factor(6791400))


# # 영향을 받지 않기 위해 for문 바깥에 위치
# divs = [2, 3, 5, 7, 11]
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     # divs의 cnt를 세주기 위해 리스트를 하나 만든다.
#     cnts = [0] * len(divs)
#
#     # divs의 값만큼 cnts에도 적용할 수 범위를 설정
#     for i in range(len(divs)):
#         # 소인수 분해를 하기 위해 나눴을 떄 0으로 나누어 지는가?
#         while N % divs[i] == 0:
#             cnts[i] += 1
#             N //= divs[i]
#
#     # divs가 얼만큼 사용되었는지 출력
#     print(f'#{tc}', *cnts)