class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create a set to keep track of seen values
        nums_cache = set()
        
        # Iterate over the list
        for num in nums:
            
            # If the value has not been seen, add it to the catch
            if num not in nums_cache:
                nums_cache.add(num)
            
            # If the value has already been seen, return true
            else:
                return True
        
        # If there were no duplicated, then return false
        return false