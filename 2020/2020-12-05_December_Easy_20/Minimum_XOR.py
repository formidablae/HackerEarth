import math

q = int(input())
for query in range(q):
    query_vals = list(map(int, input().split()))
    X = query_vals[1]
    K = 0
    if query_vals[0] == 2:
        K = query_vals[2]