def get_ludic(n):
    if n < 1:
        return []

    numbers = list(range(2, n + 1))
    index = 0

    while index < len(numbers):
        step = numbers[index]
        start = index + step
        if start >= len(numbers):
            break
        del numbers[start::step]
        index += 1

    return [1] + numbers
