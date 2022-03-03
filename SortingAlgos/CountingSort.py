from typing import List
'''
- Counting sort is a sorting technique based on keys between a specific range. 
- It works by counting the number of objects having distinct key values (kind of hashing). 
- Then doing some arithmetic to calculate the position of each object in the output sequence.
- This algorithm is made for poisitive ranges only.
- Time complexity is O(n).
- Space complexity is O(n) where n is the range of numbers that need to be sorted.
'''
class CountingSort:
    def countingSort(self, nums: List[int]) -> None:
        # numbers from 0 to 2
        count = [0,0,0]
        for i in range(0,len(nums)):
            count[nums[i]] = count[nums[i]] + 1
        for i in range(1,len(count)):
            count[i] = count[i] + count[i-1]
        count = [0] + count[:-1]
        for i in range(0,len(count)):
            if i == len(count)-1:
                nums[count[i]:] = (len(nums)-count[i])*[i]
            else:
                nums[count[i]:count[i+1]] = (count[i+1]-count[i])*[i]
        
        return nums



s = CountingSort()
# Only number 0,1 and 2
print(s.countingSort([1, 4, 1, 2, 7, 5, 2]))