from utilities import sort_test
    """Merge Sort: Recursively split the array in half. Once you reach size == 1, join it with its sibling in order. As you keep going up (in size) you end up "zipping" the 2 subarrays in order.

    Time Complexity: O(n log(n)) (for best worst and average cases.)
        The list is divided in half, to a maximum of Log(n) parts. The merging of all subarrays takes O(n) time.

    Space Complexity: O(n) 

    """
def merge_sort(list):
    left = 0
    right =  len(list) - 1
    sort_helper(list, left, right)
    return list

def sort_helper(list, left, right):
    # divide and conquer: recursively call on both halves of the list separately
    if left < right:
        mid = left + (right - left) // 2
        sort_helper(list, left, mid)
        sort_helper(list, mid + 1, right)

        merge(list, left, mid, right)

def merge(list, left, mid, right):
    """Copy the array into 2 temp arrays - each containing half the current array. 
    Using the `left` offset, compare the members of both arrays. The lower value goes into the (next) position in `list`

    Args:
        list (list[]): List of integers
        left (int): index of the left
        mid (int): divider of the 2 subarrays
        right (int): index of the right
    """
    left_half_size = mid - left + 1
    right_half_size = right - mid
    
    # Split the array
    # left_half = list[:left_half_size] -- Buggy
    
    left_half = []
    for i in range(left_half_size):
        left_half.append(list[left + i])

    # right_half = list[mid + 1:] -- This was causing "off-by-1" errors 
    right_half = []
    for j in range(right_half_size):
        right_half.append(list[mid + 1 + j])

    # Merge them in order
    left_index = 0
    right_index = 0
    main_index = left
    while left_index < left_half_size and right_index < right_half_size:
        
        # Element in the left array is smaller, put that in
        if left_half[left_index] <= right_half[right_index]:
            list[main_index] = left_half[left_index]
            left_index += 1
        # Element in the right array is smaller, put that in
        else:   
            list[main_index] = right_half[right_index]
            right_index += 1
        main_index += 1

    # Copy remaining elements (if the length of the arrays are not the same)
    while left_index < left_half_size:
        list[main_index] = left_half[left_index]
        left_index += 1
        main_index += 1

    while right_index < right_half_size:
        list[main_index] = right_half[right_index]
        right_index += 1
        main_index += 1



if __name__ == "__main__":
    sort_test(merge_sort)