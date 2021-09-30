import math
import operator


def get_column(list_, n):
    return list(map(operator.itemgetter(n), list_))


def calcfk(x, y, k):
    return (abs(x + y) - k) ** 2


def calculatepower(x1, y1, x2, y2, k):
    return abs(calcfk(x1, y1, k) - calcfk(x2, y2, k))


N = int(input())
balls = ["shift"]
for tc in range(N):
    coord = list(map(int, input().split()))
    coord.append(coord[0] ** 2 + coord[1] ** 2)
    balls.append([tc, coord])

Q = int(input())
queries = []
for qry in range(Q):
    query = list(map(str, input().split()))
    if query[0] == "+":
        coord = [int(query[2]), int(query[3])]
        coord.append(coord[0] ** 2 + coord[1] ** 2)
        balls[int(query[1])].append(coord)
    else:
        l = int(query[1])
        r = int(query[2])
        k = int(query[3])
        maxmim = (-math.inf)
        indexofballs = [[-1, -1], [-1, -1]]
        ball1 = [None, None]
        ball2 = [None, None]
        for i in range(l, r + 1):
            print("first = {}, last = {}. i = {}".format(l, r + l - 1, i))
            # first contenitor has many balls
            if len(balls[i]) > 2:
                for m in range(1, len(balls[i])):
                    for j in range(l, r + 1):
                        # second contenitor has many balls
                        if len(balls[j]) > 2:
                            for k in range(1, len(balls[j])):
                                diffofsquares = balls[i][m][2] - balls[j][k][2]
                                if maxmim < diffofsquares:
                                    maxmim = diffofsquares
                                    indexofballs = [[i, m], [j, k]]
                                    ball1 = [balls[i][m][0], balls[i][m][1]]
                                    ball2 = [balls[j][k][0], balls[j][k][1]]
                        # second contenitor has one ball
                        else:
                            diffofsquares = balls[i][m][2] - balls[j][1][2]
                            if maxmim < diffofsquares:
                                maxmim = diffofsquares
                                indexofballs = [[i, m], [j, 1]]
                                ball1 = [balls[i][m][0], balls[i][m][1]]
                                ball2 = [balls[j][1][0], balls[j][1][1]]
            # first contenitor has one ball
            else:
                for j in range(l, r + 1):
                    # second contenitor has many balls
                    if len(balls[j]) > 2:
                        for k in range(1, len(balls[j])):
                            diffofsquares = balls[i][1][2] - balls[j][k][2]
                            if maxmim < diffofsquares:
                                maxmim = diffofsquares
                                indexofballs = [[i, 1], [j, k]]
                                ball1 = [balls[i][1][0], balls[i][1][1]]
                                ball2 = [balls[j][k][0], balls[j][k][1]]
                    # second contenitor has one ball
                    else:
                        diffofsquares = balls[i][1][2] - balls[j][1][2]
                        if maxmim < diffofsquares:
                            maxmim = diffofsquares
                            indexofballs = [[i, 1], [j, 1]]
                            ball1 = [balls[i][1][0], balls[i][1][1]]
                            ball2 = [balls[j][1][0], balls[j][1][1]]

        print(ball1)
        print(ball2)
        power = calculatepower(ball1[0], ball1[1], ball2[0], ball2[1], k)
        print(power)