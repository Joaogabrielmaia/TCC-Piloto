def get_total_number_of_sequences(m, n):
    if n == 1:
        return m
    if m.bit_length() <= n - 1:
        return 0

    dp = [0] + [1] * m

    for _ in range(1, n):
        new = [0] * (m + 1)
        prefix = 0
        j = 0

        for x in range(1, m + 1):
            limit = x // 2
            while j <= limit:
                prefix += dp[j]
                j += 1
            new[x] = prefix

        dp = new

    return sum(dp)
