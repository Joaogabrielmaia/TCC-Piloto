def get_ludic(n):
    numbers = list(range(1, n + 1))
    index = 1

    while index < len(numbers):
        step = numbers[index]
        if index + step >= len(numbers):
            break
        del numbers[index + step::step]
        index += 1

    return numbers
