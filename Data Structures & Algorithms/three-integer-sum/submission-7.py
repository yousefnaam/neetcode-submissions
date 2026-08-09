class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        input: int array, 

        """

        nums.sort()
        ans = []

        for num in range(len(nums)):
            if num > 0 and nums[num] == nums[num-1]:
                continue
            l = num + 1
            r = len(nums) - 1
            while l < r:
                cur = nums[l] + nums[r] + nums[num]
                if cur == 0:
                    ans.append([nums[l],nums[r],nums[num]])
                    while l < r and nums[l] == nums[l+1]:
                        l+=1
                    l+=1
                    r-=1
                elif cur > 0:
                    r-=1
                else:
                    l+=1
        return ans






        