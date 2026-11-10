def add_elements(arr, k):
    return sum(value for value in arr[:k] if -99 <= value <= 99)
