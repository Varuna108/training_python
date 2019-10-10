import random


def sum_main_diagonal(arr):
    sum_of_diagonal = 0
    for item_of_mx in range(len(arr)):
        sum_of_diagonal += arr[item_of_mx][item_of_mx]
    return sum_of_diagonal


test_arr = []
for item_one in range(3):
    temp_arr = []
    for item_two in range(3):
        temp_arr.append(random.randint(1, 50))
    test_arr.append(temp_arr)
