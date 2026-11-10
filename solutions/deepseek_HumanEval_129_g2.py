def minPath(grid, k):
    n = len(grid)
    r = c = 0
    for i, row in enumerate(grid):
        if 1 in row:
            r, c = i, row.index(1)
            break

    res = []
    seen = {}
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

    while len(res) < k:
        if (r, c) in seen:
            start = seen[(r, c)]
            cycle = res[start:]
            remaining = k - len(res)
            res.extend(cycle * (remaining // len(cycle)) + cycle[:remaining % len(cycle)])
            break

        seen[(r, c)] = len(res)
        res.append(grid[r][c])

        if len(res) == k:
            break

        best_val = n * n + 1
        best_pos = None
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                val = grid[nr][nc]
                if val < best_val:
                    best_val = val
                    best_pos = (nr, nc)

        r, c = best_pos

    return res
