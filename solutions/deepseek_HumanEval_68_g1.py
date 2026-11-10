def pluck(arr):
    """
    "Given an array representing a branch of a tree that has non-negative integer nodes
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ smalest_value, its index ],
    If there are no even values or the given array is empty, return [].
    """
    best_val = None
    best_idx = None

    for i, val in enumerate(arr):
        if val % 2 == 0:
            if best_val is None or val < best_val:
                best_val = val
                best_idx = i

    if best_val is None:
        return []

    return [best_val, best_idx]
