import numpy as np

# f = open("inputs_4.txt", "r")
T = int(input())
# T = int(f.readline())
for tc in range(T):
    N, M = map(int, input().split())
    # N, M = map(int, f.readline().split())
    grid = np.empty((0, M))
    for rows in range(N):
        grid = np.vstack([grid, list(input())])
        # grid = np.vstack([grid, list(f.readline().strip())])
    # f.close()
    if N == M == 1:
        print(0)
    else:
        dictofvalidpoints = dict()
        steps = np.zeros((N, M), dtype=int)
        for i in range(N):
            for j in range(M):
                pointsinrowontheleft = 0
                pointsincolumndown = 0
                # dictofvalidpoints[(i, j)] = 0
                for c in range(0, j):
                    if grid[i][c] == ".":
                        pointsinrowontheleft += steps[i][c]
                        # pointsinrowontheleft += dictofvalidpoints[(i, c)]
                    else:
                        pointsinrowontheleft = 0

                for r in range(0, i):
                    if grid[r][j] == ".":
                        pointsincolumndown += steps[r][j]
                        # pointsincolumndown += dictofvalidpoints[(r, j)]
                    else:
                        pointsincolumndown = 0

                # if i == j == 0:
                #     dictofvalidpoints[(i, j)] = 1
                # elif grid[i][j] == ".":
                #     dictofvalidpoints[(i, j)] = pointsinrowontheleft + pointsincolumndown

                if i == j == 0:
                    steps[i][j] = 1
                elif grid[i][j] == ".":
                    steps[i][j] = pointsinrowontheleft + pointsincolumndown
        print(steps[N - 1][M - 1])
