from utilities import sort_test

def heap_sort(arr):
    N = len(arr)

    # Build the heap
    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i)

    # Extract elements one by one
    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

def heapify(arr, N, i):
    """Heapify subtree rooted at index i.

    Args:
        arr (arr[]): Heap
        N (int): Size of heap
        i (int): index of the root
    """
    largest= i      # initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2

    # if the left child > root
    if left < N and arr[largest] < arr[left]:
        largest = left
    
    # if the right child > root
    if right < N and arr[largest] < arr[right]:
        largest = right

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, N, largest)    # Since we did a swap, we need to rearrange the heap
    



if __name__ == "__main__":
    sort_test(heap_sort)