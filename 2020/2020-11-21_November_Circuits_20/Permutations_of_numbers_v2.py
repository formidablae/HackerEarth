import numpy
import itertools
import math
import statistics


def cost(leftarr, rightarr, numbs):
    N = len(leftarr)
    costs = 0
    for i in range(N):
        costleft = leftarr[numbs[i]]
        costright = rightarr[numbs[i]]
        costs = costs + costleft * i + costright * (N - i - 1)
    return costs


T = int(input())
for tc in range(T):
    N = int(input())
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))
    minim = math.inf
    weights = [0] * N
    diffleftright = [0] * N
    for i in range(N):
        diffleftright[i] = left[i] - right[i]
    averageleft = sum(left) / N
    averageright = sum(right) / N
    averagediff = sum(diffleftright) / N
    indexesleft = numpy.argsort(left)
    indexesright = numpy.argsort(right)
    for i in range(N):
        thiscostleft = left[i]
        weights[i] = weights[i] + (left[i] - averageleft) - (right[i] - averageright) + (left[i] - right[i] - averagediff)
    sortednumbers = numpy.argsort(weights)
    print(cost(left, right, sortednumbers))