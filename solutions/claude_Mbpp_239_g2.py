def get_total_number_of_sequences(m, n):
    if n <= 0:
        return 0
    if m <= 0:
        return 0
    dp = [1] * (m + 1)
    dp[0] = 0
    for _ in range(1, n):
        prefix = [0] * (m + 1)
        for v in range(1, m + 1):
            prefix[v] = prefix[v - 1] + dp[v]
        new = [0] * (m + 1)
        for v in range(1, m + 1):
            new[v] = prefix[v // 2]
        dp = new
    return sum(dp)
