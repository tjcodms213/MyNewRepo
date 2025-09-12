def binary_search(arr, target):
    left, right = 0, len(arr) - 1


    
    # Start of binary search
    while left <= right:
        mid = (left + right) // 2

        # Mid evaluation comment
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Return -1 when not found
    return -1


if __name__ == "__main__":
    numbers = [2, 3, 4, 10, 40]
    target = 10
    # Searching for the target value
    result = binary_search(numbers, target)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in array")
