'''
    Notables:
        The array is MOSTLY sorted
        runtime complextity needs to be log n
        there are no duplicates
        the target may not be in the array
    Planning:
    - Binary Search?
        - How would I handle the pivot?
        - Could I manage to sort the array with log n?
        - can I modify a binary search to find the pivot point?
            - then I would have the information to binary search a "chunk" of the list
    - is it keep log n time and search for the pivot point first to create two seperate arrays?
        - I can't think of a way besides mabye some sort of modified binary search?
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        print(target)
        
        if len(nums) == 0:
            return -1
        
        left = 0
        right = len(nums) - 1
        
        # NOTE: pivot will be the index of the highest value in the list
        pivot = None
        
        # Binary search for the pivot point
        while left < right:
            mid = (left + right) // 2
            value = nums[mid]
            left_value = nums[left]
            right_value = nums[right]
            
            # Check to see if the current mid is the pivot point
            if value > nums[mid - 1] and value > nums[mid + 1]:
                pivot = mid
                break
            
            # Binary searching for the pivot point
            if value > left_value:
                left = mid
            else:
                right = mid
                
        # now that we have the pivot we can decide which section of the array to do a normal binary search on
        if nums[0] <= target <= nums[pivot]:
            left = 0
            right = pivot
        else:
            left = pivot
            right = len(nums) - 1
            
        # binary search to find the value
        while left < right:
            mid = (left + right) // 2
            value = nums[mid]
            
            if value == target:
                return mid
            elif target < value:
                right = mid - 1
            else:
                left = mid + 1
            
        return -1
        