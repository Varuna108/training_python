import random


def transpose_matrix(arr):
    first = []
    for first_item in range(len(arr[0])):
        second = []
        for second_item in range(len(arr)):
            third = arr[second_item][first_item]
            second.append(third)
        first.append(second)
    arr = first
    return arr


test_arr = []
for item_one in range(3):
    temp_arr = []
    for item_two in range(2):
        temp_arr.append(random.randint(1, 50))
    test_arr.append(temp_arr)
