from utilities import get_random_array, sort_test

"""Insertion Sort: Compare the `key` with previous elements. If the previous element is greater than `key`, move the previous element to the next position. 
    Time Complexity: 
        Best Case: O(n) - array already sorted
        Avgerage Case: O(n**2) - array randomly sorted        
        Worst Case: O(n**2) - array reversely sorted
    Space Complexity: O(1)
    Sorts in Place
    Stable
    
    Suppose we have this array: 
    [ 8 3 5 1 4 2 ]
    Starting at index 1, key is 3. Looking at the previous number (index 0) 8 > 3 ==> move the 8 to the next position and put the key 3,  in the previous position.
    [ 3 8 5 1 4 2 ]
    Now the key moves forward to the 5 at index 2. 8 > 5 so move the 8 to where the 5 is and the 5 to where the 8 was.
    [ 3 5 8 1 4 2 ]
    1 becomes the key at index 3. 
        8 > 1 [ 3 5 1 8 4 2 ]
        5 > 1 [ 3 1 5 8 4 2 ]
        3 > 1 [ 1 3 5 8 4 2 ]
    4 becomes key at index 4.
        8 > 4 [ 1 3 5 4 8 2 ]
        5 > 4 [ 1 3 4 5 8 2 ]
        3 < 4 NO SWAP
    2 becomes key at index 5.
        8 > 2 [ 1 3 4 5 2 8 ]
        5 > 2 [ 1 3 4 2 5 8 ]
        4 > 2 [ 1 3 2 4 5 8 ]
        3 > 2 [ 1 2 3 4 5 8 ]
        1 < 2 NO SWAP
        
"""

def insertion_sort(arr):
    """Similar to sorting a hand of cards.

    Args:
        arr (list): list of ints

    Returns:
        list: The sorted array
    """
    for i in range(1, len(arr)):
        key = arr[i]

        # Move the elements of arr[0..i - 1] that are greater than `key` to 
        # one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

if __name__ == "__main__":
    arr = get_random_array(20, 1, 100)
    print(arr)
    insertion_sort(arr)
    print(f"After insertion sort:")
    print(arr)
    # sort_test(insertion_sort)   

    