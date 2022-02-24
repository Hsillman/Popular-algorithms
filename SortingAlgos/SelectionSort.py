from typing import List
class SelectionSort:
    def selectionSort(self,arr: List[int]) -> List[int]:
        '''
        - Time complexity for this algorithm is O(n^2) because of the nested for loop.
        - Space complexity is 0(1).
        '''
        for i in range(0,len(arr)):
            current_minimum = i
            for j in range(i+1,len(arr)):
                if arr[j] < arr[current_minimum]:
                    current_minimum = j
            arr[i],arr[current_minimum] = arr[current_minimum],arr[i]
        return arr

s = SelectionSort()
print("Selection Sort:", s.selectionSort([2,8,5,3,9,4,1]))