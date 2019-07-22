def rotated_array_search(input_array, target):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    pivot = search_pivot(input_array)
    last_index = len(input_array)-1

    if input_array[0] < input_array[last_index]:
        return binary_search_recursive(input_array, target, 0, last_index)
    elif target > input_array[0]:
        return binary_search_recursive(input_array, target, 0, pivot - 1)
    elif target < input_array[0]:
        return binary_search_recursive(input_array, target, pivot, len(input_array) - 1)
    else:
        return 0


def binary_search_recursive(array, target, start_index, end_index):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2
    mid_element = array[mid_index]

    if mid_element == target:
        return mid_index
    elif target < mid_element:
        return binary_search_recursive(array, target, start_index, mid_index - 1)
    else:
        return binary_search_recursive(array, target, mid_index + 1, end_index)


def search_pivot(input_array):
    left_index = 0
    right_index = len(input_array) - 1

    if input_array[left_index] < input_array[right_index]:
        return left_index

    while left_index < right_index:
        mid_index = (left_index + right_index) // 2

        if input_array[mid_index] > input_array[mid_index + 1]:
            return mid_index + 1
        elif input_array[mid_index] < input_array[mid_index - 1]:
            return mid_index

        if input_array[mid_index] > input_array[right_index]:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_search_pivot(input_array, expected):
    index = search_pivot(input_array)
    if index == expected:
        print("Success")
    else:
        print("Fail")

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_search_pivot([4, 5, 6, 7, 8, 0, 1, 2, 3], 5)
test_function([[4, 5, 6, 7, 8, 0, 1, 2, 3], 8])

test_search_pivot([4, 0, 1, 2, 3], 1)
test_function([[4, 0, 1, 2, 3], 4, 0])

test_search_pivot([0, 1, 2, 3], 0)
test_function([[0, 1, 2, 3], 3, 3])

test_search_pivot([2, 3, 4, 0, 1], 3)
test_function([[2, 3, 4, 0, 1], 3, 1])

test_search_pivot([1, 2, 3, 4, 0], 4)
test_function([[1, 2, 3, 4, 0], 4, 3])

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
