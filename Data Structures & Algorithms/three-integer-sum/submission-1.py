class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for num in range(len(nums)):
            if num > 0 and nums[num] == nums[num-1]:
                continue
            l = num + 1
            r = len(nums) - 1
            while l < r:
                cur = nums[r] + nums[l] + nums[num]
                if cur == 0:
                    res.append([nums[num],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l +=1
                    while l < r and nums[l] == nums[l+1]:
                        r -=1                    
                    l+=1
                    r-=1
                elif cur > 0 and l < r:
                    r-=1
                elif cur < 0 and l < r:
                    l +=1
        return res




        