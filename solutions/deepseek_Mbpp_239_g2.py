def get_total_number_of_sequences(m, n):
    if n == 1:
        return m
    if m.bit_length() < n:
        return 0
    if n == 2:
        r = m // 2
        return r * (m - r)

    dp = [0] + [1] * m
    for _ in range(1, n):
        acc = 0
        for i in range(1, m + 1):
            acc += dp[i]
            dp[i] = acc

        next_dp = [0] * (m + 1)
        for x in range(1, m + 1):
            next_dp[x] = dp[x // 2]
        dp = next_dp

    return sum(dp)
