T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    coins = list(map(int, input().split()))
    coins.sort(reverse=True)
    count = 0
    added = set()
    summat = 0
    for coin in coins:
        if coin not in added and count < K:
            added.add(coin)
            summat += coin
            count += 1
    print(summat)
    # print(sum(set(coins[0:min(K, N)])))