def linear_search_ordered(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where the target element is found
        elif arr[i] > target:
            return -1  # Since the list is ordered, if the current element is greater, the target is not in the list
    return -1  # Return -1 if the target element is not found


if __name__ == "__main__":
    ordered_list = [1, 3, 5, 7, 9, 11, 13]
    target_element = 7

    result = linear_search_ordered(ordered_list, target_element)

    if result != -1:
        print(f"Element {target_element} found at index {result}")
    else:
        print(f"Element {target_element} not found in the list")
