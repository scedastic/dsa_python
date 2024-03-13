import random

def sort_test(sort_method):
    """Pass in the name of the function (without arguments). This function will test the function you pass in with a sizable array and print the results to the console.

    Args:
        sort_method (func): Sorting function.
    """
    errors = 0
    arr = random.sample(range(10000), 200)
    sorted_arr = sort_method(arr)
    for i in range(len(sorted_arr) - 1):
        if sorted_arr[i] > sorted_arr[i + 1]:
            errors += 1
            print(f"Error found: arr[{i}] == {sorted_arr[i]} > arr[{i + 1}] == {sorted_arr[i+1]}. ")
            break
    if errors == 0:
        print("Sorted successfully.")
    print("Done")

def get_random_array(size=200, low=1, high=10000):
    """Returns an `size` element array with numbers between `low` and `high` of random numbers.

    Args:
        size (int, optional): Size of array. Defaults to 200.
        low (int, optional): Lowest number allowed. Defaults to 1.
        high (int, optional): Highest number allowed. Defaults to 10000.

    Returns:
        [int]: array of ints
    """
    return random.sample(range(low, high), size)
    pass

if __name__ == "__main__":
    x = get_random_array()