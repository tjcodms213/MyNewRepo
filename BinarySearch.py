def binary_search(arr, target):
    left, right = 0, len(arr) - 1


    
    
    while left <= right:
        mid = (left + right) // 2

        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    
    return -1


if __name__ == "__main__":
    numbers = [2, 3, 4, 10, 40]
    target = 10
    # Searching for the target value
    result = binary_search(numbers, target)

    if result != -1:
        print(f"Rsult {result}")
    else:
        print("None")
