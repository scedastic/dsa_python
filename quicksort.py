from utilities import get_random_array, sort_test 
"""Quicksort moves smaller elements to the left of a pivot. Then recursively divides the array into 2 partitions.
    Time complexity best case n log(n), 
        average: n log(n)
        worst case n**2 -- when arr is already sorted.
    Space complexity log(n) - recursion
    Two methods are shown below, BroCode looks cleaner.
"""
# Function to find the partition position
def partition(array, low, high):
 
    # Choose the rightmost element as pivot
    pivot = array[high]
    # Pointer for greater element
    i = low - 1
 
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i 
            # otherwise, j keeps moving while i stays put.
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
            
    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# Function to perform quicksort: GeeksForGeeks
def quicksort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)
         
        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)
        # print(f"Array is: {array}")
 
######################################################################################### 
def quicksort_brocode(arr, start, end):
    if(end <= start):
        return
    pivot = partition_brocode(arr, start, end)
    quicksort_brocode(arr, start, pivot - 1)
    quicksort_brocode(arr, pivot + 1, end)
    
def partition_brocode(arr, start, end):
    """All elements to the "Left" will be smaller than the pivot and all elements to the right will be greater.
    i & j start at `start` j moves along the array. If j > pivot then i and j swap positions and i moves one position over. 
    When j reaches the end, we swap it with the pivot and now the pivot is in the right spot.

    Args:
        arr (list): Array of unsorted ints
        start (int): starting point in the array
        end (int): ending point in the array

    Returns:
        int: location of the pivot
    """
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] < pivot:  # If the number is less than pivot, swap it
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i]) # below is the non-pythonic way
            # temp = arr[i]
            # arr[i] = arr[j]
            # arr[j] = temp
    
    # Place the pivot in its proper place
    i += 1  
    (arr[i], arr[end]) = (arr[end], arr[i])

    return i



# Driver code
if __name__ == '__main__':
    arr = get_random_array(7,1,20)
    print(arr)
    print("GeeksForGeeks Method")
    quicksort(arr, 0, len(arr) - 1)
    print(arr)
    print("Reseting array to random.\nBro code (youtube) method.")
    arr = get_random_array(20, -4, 50)
    quicksort_brocode(arr, 0, len(arr) - 1)
    print(arr)
