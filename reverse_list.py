import random


def reverse_list(arr):
    for i in range(len(arr) // 2):
        n = len(arr)
        s = arr[i]
        arr[i] = arr[n - 1 - i]
        arr[n - 1 - i] = s
    return arr


test_arr = []
for item in range(10):
    test_arr.append(random.randint(1, 50))
