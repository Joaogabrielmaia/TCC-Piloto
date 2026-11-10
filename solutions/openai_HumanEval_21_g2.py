from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    minimum = min(numbers)
    maximum = max(numbers)

    if minimum == maximum:
        return [0.0 for _ in numbers]

    span = maximum - minimum
    if span == float("inf") and minimum != -float("inf") and maximum != float("inf"):
        minimum /= 2.0
        span = maximum / 2.0 - minimum
        return [(number / 2.0 - minimum) / span for number in numbers]

    return [(number - minimum) / span for number in numbers]
