''' 
- This algorithm will sort an array of integers.
- Merge sort uses the devide and conquer approach.
- The recursive part of the algorithm keeps dividing the array in half.
- It is very similar to the division made in binary search as well which has time complexity of O(logn).
- So the recursive part of merge sort has time complexity of O(logn).
- However, the "while" part of merge sort visits all elements in order to order them. 
  That part has time complexity of O(n).
- So the time complexity of the whole algorithm is 0(nlogn).
- The space complexity is O(n). This means that for every value of the initial array there will be a call to a function. 
  That means that every n will occupy its own space in the memory stack. Because of that we have space complexity of O(n)

'''
def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

print(mergeSort([38,27,43,3,9,82,10]))
