def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # keys = set(nums)
    # highest_count = 0
    # mode = None
    # for val in keys
    #     if highest_count < nums.count(val)
    #         mode 

    nums.sort()
    biggest_count = 0
    curr_count = 0
    mode = None
    last_n = nums[0]

    for n in nums:
        if n == last_n:
            curr_count += 1
            if biggest_count < curr_count:
                biggest_count = curr_count
                mode = n 
    return mode