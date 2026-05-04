class Solution:
    def canJump(self, nums: List[int]) -> bool:

        flag = len(nums)-1
        ptr = len(nums) - 2

        while ptr >= 0:
            if nums[ptr] + ptr >= flag:
                flag = ptr
            ptr -= 1
        
        return flag ==0



        