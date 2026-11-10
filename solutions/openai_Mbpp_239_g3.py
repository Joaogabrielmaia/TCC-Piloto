def get_total_number_of_sequences(m, n):
    if n == 1:
        return m
    if n > m.bit_length():
        return 0

    limit = m >> (n - 1)
    counts = [0] + [1] * limit

    for length in range(2, n):
        limit = m >> (n - length)
        next_counts = [0] * (limit + 1)
        running_total = 0

        for value in range(1 << (length - 1), limit + 1):
            if value % 2 == 0:
                running_total += counts[value // 2]
            next_counts[value] = running_total

        counts = next_counts

    return sum(
        count * (m - 2 * value + 1)
        for value, count in enumerate(counts)
        if count
    )
