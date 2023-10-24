class SortableList:
    """
    A sortable list class
    providing methods to sort the list
    using the quick sort algorithm
    """

    def __init__(self, arr):
        self.arr = arr

    def partition(self, left_pointer, right_pointer):
        pivot_index = right_pointer
        pivot = self.arr[pivot_index]
        right_pointer -= 1

        while True:
            while self.arr[left_pointer] < pivot:
                left_pointer += 1

            while self.arr[right_pointer] > pivot:
                right_pointer -= 1

            if left_pointer >= right_pointer:
                break
            else:
                self.arr[left_pointer], self.arr[right_pointer] = (
                    self.arr[right_pointer],
                    self.arr[left_pointer],
                )
                left_pointer += 1

        self.arr[left_pointer], self.arr[pivot_index] = (
            self.arr[pivot_index],
            self.arr[left_pointer],
        )

        return left_pointer

    def quick_sort(self, left_index, right_index):
        # base case
        if right_index - left_index <= 0:
            return

        # recursive case
        pivot_index = self.partition(left_index, right_index)
        self.quick_sort(left_index, pivot_index - 1)
        self.quick_sort(pivot_index + 1, right_index)

    def quick_select(self, nth_lowest_value, left_index, right_index):
        # base case
        if right_index - left_index <= 0:
            return self.arr[left_index]

        # recursive case
        pivot_index = self.partition(left_index, right_index)
        # if what we are looking for is left of the pivot:
        if nth_lowest_value < pivot_index:
            # recursively call quick_select on the left side of the partition
            return self.quick_select(
                nth_lowest_value, left_index, pivot_index - 1
            )
        # if what we are looking for is right of the pivot:
        elif nth_lowest_value > pivot_index:
            # recursively call quick_select on the right side of the partition
            return self.quick_select(
                nth_lowest_value, pivot_index + 1, right_index
            )
        # if what we are looking for is the pivot:
        else:
            # return the pivot
            return self.arr[pivot_index]


# test the class
my_list = SortableList([5, 9, 3, 7, 2, 8, 1, 6])
my_list.quick_sort(0, len(my_list.arr) - 1)
print(my_list.arr)  # [1, 2, 3, 5, 6, 7, 8, 9]

my_second_list = SortableList([0, 50, 20, 10, 60, 30, 80, 70, 40, 90])
print(my_second_list.quick_select(1, 0, len(my_second_list.arr) - 1))
