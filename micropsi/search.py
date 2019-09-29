from micropsi import assertions


def min_search(data):
    """
    Searches for the minimum element inside data

    :param data: Data to be searched. The data object must provide length and be subscriptable (ex: list). Elements
    contained inside don't have to be of same type, but must all implement __lt__, and be compatible with one another/
    support each other in that implementation.

    The data array shall be given such that the first few elements are strictly monotonically decreasing,
    the remaining elements are strictly monotonically increasing

    :return: Element in data that is less than all other elements
    :rtype: object
    """
    return __min_binsearch(data)


def __min_binsearch(data, start=0, datalen=-1):
    """
    Applies binary search to find the minimum item contained in side data

    :param data: Data to be searched. The data object must provide length and be subscriptable (ex: list). Elements
    contained inside don't have to be of same type, but must all implement __lt__, and be compatible with one another/
    support each other in that implementation.

    The data array shall be given such that the first few elements are strictly monotonically decreasing,
    the remaining elements are strictly monotonically increasing

    :param start: Where to start searching data
    :type start: int
    :param datalen: How many elements to search, starting index given by start
    :type datalen: int
    :return: Element in data that is less than all other elements
    :rtype: object
    """
    # Ensure data object is compatible
    assertions.ensure_not_none(data, "data must not be None")
    assertions.ensure_subscriptable(data, "data must support random access")
    assertions.ensure_has_length(data, "data must provide length")
    assertions.check(len(data), "data must not be empty", fail=True)

    # Ensure indices and datalen are valid
    assertions.check(type(start) is int, "Can only support int indices", fail=True)
    assertions.check(start >= 0, "Invalid start index: %s" % start, fail=True)
    assertions.check(datalen != 0, "datalen must be greater than 0", fail=True)

    if datalen < 0:
        assertions.ensure_has_length(data, "data object does not provide length, and not datalen supplied")
        datalen = len(data)

    # if there is one element remaining, this must be the minimum
    if datalen == 1:
        return data[0]

    # mid point where data is going to be split, shifted by start
    split_index = start + (datalen // 2)

    # Begin by assuming the left chunk is increasing towards split_index
    left_decreasing = False
    left_len = split_index - start
    # first element to the left of split_index
    left_peek_one = data[split_index - 1]
    # index of second element to the left of split index (if any)
    left_peek_two_index = split_index - 2

    # Begin by assuming the right chunk is decreasing away from split_index
    right_increasing = False
    right_len = datalen - left_len
    # first element to the right of split_index
    right_peek_one = data[split_index]
    # index of second element to the right of split index (if any)
    right_peek_two_index = split_index + 1

    # left chunk is decreasing towards split_index if left_peek_one is less than left_peek_two
    # if there is only one element in left chunk, will treat as decreasing too
    if left_len == 1 or left_peek_one < data[left_peek_two_index]:
        left_decreasing = True
        # if the right chunk is also decreasing but away from split_index, the minimum must exist on it, drop
        # the left chunk and repeat the search on right one.
        if right_len > 1 and data[right_peek_two_index] < right_peek_one:
            return __min_binsearch(data, split_index, right_len)

    # right chunk is increasing away of split_index if right_peek_one is less than right_peek_two
    # if there is only one element in right chunk, will treat as increasing too.
    if right_len == 1 or right_peek_one < data[right_peek_two_index]:
        right_increasing = True
        # if the left chunk is also increasing but towards split_index, the minimum must exist on it, drop
        # the right check and repeat search on left one
        if left_len > 1 and data[left_peek_two_index] < left_peek_one:
            return __min_binsearch(data, start, left_len)

    # if left chunk was decreasing toward split_index, and right chunk was increasing away from split_index
    # the minimum is one of their first elements with respect to split_index
    if left_decreasing and right_increasing:
        return left_peek_one if left_peek_one < right_peek_one else right_peek_one

    raise ValueError("Elements in data are not strictly monotonically decreasing then increasing, aborting")
