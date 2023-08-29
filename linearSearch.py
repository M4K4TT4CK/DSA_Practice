# Searching an ordered array
# Sorted arrays cannot have dupliate numbers 

# Non ordered
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where the target element is found
    return -1  # Return -1 if the target element is not found

# if __name__ == "__main__":
# # Example usage:
#     my_list = [1, 3, 5, 7, 9, 11, 13]
#     target_element = 7

#     result = linear_search(my_list, target_element)

#     if result != -1:
#         print(f"Element {target_element} found at index {result}")
#     else:
#         print(f"Element {target_element} not found in the list")
    
    
    
