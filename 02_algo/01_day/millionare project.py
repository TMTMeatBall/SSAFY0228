T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int,input().split()))
    profit = prices[-1]
    total = 0
    for i in range(len(prices)-1,-1,-1):
        if prices[i]>profit:
            profit = prices[i]
        elif prices[i] < profit:
            total += profit - prices[i]
    print(f'#{tc} {total}')

#2.
T = int(input())
for tc in range(1,T+1):
    stack = list(map(int,input().split()))
    total = 0
    mx = stack.pop()
    while stack:
        price = stack.pop()
        if mx < price:
            mx = price
        else:
            total += mx - price

    for ptice in reversed(arr):
        if price>mx:
            mx = price
        else:
            total += mx - price