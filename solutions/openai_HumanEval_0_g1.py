from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    if not threshold > 0:
        return False

    ordered = sorted(number for number in numbers if number == number)
    return any(
        right - left < threshold
        for left, right in zip(ordered, ordered[1:])
    )
