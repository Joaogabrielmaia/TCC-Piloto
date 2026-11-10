def next_power_of_2(n):
    if n <= 0:
        return 1
    return 1 << (n - 1).bit_length()
