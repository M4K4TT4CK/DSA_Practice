# binary search is O(log N)
# for every bit of data doubled the algorithm only requires one additional step
# binary search onyl work on ordered lists

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Target element found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    return -1  # Target element not found in the list

# Example usage:

if __name__ == '__main__':
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    target_element = 9

    result = binary_search(sorted_list, target_element)

    if result != -1:
        print(f"Element {target_element} found at index {result}")
    else:
        print(f"Element {target_element} not found in the list")

        