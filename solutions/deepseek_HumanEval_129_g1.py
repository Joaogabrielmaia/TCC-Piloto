def minPath(grid, k):
    n = len(grid)

    # Find the cell containing the smallest value, 1
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                curr_r, curr_c = r, c
                break
        else:
            continue
        break

    path = [1]

    for _ in range(k - 1):
        best_val = None
        best_r = best_c = None

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = curr_r + dr, curr_c + dc
            if 0 <= nr < n and 0 <= nc < n:
                val = grid[nr][nc]
                if best_val is None or val < best_val:
                    best_val = val
                    best_r, best_c = nr, nc

        path.append(best_val)
        curr_r, curr_c = best_r, best_c

    return path
