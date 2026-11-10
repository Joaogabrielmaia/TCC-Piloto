def highest_Power_of_2(n):
    if n < 1:
        return 0
    power = 1
    while power <= n:
        power <<= 1
    return power >> 1
