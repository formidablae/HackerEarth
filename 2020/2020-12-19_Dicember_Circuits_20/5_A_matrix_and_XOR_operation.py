T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    if (N == 1 or M == 1) and 1 <= K <= N * M:
        print("Yes")
    elif K > N * M:
        print("No")
    elif (N != 1 and M != 1) and K == 1:
        print("No")
    else:
        flag = False
        for x in range(0, N + 1):
            if N == 2 * x:
                if K == M * x:
                    flag = True
                    break
            else:
                val = (K - M * x) / (N - 2 * x)
                if val.is_integer() and 0 <= val <= M:
                    flag = True
                    break
        if flag:
            print("Yes")
        else:
            print("No")