import random
def selectionsort(arr):
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        # Assume the current index as the minimum
        temp = i
        # Check the rest of the array for a smaller element
        for j in range(i+1, n):
            if arr[j] < arr[temp]:
                temp = j
        # Swap the found minimum element with the current element, only if they are different
        if temp != i:
            arr[i], arr[temp] = arr[temp], arr[i]
    return arr

numbers = [random.randint(0, 100) for _ in range(5)]
print("\n selection Unsorted Array: ", numbers)
selectionsort(numbers)
print("selection Sorted array is:", numbers)
