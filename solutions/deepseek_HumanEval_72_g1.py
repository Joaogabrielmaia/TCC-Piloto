def will_it_fly(q, w):
    """
    Return True if q is a palindromic list and its sum is <= w.
    """
    return q == q[::-1] and sum(q) <= w
