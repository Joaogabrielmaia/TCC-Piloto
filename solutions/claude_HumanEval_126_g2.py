def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.
    '''
    counts = {}
    for x in lst:
        counts[x] = counts.get(x, 0) + 1
        if counts[x] > 2:
            return False
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            return False
    return True
