def bubbleSort(arr):
    length = len(arr)
    for i in range(length-1):
        for j in range(length - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def second_largest(arr):
    if len(arr) < 2:
        return 'List must have atleast Two elements'
    bubbleSort(arr)
    return arr[-2]

array_list = [1,5,4,8,6,90,123,345,65,476,343]
print(f'Second Largest Number : {second_largest(array_list)}')
bubbleSort(array_list)
print(array_list)