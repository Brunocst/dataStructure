def heapify(arr, n ,i):

    largest = i
    l = 2*i +1
    r = 2*i + 2

    if l< n and arr[i] < array[l]:
        largest = l
    
    if r < n and arr[largest] < array[r]:
        largest = r

    if largest != i:
        array[largest], array[i] = array[i], array[largest]
        heapify(array, n, largest)



array = [1, 2, 3]

heapify(array, 3, 0)
print(array)