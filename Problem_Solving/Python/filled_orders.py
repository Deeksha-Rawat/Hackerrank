def filledOrders(order, k):
    """Method that resolve filled orders problem.
    Usage: print(filledOrders([3, 2, 1], 3))  # Output: 2
    """

    total = 0

    for i, v in enumerate(sorted(order)):
        if total + v <= k:
            total += v
        else:
            return i
    else:
        return len(order)
