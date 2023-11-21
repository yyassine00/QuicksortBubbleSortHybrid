import time
# Quicksort implementation
def quick_sort(arr):
    # Base case: if the array is empty or has only one element, it is already sorted
    if len(arr) <= 1:
        return arr
    # Select a pivot element (in this case, the middle element)
    pivot = arr[len(arr)//2]
    # Partition the array into elements less than, equal to, or greater than the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # Recursively sort the left and right partitions, and concatenate with the middle elements to form the final sorted array
    return quick_sort(left) + middle + quick_sort(right)

# Optimizing Bubble Sort implementation
def bubble_sort(arr):
    n = len(arr)
    # Iterate through the array multiple times
    for i in range(n):
        # Set a flag to False before each pass through the array
        swapped = False
        # Compare adjacent elements and swap them if they are out of order
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swaps are made during the pass, the flag remains False and the function exits early
        if not swapped:
            break
    # Return the sorted array
    return arr

  
# Combined algorithm to find optimal k
def hybrid_sort(arr, k):
    if len(arr) <= k:
        return bubble_sort(arr)
    else:
        left = hybrid_sort(arr[:len(arr) // 2], k)
        right = hybrid_sort(arr[len(arr) // 2:], k)
        return quick_sort(left + right) 

def time_sort(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time