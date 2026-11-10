def minPath(grid, k):
    n = len(grid)
    val = float('inf')
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                temp = []
                if i > 0:
                    temp.append(grid[i - 1][j])
                if j > 0:
                    temp.append(grid[i][j - 1])
                if i < n - 1:
                    temp.append(grid[i + 1][j])
                if j < n - 1:
                    temp.append(grid[i][j + 1])
                val = min(temp)
    ans = []
    for i in range(k):
        if i % 2 == 0:
            ans.append(1)
        else:
            ans.append(val)
    return ans
