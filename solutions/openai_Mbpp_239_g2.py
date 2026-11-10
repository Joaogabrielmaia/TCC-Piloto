def get_total_number_of_sequences(m, n):
    from itertools import accumulate

    if m <= 0 or n <= 0:
        return 0
    if n > m.bit_length():
        return 0
    if n == 1:
        return m

    limit = m >> (n - 1)
    counts = list(range(limit + 1))

    for length in range(2, n):
        limit = m >> (n - length)
        counts = list(
            accumulate(counts[value // 2] for value in range(limit + 1))
        )

    return 2 * sum(counts) - (counts[-1] if m % 2 == 0 else 0)
