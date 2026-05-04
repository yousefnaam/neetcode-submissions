class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        localmin = float("inf")
        bestprice = 0

        for x in prices: 
            if x < localmin:
                localmin = x
            bestprice = max(bestprice,x - localmin)

        return bestprice
            
        