from typing import List
class InsertionSort:
    def insertionSort(self,arr: List[int]) -> List[int]:
        '''
        - Time complexity is O(n^2) in worst case.
        - Space complexity is O(1).
        '''
        for i in range(1,len(arr)):
            j = i
            while (j > 0) and (arr[j-1] > arr[j]):
                arr[j],arr[j-1] = arr[j-1],arr[j]
                j = j -1
        return arr

s = InsertionSort()
print("Insertion Sort:", s.insertionSort([2,8,5,3,9,4,1]))