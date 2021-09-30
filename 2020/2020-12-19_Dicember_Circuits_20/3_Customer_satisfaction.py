import math

T = int(input())
for tc in range(T):
    N = int(input())
    total_Z = 0
    orders = []
    departures = []
    demand_at_departure = {}
    max_R = 0
    min_L = math.inf
    minrate = 0
    stock = 0
    for order in range(N):
        L, R, Z = map(int, input().split())
        orders.append([L, R, Z])
        departures.append(R)
        if R in demand_at_departure.keys():
            demand_at_departure[R] += Z
        else:
            demand_at_departure[R] = Z
    departures = list(set(departures))
    departures.sort()
    stock = 0
    demand = 0
    for t in departures:
        demand += demand_at_departure[t]
        minrate = max(minrate, int(math.ceil(demand / t)))
    print(minrate)
