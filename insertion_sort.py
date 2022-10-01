
def insertionSort1(n, arr):
    min = arr[n-1]
    j = n-2
    while j >= 0 and arr[j] > min:
        arr[j+1] = arr[j]
        j = j-1
        print(*arr)
    arr[j+1] = min
    print(*arr)


insertionSort1(5, [2, 4, 6, 8, 3])
