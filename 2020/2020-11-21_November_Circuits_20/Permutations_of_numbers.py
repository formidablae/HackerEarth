import numpy
import itertools
import math


def cost(leftarr, rightarr, numbs):
    N = len(leftarr)
    costs = 0
    for i in range(N):
        costleft = leftarr[numbs[i]]
        costright = rightarr[numbs[i]]
        for j in range(N):
            costs = costs + costleft * j + costright * (N - j - 1)
    return costs

T = int(input())
for tc in range(T):
    N = int(input())
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))
    costs = numpy.zeros((N, N), int)
    for i in range(N):
        for j in range(N):
            costs[i][j] = left[i] * j + right[i] * (N - j - 1)
    i = 0
    mimim = math.inf
    for perm in itertools.permutations(list(range(N))):
        #print(perm)
        permutlist = list(perm)
        summat = 0
        for k in range(N):
            summat = summat + costs[permutlist[k]][k]
            if summat > mimim: break
        if mimim > summat: mimim = summat
        i = i + 1
    print(costs)
    print(mimim)