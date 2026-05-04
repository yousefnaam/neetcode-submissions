class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set() #search if exists in o(1) cost of o(n) space

        for x in nums:
            if x in seen:
                return True
            else:
                seen.add(x)
        return False
        