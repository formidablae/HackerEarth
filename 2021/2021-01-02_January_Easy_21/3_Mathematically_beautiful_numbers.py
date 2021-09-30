from itertools import combinations

T = int(input())
for tc in range(T):
    x, k = map(int, input().split())
    powers = []
    i = 0
    flag = False
    while True:
        num = k ** i
        if num == x:
            flag = True
            break
        elif num > x:
            break
        powers.insert(0, num)
        i += 1
    # print(powers)
    if not flag:
        for i in range(2, len(powers) + 1):
            comb = list(combinations(powers, i))
            for c in comb:
                if sum(c) == x:
                    flag = True
                    break
        if flag:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")