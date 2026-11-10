def minPath(grid, k):
    n = len(grid)
    min_neighbor = float('inf')
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        min_neighbor = min(min_neighbor, grid[ni][nj])
    return [1 if idx % 2 == 0 else min_neighbor for idx in range(k)]
