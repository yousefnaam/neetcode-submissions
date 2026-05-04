class Solution:
    def maxArea(self, heights: List[int]) -> int:


        right = len(heights) - 1
        left = 0
        maxvolume = 0

        while left < right:


            volume = min(heights[left], heights[right]) * (right - left)
            maxvolume = max(maxvolume,volume)

            if heights[left] < heights[right]:
                left +=1
            elif heights[left] > heights[right]:
                right -=1
            else:
                left+=1
                right-=1
        return maxvolume







        