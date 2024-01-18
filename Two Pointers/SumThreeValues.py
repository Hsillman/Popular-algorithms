""""
Problem:
Given an array of integers, nums, and an integer value, target, 
determine if there are any three integers in nums whose sum is equal 
to the target, that is, nums[i] + nums[j] + nums[k] == target. 
Return TRUE if three such integers exist in the array. Otherwise, return FALSE.
"""

def find_sum_of_three(nums, target):
    nums.sort()

    for i in range(0, len(nums)-2):
        low = i + 1
        high = len(nums) - 1

        while low < high:
            triplet = nums[i] + nums[low] + nums[high]

            if triplet == target:
                return True
                
            elif triplet < target:
                low += 1
            
            else:
                high -= 1
    
    return False

print(find_sum_of_three([3, 7, 1, 2, 8, 4, 5],10))
"""
Time complexity

In the solution above, sorting the array takes O(nlog(n)) 
and the nested loop takes O(n2) to find the triplet. Here, n is 
the number of elements in the input array. Therefore, the total time 
complexity of this solution is O(nlog(n)+n2),nwhich simplifies to O(n2)O(n2).

Space complexity

The space complexity of this solution can range from O(log(n)) to O(n), 
as per the sorting algorithm we use. We use the built-in Python function, sort(), 
so the space complexity of the provided solution is O(n).
"""