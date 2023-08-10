#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# An example of using the binary search algorithm
arr = [2, 4, 6, 8, 10]
target = 8

result = binary_search(arr, target)

if result != -1:
    print("the desired number is in the index", result)
else:
    print("The desired number does not exist in the list.")

