class Solution:
    def search(self, nums: List[int], target: int) -> int:

        #how does binary search work,
        #we initialize 2 pointers at first, a low and a high
        #while l < h, we calculate a mid, which is high + low // 2

        #if nums[mid] == target, we return mid
        #else we use <> to determine if we should move the low or high pointers

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (high + low)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1


        