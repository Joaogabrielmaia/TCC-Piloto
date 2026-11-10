def get_total_number_of_sequences(m, n):
    if n <= 0:
        return 0
    # dp[v] = number of sequences of current length ending with value v
    dp = [0] + [1] * m
    for _ in range(n - 1):
        prefix = [0] * (m + 1)
        for v in range(1, m + 1):
            prefix[v] = prefix[v - 1] + dp[v]
        new = [0] * (m + 1)
        for v in range(1, m + 1):
            new[v] = prefix[v // 2]
        dp = new
    return sum(dp)
