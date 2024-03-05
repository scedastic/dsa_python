from utilities import sort_test

def bubble_sort(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list


if __name__ == "__main__":
    sort_test(bubble_sort)