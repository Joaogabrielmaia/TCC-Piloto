def largest_smallest_integers(lst):
    largest_negative = None
    smallest_positive = None

    for number in lst:
        if number < 0:
            if largest_negative is None or number > largest_negative:
                largest_negative = number
        elif number > 0:
            if smallest_positive is None or number < smallest_positive:
                smallest_positive = number

    return largest_negative, smallest_positive
