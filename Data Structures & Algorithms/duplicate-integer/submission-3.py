class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """

        return: boolean if value appears more than once
        input: array

        data structure: hashset, 
        """
        
        return len(nums) != len(set(nums))

        