def rotated_array_search(input, number):
    """
    Find the index by searching in a rotated sorted array
    Provided assumption: no repeating number

    Args:
       input(list): Input array to search
       number(int): Target of search
    Returns:
       int: Index or -1
    """

    # Return -1 for the case where input list is empty
    if len(input) == 0:
        return -1

    offset = 0
    search = input

    while len(search) > 2:
        mid = len(search)//2
        if search[mid] == number:
            return mid + offset

        # Check range of first half
        left_start = search[0]
        left_end = search[mid-1]

        # Check range of second half
        right_start = search[mid+1]
        right_end = search[-1]

        # Can check if any of the start or end values are equal to the number being searched?
        if left_start == number:
            return 0 + offset
        elif left_end == number:
            return mid - 1 + offset
        elif right_start == number:
            return mid + 1 + offset
        elif right_end == number:
            return len(search) - 1 + offset

        # If the rotation is within the left half (the start value is higher than the end value of this half)
        if left_start > left_end and (number >= left_start or number <= left_end):
            search = search[0:mid]
            
        # Otherwise, the left half is in linear order - does the number fall into that?
        elif left_start < left_end and left_start <= number <= left_end:
            search = search[0:mid]

        # If the rotation is within the right half (the start value is higher than the end value of this half)
        elif right_start > right_end and (number >= right_start or number <= right_end):
            search = search[mid:-1]
            offset += mid
            
        # Otherwise the right half is in linear order - does the number fall into that?
        elif right_start < right_end and right_start <= number <= right_end:
            search = search[mid:-1]
            offset += mid

        # If the number does not fit into any range
        else:
            return -1

    # Search remaining elements (should be up to 2 remaining)
    if search[0] == number:
        return offset
    elif search[-1] == number:
        return offset + len(search) - 1

    # Otherwise number not found
    return -1

def linear_search(input, number):
    for index, element in enumerate(input):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input = test_case[0]
    number = test_case[1]
    if linear_search(input, number) == rotated_array_search(input, number):
        print("Pass")
    else:
        print("Fail")


# Test case 1
test_function([[2], 2])
# Test case 2
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# Test case 3
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 10])
# Test case 4
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 20])
# Test case 5
test_function([[8, 10, 1, 2, 3, 4, 5, 6, 7], 10])
# Test case 6
test_function([[3, 4, 5, 6, 7, 8, 10, 1, 2], 10])
# Test case 7
test_function([[], 10])
# Test case 8
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 4])