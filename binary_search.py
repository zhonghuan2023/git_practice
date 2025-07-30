def binary_search(arr, target):
    """
    Performs binary search on a sorted list to find the target value.

    Args:
        arr: A sorted list of elements.
        target: The value to search for.

    Returns:
        The index of the target in the list if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# Example usage:
if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    print(f"Original list: {my_list}")

    # Search for a value that is in the list
    target_value = 7
    index = binary_search(my_list, target_value)
    if index != -1:
        print(f"Found {target_value} at index {index}")
    else:
        print(f"{target_value} not found in the list")

    # Search for a value that is not in the list
    target_value_not_found = 10
    index = binary_search(my_list, target_value_not_found)
    if index != -1:
        print(f"Found {target_value_not_found} at index {index}")
    else:
        print(f"{target_value_not_found} not found in the list")
