def pluck(arr):
    result = []
    for i, val in enumerate(arr):
        if val % 2 == 0:
            if not result or val < result[0]:
                result = [val, i]
    return result
