# T = int(input())
# for tc in range(T):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     count = 0
#     for i in range(1, N):
#         if arr[i - i] % 2 == 1:
#             arr[i - i], arr[i] = arr[i - i] + arr[i], arr[i] - arr[i - 1]
#             count += 1
#     print(count)