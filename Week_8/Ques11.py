def insertion_sort(arr):
    print("Original Array:", arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

        print(f"Step {i}: {arr}")

    return arr

arr = [9, 5, 1, 4, 3]
sorted_arr = insertion_sort(arr)
print("Sorted Array:", sorted_arr)
