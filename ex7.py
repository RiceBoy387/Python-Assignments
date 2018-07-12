def rsum(nums):
    '''(list) -> int
    This function is designed to sum up all the values that are in the given
    list. Functin will return an integer value
    '''
    # Base case
    if ((len(nums) == 1) and isinstance(nums[0], int)):
        result = nums[0]
    elif ((len(nums) == 1) and isinstance(nums[0], list)):
        result = rsum(nums[0])
    elif (len(nums) != 0):
        if (isinstance(nums[0], int)):
            result = nums[0] + rsum(nums[1:])
        else:
            result = rsum(nums[0]) + rsum(nums[1:])
    else:
        result = 0
    # Return the result
    return result


def rmax(nums):
    '''(list) -> int
    This function is designed to find the maximum value in a given list. Will

    return the max value
    '''
    # Base case
    if ((len(nums) == 1) and isinstance(nums[0], int)):
        result = nums[0]
    elif ((len(nums) == 1) and isinstance(nums[0], list)):
        result = rmax(nums[0])
    elif (len(nums) != 0):
        max_num = rmax(nums[1:])
        if (isinstance(nums[0], list)):
            nums[0] = rmax(nums[0])
        if (nums[0] > max_num):
            result = nums[0]
        else:
            result = max_num
    else:
        result = 0
    return result


def low_lowest(nums):
    '''(list) -> tup
    This function is designed to be a helper function which will return the
    lowest and second lowest values in a given list. Will return a tuple
    '''
    # Base case
    if (len(nums) == 2):
        if (nums[0] < nums[1]):
            result = (nums[0], nums[1])
        else:
            result = (nums[1], nums[0])
    else:
        low_tup = low_lowest(nums[1:])
        if (nums[0] < low_tup[0]):
            result = (nums[0], low_tup[0])
        elif (nums[0] < low_tup[1]):
            result = (low_tup[0], nums[0])
        else:
            result = low_tup
    return result


def second_smallest(nums):
    '''(list) -> int
    This function is deisgned to find the second smalles value in a given list.
    Will return that value
    '''
    new_list = flatten(nums)
    result = low_lowest(new_list)
    return (result[1])


def max_min(nums):
    '''(list) -> tup
    This function is a helper function which will return the  largest and
    smalles values in the given list. Will return a tuple
    '''
    # Base case
    if (len(nums) == 2):
        if (nums[0] >= nums[1]):
            result = (nums[0], nums[1])
        else:
            result = (nums[1], nums[0])
    else:
        end_tup = max_min(nums[1:])
        if (nums[0] > end_tup[0]):
            result = (nums[0], end_tup[1])
        elif (nums[0] < end_tup[1]):
            result = (end_tup[0], nums[0])
        else:
            result = end_tup
    return result


def sum_max_min(nums):
    '''(list) -> float
    This function is designed to take the sum of the smallest and largest value
    in the given list
    '''
    new_list = flatten(nums)
    if (len(new_list) == 0):
        result = 0
    elif (len(new_list) == 1):
        result = new_list[0] + new_list[0]
    elif (len(new_list) != 0):
        high_low = max_min(new_list)
        result = (high_low[0] + high_low[1])
    else:
        result = 0
    return (result)


def flatten(old_list):
    '''(list) -> list
    This function is designed as a helper function which will remove nest lists
    and return a single list containing all the elements
    '''
    if old_list == []:
        return old_list
    if isinstance(old_list[0], list):
        return flatten(old_list[0]) + flatten(old_list[1:])
    return old_list[:1] + flatten(old_list[1:])
