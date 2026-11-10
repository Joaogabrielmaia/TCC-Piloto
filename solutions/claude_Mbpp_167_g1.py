def next_power_of_2(n):
    if n <= 1:
        return 1
    return 1 << (int(n) - 1).bit_length() if n == int(n) else 1 << int(n).bit_length()
