T = int(input())
for tc in range(1, T + 1):
    sentence = input()
    # repetition = ''
    # max = 0
    #
    # for i in sentence:
    #     repetition += i
    #     nichecut = len(repetition)
    #     if repetition == sentence[nichecut:nichecut*2]:
    #         max = nichecut
    #
    # print(f'#{tc} {max}') #만약 aabcd
    # print(max)
    # print(repetition)
    # print(f'#{tc} {repetition}')
    # ans = len(sent)//niche -1
    # print(f'#{tc} {ans}')

    # result = 0
    # # i : 10 -> 1 마디 중에서 가장 큰 마디 체크 먼저 진행한다...
    # for i in range(10, 0, -1):
    #     if sentence[:i] == sentence[i: i+i]:
    #         result = i
    #         break
    #
    # print(f'#{tc} {result}')
    # 1 -> 10 까지로 가는 코드를 작성
    repeat = ''
    for i in sentence:
        repeat += i
        niche = len(repeat)
        if repeat == sentence[niche:niche + niche]:
            remains = sentence[niche:]
            remains = remains.replace(repeat, '')
            if len(remains) < len(repeat):
                break

    print(f'#{tc} {niche}')
    # 제공된 인풋에서 얼마나 띄워쓰기가 필요한가
    # print(len(sentence)//len(repeat)-1)

    # sentence 말고 range 돌리기 마디의 최대 길이가 10까지인 조건을 추가하기
    # 진짜 이게 왜 맞는지 생각해보기 aabdeaabdeaabde경우에 왜 오류가 나지 않는지
