T = int(input())
for tc in range(T):
    x = int(input())
    arr = list(map(int, input().split()))
    elements = set(arr)
    result = 0
    left = {}
    right = {}
    for el in elements:
        left[el] = x
        right[el] = -1
    # print("counts", counts)
    # print()
    # print("left ", left)
    # print("right", right)
    # print()
    for k in range(x):
        this_num = arr[k]
        left[this_num] = min(k, left[this_num])
        right[this_num] = max(k, right[this_num])
        # print("this_num ", this_num)
        # print("k", k)
        # print("left ", left)
        # print("right", right)
        # print()
    # print("result", result)
    for elem in elements:
        result += (right[elem] - left[elem])
        # print("result", result)
    print(result)