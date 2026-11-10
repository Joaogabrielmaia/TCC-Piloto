def highest_Power_of_2(n):
    if n <= 0:
        return 0
    return 1 << (n.bit_length() - 1)
