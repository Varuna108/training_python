import random


def min_max(arr):
    min_of_list = arr[0]
    max_of_list = arr[0]

    for item in arr:
        if item < min_of_list:
            min_of_list = item
        if item > max_of_list:
            max_of_list = item
    return [min_of_list, max_of_list]


list_of_values = []
for value in range(100):
    list_of_values.append(random.randint(1, 50))
