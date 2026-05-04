class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeros = nums.count(0)

        if zeros > 1:
            return [0] * n
        if zeros == 1:
            total = 1
            zeroindex = nums.index(0)
            res = [0] * n
            for num in nums:
                if num != 0:
                    total *= num
            res[zeroindex] = total
            return res
        total = 1
        for num in nums:
            total *= num
        return [total // num for num in nums] 

            
                



        