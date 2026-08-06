class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        1,1,2,8
        1,6,24,48
        """

        pre = [0] * len(nums)
        suf = [0] * len(nums)
        prefix = 1
        suffix = 1
        ans = [0] * len(nums)

        for x in range(len(pre)):
            pre[x] = prefix
            prefix *= nums[x]

        for x in range(len(pre)-1,-1,-1):
            suf[x] = suffix
            suffix *= nums[x]
        
        for x in range(len(pre)):
            ans[x] = pre[x] * suf[x]
        
        return ans
            

        