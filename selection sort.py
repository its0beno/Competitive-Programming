
class Solution:

    def select(self, arr, i):
        min = i
        size = len(arr)
        for check in range(i, size):
            if (arr[check] < arr[min]):
                min = check

        return min

    def selectionSort(self, arr, n):
        for index in range(n):
            selected_index = self.select(arr, index)
            arr[index], arr[selected_index] = arr[selected_index], arr[index]
