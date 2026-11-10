def minPath(grid, k):
    if k == 1:
        return [1]

    n = len(grid)
    row, col = next(
        (r, c)
        for r, values in enumerate(grid)
        for c, value in enumerate(values)
        if value == 1
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
    return [1, neighbor] * (k // 2) + ([1] if k % 2 else [])
