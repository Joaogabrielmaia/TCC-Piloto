def minPath(grid, k):
    n = len(grid)
    
    # Locate the cell containing value 1.
    start_r = start_c = -1
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                start_r, start_c = r, c
                break
        if start_r != -1:
            break
    
    path = [1]
    r, c = start_r, start_c
    
    for _ in range(k - 1):
        best_r = best_c = -1
        best_val = float('inf')
        
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                val = grid[nr][nc]
                if val < best_val:
                    best_val = val
                    best_r, best_c = nr, nc
        
        r, c = best_r, best_c
        path.append(grid[r][c])
    
    return path
