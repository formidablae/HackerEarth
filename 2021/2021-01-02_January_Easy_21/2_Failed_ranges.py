# N, M = map(int, input().split())
# A_array = list(map(int, input().split()))
# B_array = list(map(int, input().split()))
# X, Y = map(int, input().split())
# C_array = []
# C_dicti = {}
# for i in range(N):
#     for j in range(M):
#         summat = A_array[i] + B_array[j]
#         C_array.append((summat, (i + 1, j + 1)))
#         # C_array.append(summat)
#         # if summat not in C_dicti.keys():
#         #     C_dicti[summat] = [(i + 1, j + 1)]
#         # else:
#         #     C_dicti[summat] += [(i + 1, j + 1)]
# C_array = sorted(C_array, key=lambda x: x[0], reverse=False)
# # C_array.sort()
# # print(C_array)
# # print(C_dicti)
# # inf_lim = C_array[X - 1]
# # sup_lim = C_array[Y - 1]
# inf_lim = C_array[X - 1][0]
# sup_lim = C_array[Y - 1][0]
# pairs = []
# # for i in range(X, Y - 1):
# #     # print(C_array[i], C_dicti[C_array[i]])
# #     if inf_lim < C_array[i] < sup_lim:
# #         pairs.append(C_dicti[C_array[i]])
# #         count += 1
# for i in range(X, Y - 1):
#     # print(C_array[i][0], C_array[i][1])
#     if inf_lim < C_array[i][0] < sup_lim:
#         pairs.append(C_array[i][1])
# # answer = set()
# # for pair in pairs:
# #     for comb in pair:
# #         p = str(comb).replace(" ", "")
# #         answer.add(p)
# # answer = sorted(list(answer))
# answer = []
# for pair in pairs:
#     answer.append(str(pair).replace(" ", ""))
# # answer = sorted(answer)
# print(len(pairs))
# print(*answer)