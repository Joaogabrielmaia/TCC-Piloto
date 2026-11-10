def pluck(arr):
    result = []
    for index, value in enumerate(arr):
        if value % 2 == 0 and (not result or value < result[0]):
            result = [value, index]
            if value == 0:
                break
    return result
