import random
def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        # to check the condition that it is swapped or not
        swapped = False
        # here loop is used to check 0 to the element till it is not sorted (so here last element will be sorted)
        for j in range(0, n - i - 1):
            # If the a[j] is bigger than the a[j+1], swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swapping happened in the inner loop, the array is already sorted
        if not swapped:
            break
    return arr

numbers = [random.randint(0, 100) for _ in range(5)]
print("bubble Unsorted Array: ", numbers)
bubblesort(numbers)
print("bubble Sorted array:", numbers)