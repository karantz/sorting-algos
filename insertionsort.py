import random
def insertionsort(arr):
    # the array range is from 1 to the last element 
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than the key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Place the key in its correct location
        arr[j + 1] = key
    return arr
numbers = [random.randint(0, 100) for _ in range(5)]
print("\n insertion Unsorted Array: ", numbers)
insertionsort(numbers)
print("insertion Sorted array is:", numbers)