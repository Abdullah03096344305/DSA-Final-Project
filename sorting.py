from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys
import traceback

class Sorting(QMainWindow):
    def __init__(self):
        super(Sorting, self).__init__()

    def bubblesort(self, arr, col_name, sort_type):
        n = len(arr)
        for i in range(1,n):
            swapped = False
            for j in range(1,n - 1):
                if sort_type == "ascending":
                    if arr[j][col_name] > arr[j + 1][col_name]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swapped = True
                else:
                    if arr[j][col_name] < arr[j + 1][col_name]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swapped = True
            if not swapped:
                break
        return arr

    def callingfunction(self, algorithm, arr, indextosort, ascending):
        try:
            if algorithm == "insertionsort":
                return self.InsertionSort(arr, indextosort, ascending)
            elif algorithm == "merge_sort":
                return self.merge_sort(arr, indextosort, ascending)
            elif algorithm == "quicksort":
                return self.quicksort_2d(arr, indextosort, ascending)
            elif algorithm == "selectionsort":
                return self.selectionsort(arr, indextosort, ascending)
            elif algorithm == 'radixsort':
                return self.RadixSort(arr, indextosort, ascending)
            elif algorithm=='countingsort':
                return self.countingSort(arr, indextosort, ascending)
            elif algorithm =='bucketsort':
                return self.bucket_sort_2d(arr, indextosort, ascending)

            else:
                return self.bubblesort(arr, indextosort, ascending)
            
        except Exception as e:
            print(f"An error occurred: {e}")
            traceback.print_exc()

    def InsertionSort(self, array, column, order):
        for i in range(1, len(array)):
            j = i - 1
            key = array[i]
           
            while j >= 1 and ((order == 'ascending' and key[column] < array[j][column]) or
                             (order == 'descending' and key[column] > array[j][column])):
                array[j + 1] = array[j]
                j -= 1
        
            array[j + 1] = key
        return array

    def selectionsort(self, arr, col_name, sort_type):
        for i in range(1,len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if sort_type == "ascending":
                    if arr[j][col_name] < arr[min_idx][col_name]:
                        min_idx = j
                else:
                    if arr[j][col_name] > arr[min_idx][col_name]:
                        min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def merge_sort(self, arr, col_name, sort_type):
        try:
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = arr[1:mid]
            right = arr[mid:]

            left = self.merge_sort(left, col_name, sort_type)
            right = self.merge_sort(right, col_name, sort_type)

            return self.merge(left, right, col_name, sort_type)
        except Exception as e:
            print(f"An error occurred: {e}")

    def merge(self, left, right, col, sort_type):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if (left[i][col] < right[j][col] and sort_type == "ascending") or (left[i][col] > right[j][col] and not sort_type == "ascending"):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def quicksort_2d(self, arr, col_name, sort_type):
        if len(arr) <= 1:
            return arr

        pivot_row = arr[len(arr)//2]
        pivot_value = pivot_row[col_name]

        left = [row for row in arr[1:] if row[col_name] < pivot_value]
        middle = [row for row in arr[1:] if row[col_name] == pivot_value]
        right = [row for row in arr[1:] if row[col_name] > pivot_value]

        if sort_type == "ascending":
            return self.quicksort_2d(left, col_name, sort_type) + middle + self.quicksort_2d(right, col_name, sort_type)
        else:
 
            return self.quicksort_2d(right, col_name, sort_type) + middle + self.quicksort_2d(left, col_name, sort_type)
        
        #radix sort
    def InsertionSorting(self,array, exp, column, Type):
        for i in range(2, len(array)):
            j = i - 1
            key = array[i]
            if Type == 'ascending':
                while j >= 1 and key[column] // exp < array[j][column] // exp:
                    array[j + 1] = array[j]
                    j -= 1
                array[j + 1] = key
            else:
                while j >= 1 and key[column] // exp > array[j][column] // exp:
                    array[j + 1] = array[j]
                    j -= 1
                array[j + 1] = key

    def RadixSort(self,array, column, Type):
        max_element = max(array[1:], key=lambda x: x[column])[column]
        exp = 1
        while max_element // exp > 0:
            self.InsertionSorting(array, exp, column, Type)
            exp = exp * 10
        return array
    
    #counting sort 
    def countingSort(self,arr, column, Type):
    # Extract the column values to sort
        array=arr[1:]
        values = [item[column] for item in array]
        m = max(values)
        n = min(values)

        Count = [0] * int((m - n + 1))
        output = [0] * len(array)

        for val in values:
            k = int(val - n)
            Count[k] += 1

        for i in range(1, len(Count)):
            Count[i] += Count[i - 1]
        if Type == 'ascending':
            for i in range(len(array) - 1, -1, -1):
                j = int(values[i] - n)
                Count[j] -= 1
                output[Count[j]] = array[i]
        elif Type == 'descending':
            for i in range(len(array)):
                j = int(values[i] - n)
                output[Count[j]] = array[i]
                Count[j] += 1

        return output
   # odd_even
    def bucket_sort_2d(self,array, col_index, sort_type):
        arr=array[1:]
    # Determine the range of values in the specified column
        min_val = min(row[col_index] for row in arr)
        max_val = max(row[col_index] for row in arr)

    # Create buckets
        num_buckets = len(arr)  # Number of buckets = number of rows
        buckets = [[] for _ in range(num_buckets)]

    # Distribute elements into buckets
        for row in arr:
            value = row[col_index]
            bucket_index = int((value - min_val) / (max_val - min_val) * (num_buckets - 1))
            buckets[bucket_index].append(row)

    # Sort buckets
        for bucket in buckets:
            if sort_type == 'ascending':
                bucket.sort(key=lambda x: x[col_index])
            elif sort_type == 'descending':
                bucket.sort(key=lambda x: x[col_index], reverse=True)

    
        sorted_arr = [item for bucket in buckets for item in bucket]

        return sorted_arr
    #def multi sorting
    def multi_sort(data, columns, sort_order='ascending'):
        def custom_key(item):
            return [item[column] for column in columns]

        def merge_sort(data):
            if len(data) <= 1:
                return data

            mid = len(data) // 2
            left = data[:mid]
            right = data[mid:]

            left = merge_sort(left)
            right = merge_sort(right)

            return merge(left, right)

        def merge(left, right):
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if custom_key(left[i]) < custom_key(right[j]):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])

            return result

        sorted_data = merge_sort(data)

        if sort_order == 'descending':
            sorted_data = sorted_data[::-1]

        return sorted_data

                    
                   
                
             
    



    
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Sorting()
    window.show()
    sys.exit(app.exec_())
