"""Given a sorted and rotated array arr[] of size N and a key, the task is to find the key in the array.
    Note: Find the element in O(logN) time and assume that all the elements are distinct.

Approach #1:
    Find the pivot point, divide the array into 2 subarrays and perfor a binary search.
    For a sorted array, the pivot point is where the the next element is smaller than the previous.
    After the pivot point is found, divide the array into 2 sub-arrays.
    Continue with binary search.
"""
import random

def pivotedBinarySearch(arr, n, key):
    """Searches an element key in a pivoted sorted array of size n

    Args:
        arr (array): array
        n (int): size of arr
        key (int): element we are looking for
    """
    pivot = findPivot(arr, 0, n-1)

    # If we did not find a pivot, the array is not pivoted
    if pivot == -1:
        return binarySearch(arr, 0, n-1, key)
    
    # If we found aa pivot, compare key with pivot and then search in 2 subarrays around pivot
    if arr[pivot] == key:
        return pivot
    
    # key is between arr[0] and pivot
    if arr[0] <= key:
        return binarySearch(arr, 0, pivot-1, key)
    
    # key is between pivot and arr[n]
    return binarySearch(arr, pivot + 1, n-1, key)

def findPivot(arr, low, high):
    """Finds pivot location

    Args:
        arr (array): array
        low (int): low end 
        high (int): high end
    """

    # base cases
    if high < low:
        return -1
    if high == low:
        return low
    
    mid = int((low + high)/2)

    # bounds check, mid is pivot
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    # bounds check, (mid - 1) is pivot
    if mid > low and arr[mid] < arr[mid-1]:
        return (mid - 1)
    
    # pivot is in the left half
    if arr[low] >= arr[mid]:
        return findPivot(arr, low, mid-1)
    
    # pivot is in the right half
    return findPivot(arr, mid + 1, high)

def binarySearch(arr, low, high, key):
    """Typical binary search - O(log n)"""
    if high < low:
        return -1
    
    mid = int((low + high)/2)

    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binarySearch(arr, mid + 1, high, key)
    return binarySearch(arr, low, mid - 1, key)

if __name__ == "__main__":
    random.randrange(1, 100)
    