def is_sorted(lst):
    from collections import Counter
    counts = Counter(lst)
    if any(c > 2 for c in counts.values()):
        return False
    return all(lst[i - 1] <= lst[i] for i in range(1, len(lst)))
