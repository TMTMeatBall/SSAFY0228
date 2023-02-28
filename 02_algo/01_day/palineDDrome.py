def ispalindrome(string):
    if string == string[::-1]:
        return True
    else
        return False

    return True if string == string[::-1] else False
    #2리스트를 사용해서 리버스
    origin = string
    string = list(string)
    string.reverse()
    return origin == ''.join(string)
    #3. for 문으로 진행하는 경우
    for i in range(len(string)//2):
        if string[i] != string[len(string)-i-1]:
            return False
        return True



T = int(input())
for tc in range(1,T+1):
    string = input()
    if ispalindrome(string):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
    result = 1 if ispalindrome(string) else 0