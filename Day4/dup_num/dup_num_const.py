'''
    Notables:
        can not modify the array
        must have a constant space complexity
        must have beeter than expodential time complexity
    Plan
    - use a pointer and move it along the list
    - check each instance in the list after the pointer
    - would this be n log n?
    - It would be faster then nested loops, which ARE exponential
    - I think this is the best solution I can come up with considering the constraints
    ---- Does not pass
    - I can not think of a way to complete this under these constraints
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        
        pointer = 0
        
        while pointer < len(nums) - 1:
            dup_check = nums[pointer]
            
            for i in range(pointer + 1, len(nums)):
                if dup_check == nums[i]:
                    return dup_check
            
            pointer += 1
            
        return -1