arr = [10, 20, 30, 40, 50]


def calc_median(arr: list) -> int:
    """

    :param arr: list of trailing days
    :return: median number
    """

    arr = sorted(arr)

    if len(arr) == 0:
        raise ValueError
    middle = len(arr) // 2
    if len(arr) % 2 == 0:
        return (arr[middle - 1] + arr[middle]) / 2
    return arr[middle]


def notify_fraudulent_activity(arr: list, d: int, n: int) -> int:
    """
    Function let to notify client when see fraud activity.

    :param arr: list numbers
    :param d: trailing days
    :param n: number of days
    :return: sum of notice
    """
    start = 0
    end = d
    notice = 0
    while True:
        if end == n:
            break
        new_arr = arr[start:end]
        median = calc_median(new_arr) * 2
        if arr[end] >= median:
            notice += 1
        start += 1
        end += 1
    return notice
