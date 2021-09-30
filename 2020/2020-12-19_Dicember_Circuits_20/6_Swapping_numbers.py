import math

N = int(input())
permut = list(map(int, input().split()))
# N = 8
# permut = [6, 1, 4, 8, 2, 7, 3, 5]
# N = 8
# permut = [8, 7, 6, 5, 4, 3, 2, 1]
# N = 5
# permut = [1, 4, 2, 3, 5]
if N < 3:
    print(0)
else:
    dist_to_right = [0] * N
    for i in range(N):
        dist_to_right[i] = i - permut[i] + 1
    if max(dist_to_right) == 0 and min(dist_to_right) == 0:
        print(0)
    else:
        minim_index = dist_to_right.index(min(dist_to_right))
        maxim_index = dist_to_right.index(max(dist_to_right))
        # swap them
        # print(permut)
        # print(dist_to_right)
        permut[minim_index], permut[maxim_index] = permut[maxim_index], permut[minim_index]
        dist_to_right[minim_index] = minim_index - permut[minim_index] + 1
        dist_to_right[maxim_index] = maxim_index - permut[maxim_index] + 1
        # print(permut)
        # print(dist_to_right)
        # print()
        if max(dist_to_right) == 0 and min(dist_to_right) == 0:
            print(0)
        else:
            count = 0
            j = 1
            # while j < N:
            #     if permut[j] < permut[j - 1]:
            #         permut[j], permut[j - 1] = permut[j - 1], permut[j]
            #         dist_to_right[j] = j - permut[j] + 1
            #         dist_to_right[j - 1] = j - permut[j - 1]
            #         count += 1
            #         if j > 1:
            #             j -= 1
            #         else:
            #             j += 1
            #     else:
            #         j += 1
            #     print(permut)
            #     print(dist_to_right)
            #     print()
            while j < N:
                if dist_to_right[j] > dist_to_right[j - 1]:
                    dist_to_right[j], dist_to_right[j - 1] = dist_to_right[j - 1] + 1, dist_to_right[j] - 1
                    count += 1
                    if j > 1:
                        j -= 1
                    else:
                        j += 1
                else:
                    j += 1
            #     print(permut)
            #     print(dist_to_right)
            #     print()
            # print(permut)
            print(count)
