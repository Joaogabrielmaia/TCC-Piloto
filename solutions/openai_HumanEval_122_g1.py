def add_elements(arr, k):
    return sum(value for value in arr[:k] if len(str(value)) <= 2)
