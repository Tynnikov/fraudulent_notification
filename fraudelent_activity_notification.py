arr = [10, 20, 30, 40, 50]


def calc_median(arr: list) -> int:
    """Return median."""

    arr = sorted(arr)

    if len(arr) == 0:
        raise ValueError
    middle = len(arr) // 2
    if middle % 2 == 0:
        return (arr[middle - 1] + arr[middle]) / 2
    return arr[middle]


