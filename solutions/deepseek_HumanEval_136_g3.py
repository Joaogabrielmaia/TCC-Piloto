def largest_smallest_integers(lst):
    a = None
    b = None

    for x in lst:
        if x < 0:
            if a is None or x > a:
                a = x
        elif x > 0:
            if b is None or x < b:
                b = x

    return (a, b)
