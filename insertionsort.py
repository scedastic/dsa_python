from utilities import sort_test

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
    sort_test(insertion_sort)

    