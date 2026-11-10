from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    minimum = min(numbers)
    maximum = max(numbers)
    if minimum == maximum:
        return [0.0 for _ in numbers]
    span = maximum - minimum
    return [(number - minimum) / span for number in numbers]
