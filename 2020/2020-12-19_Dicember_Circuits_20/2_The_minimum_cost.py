T = int(input())
for tc in range(T):
    N, C01, C10 = map(int, input().split())
    A_list = list(map(int, input().split()))
    cost1_start1 = 0
    cost2_start0 = 0
    for i in range(N):
        if i % 2 == 0:
            if A_list[i] != 1:
                cost1_start1 += C01
            else:
                cost2_start0 += C10
        else:
            if A_list[i] != 0:
                cost1_start1 += C10
            else:
                cost2_start0 += C01
    print(min(cost1_start1, cost2_start0))
