def highest_Power_of_2(n):
    if n < 1:
        return 0
    return 1 << (int(n).bit_length() - 1)
