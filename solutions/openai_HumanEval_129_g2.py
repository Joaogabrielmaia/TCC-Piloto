def minPath(grid, k):
    if k == 1:
        return [1]

    n = len(grid)
    row, col = next(
        (r, c)
        for r in range(n)
        for c in range(n)
        if grid[r][c] == 1
    )

    neighbor = min(
        grid[r][c]
        for r, c in (
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
        )
        if 0 <= r < n and 0 <= c < n
    )

    return [1 if i % 2 == 0 else neighbor for i in range(k)]
