"""
    1st pass solution:
        - using a nested loop, check every possible combination of indicies values to see if the sum matches the target value
        - This would have O(n^2) time complexity but constant space complexity
        
    2nd pass solution: 
        - Initialize a hashtable
        - iterate through the array 
        - check if the value at [i] is in the hashtable
        - if not
            - subtracting the value at [i] from the target
            - create a hashtable entry where the key is the remainder from arr[i]-target and the value is i
        - else 
            - return the current index and the index stored in the hashtable at arr[i]'s key
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize an empty hashtable
        needed_nums = dict()
        
        # Iterate through the array
        for i in range(len(nums)):
            num = nums[i]
            
            # Check if the current num is in the needed_nums hashtable
            # If not, create a hashtable entry where the key is the remainder from target - num
            # and the value being the current index
            if num not in needed_nums:
                remainder = target - num
                needed_nums[remainder] = i
                
            # If there is a hashtable entry, return the current index, and the one stored in the hashtable
            else:
                stored_index = needed_nums[num]
                return [stored_index, i]