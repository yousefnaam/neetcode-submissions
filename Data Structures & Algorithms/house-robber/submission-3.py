class Solution:
    def rob(self, nums: List[int]) -> int:

        #return max of nums[n] + nums[n-2], nums[n-1]

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1]) 
        
        prev1,prev2 = 0,0 
        for n in nums:
            prev2, prev1 = prev1, max(n + prev2, prev1)
        return prev1



        