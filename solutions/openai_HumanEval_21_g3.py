from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    minimum = min(numbers)
    maximum = max(numbers)
    span = maximum - minimum

    if span == 0:
        return [0.0 for _ in numbers]

    if span == float("inf") and minimum != float("-inf") and maximum != float("inf"):
        half_minimum = minimum / 2.0
        half_span = maximum / 2.0 - half_minimum
        return [(number / 2.0 - half_minimum) / half_span for number in numbers]

    return [(number - minimum) / span for number in numbers]
