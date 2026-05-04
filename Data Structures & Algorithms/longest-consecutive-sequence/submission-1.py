class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        if len(nums) == 0:
            return 0
        longest = 1

        for num in nums:
            if num-1 not in numset:
                current = 1
                inset = num
                while inset+1 in numset:
                    current +=1
                    inset +=1
                longest = max(longest, current)
        return longest




        """

        nums = [2,20,4,10,3,4,5]


        longest:




        """



        