def get_total_number_of_sequences(m, n):
    if n > m.bit_length():
        return 0
    if n == 1:
        return m

    # counts[x] counts shorter sequences whose elements are at most x.
    counts = list(range((m >> (n - 1)) + 1))

    for length in range(2, n):
        limit = m >> (n - length)
        next_counts = [0] * (limit + 1)
        running_total = 0
        for maximum in range(1, limit + 1):
            running_total += counts[maximum // 2]
            next_counts[maximum] = running_total
        counts = next_counts

    # Sum counts[last // 2] over all possible final elements.
    return 2 * sum(counts) - (counts[-1] if m % 2 == 0 else 0)
