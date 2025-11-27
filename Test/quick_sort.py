

# no good
class QuickSort:

    def quick_sort_main(self, my_array):
        if len(my_array) > 1: self.quick_sort(my_array, 0, len(my_array) - 1)

    def quick_sort(self, my_array, left, right):
        if left < right:
            pivot = self.partition(my_array, left, right)
            self.quick_sort(my_array, left, pivot - 1)
            self.quick_sort(my_array, pivot + 1, right)

    def partition(self, my_array, left, right):
        i, j = left, right
        while i < j:
            while i < j and my_array[j] >= my_array[left]: j -= 1
            while i < j and my_array[i] <= my_array[left]: i += 1
            if i < j: my_array[i], my_array[j] = my_array[j], my_array[i]
        my_array[left], my_array[i] = my_array[i], my_array[left]
        return i

quicksort = QuickSort()
my_array = [2,5,1,8,3,23,-12,56,0,-2]

# 2 1 5 8 3
# print(solu.partition(my_array, 0, len(my_array) - 1))
print(quicksort.quick_sort_main(my_array))
print(my_array)