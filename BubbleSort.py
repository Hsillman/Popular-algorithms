from typing import List
class BubbleSort:
    '''
    - Bubble Sort is an easy-to-implement, stable sorting algorithm with a 
    time complexity of O(n²) in the average and worst cases and O(n) in the best case.
    '''
    def bubbleSortCode1(self,arr: List[int]) -> List[int]:
        swap = True
        while swap:
            swap = False
            for i in range(len(arr)-1):
                if arr[i] > arr[i+1]:
                    arr[i],arr[i+1] = arr[i+1],arr[i]
                    swap = True
        return arr

    def bubbleSortCode2(self,arr: List[int]) -> List[int]:
        '''
        - This implementation of bubble sort is more efficient
        '''
        # Traverse through all array elements
        for i in range(len(arr)):
            swapped = False
            # Last i elements are already in place
            for j in range(0, len(arr)-i-1):
    
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if swapped == False:
                break
        return arr

   


s = BubbleSort()
print(s.bubblesort([5,1,4,2,8]))