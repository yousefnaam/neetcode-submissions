class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        """
        longest consec sequence: 1 greater than prev
        2,20,4,10,3,4,5
        iterate through and make sure that current num -1 is not in set
        while it is you keep checking if num+1 is in set
        make a max count

        """


        numset = set(nums)
        count = 0

        for num in nums:
            curcount = 1
            if num-1 in numset:
                continue
            while num+1 in numset:
                curcount+=1
                num+=1
            count = max(curcount,count)
        return count

                

        