'''
 - Quick Sort has a time complexity of O(n^2) in worst cases.
   For best cases the time complexity becomes O(nlog(n)).
 - The space complexity is calculated based on the space used in the recursion stack. 
   The worst case space used will be O(n) . The average case space used will be of the order O(log n). 
   The worst case space complexity becomes O(n).
'''
class QuickSort:
    def partition(self,start, end, array):
        pivot = array[end]
        
        i = start
        for j in range(start,end):
            if array[j] <= pivot:
                array[j],array[i] = array[i],array[j]
                i = i + 1
        array[end],array[i] = array[i],array[end]
        return i
     
    def quick_sort(self,start, end, array):
        if (start < end):
            p = self.partition(start, end, array)
            self.quick_sort(start, p - 1, array)
            self.quick_sort(p + 1, end, array)

s = QuickSort()
array = [4,7,2,6,4,1,8,3]
s.quick_sort(0,len(array)-1,array)