class Solution:
    def maxArea(self, heights: List[int]) -> int:

        ptr1 = 0
        ptr2 = len(heights) - 1
        maxwater = 0

        while ptr1 < ptr2:
            maxwater = max(maxwater, min(heights[ptr1],heights[ptr2]) * (ptr2-ptr1))

            if heights[ptr1] <= heights[ptr2]:
                ptr1+=1
            else:
                ptr2 -=1
        return maxwater
            


        