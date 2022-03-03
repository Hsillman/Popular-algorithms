from typing import List
class BinarySearch:
    def iterativeBinarySearch(self,arr:List[int],target:int)->int:
        '''
        - The time complexity of the binary search algorithm is O(log n). 
        - The best-case time complexity would be O(1) when the central index would directly match the desired value.
        '''
        low = 0
        high = len(arr)

        while low <= high:
            mid = (low+high)//2
            if arr[mid] > target:
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                return mid
        return -1

    def recursiveBinarySearch(self,arr:List[int],target:int,low=0,high=None)-> int:
        '''
        - For the recursive approach the space complexity will be O(logn) instead of O(1).
        - Time complexity for the recursive version remains the same.
        '''
        if high == None:
            high = len(arr)

        if low < high:
            mid = (low+high)//2
            if arr[mid] > target:
                return self.recursiveBinarySearch(arr,target,low,mid-1)
            elif arr[mid] < target:
                return self.recursiveBinarySearch(arr,target,mid+1,high)
            else:
                return mid
        else:
            return -1

        


s = BinarySearch()
print(s.recursiveBinarySearch([1,2,3,4,6,7,8,9,10,11],0))