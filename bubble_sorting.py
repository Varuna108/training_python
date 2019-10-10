import random


def bubble_sorting(arr):
    for item in range(0, len(arr)-1):
        for item_two in range(0, len(arr)-1):
            if arr[item_two] > arr[item_two+1]:
                arr[item_two], arr[item_two+1] = arr[item_two+1], arr[item_two]
    return arr


test_arr = []
for item in range(10):
    test_arr.append(random.randint(1, 50))
