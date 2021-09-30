import numpy as np

f = open("inputs_4.txt", "r")
# T = int(input())
T = int(f.readline())
for tc in range(T):
    # N, M = map(int, input().split())
    N, M = map(int, f.readline().split())
    grid = np.empty((0, M))
    for rows in range(N):
        # grid = np.vstack([grid, list(input())])
        grid = np.vstack([grid, list(f.readline().strip())])
    f.close()
    if N == M == 1:
        print(0)
    else:
        dictofvalidpoints = dict()
        stepsleft = np.zeros((N, M), dtype=int)
        stepsup = np.zeros((N, M), dtype=int)
        for i in range(N):
            for j in range(M):
                pointsinrowontheleft = 0
                pointsincolumndown = 0

                if grid[i][j] == "." and j != 0:
                    pointsinrowontheleft = stepsleft[i][j - 1]
                else:
                    pointsinrowontheleft = 0

                if grid[i][j] == "." and i != 0:
                    pointsincolumndown = stepsup[i - 1][j]
                else:
                    pointsincolumndown = 0

                if i == j == 0:
                    stepsleft[i][j] = 1
                    stepsup[i][j] = 1
                elif i == N - 1 and j == M - 1:
                    stepsleft[i][j] = pointsinrowontheleft + pointsincolumndown
                    stepsup[i][j] = pointsinrowontheleft + pointsincolumndown
                elif grid[i][j] == "." and i == 1 and j == 0:
                    stepsleft[i][j] = pointsinrowontheleft + pointsincolumndown
                    stepsup[i][j] = pointsinrowontheleft + 2 * pointsincolumndown
                elif grid[i][j] == "." and i == 0 and j == 1:
                    stepsleft[i][j] = 2* pointsinrowontheleft + pointsincolumndown
                    stepsup[i][j] = pointsinrowontheleft + pointsincolumndown
                elif grid[i][j] == "." and i != N and j != M:
                    stepsleft[i][j] = 2 * pointsinrowontheleft + pointsincolumndown
                    stepsup[i][j] = pointsinrowontheleft + 2 * pointsincolumndown
                # print("stepsleft\n", stepsleft)
                # print("stepsup\n", stepsup)
                # print()
        print(stepsleft[N - 1][M - 1])
