class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        localmin = prices[0]   
        localmax = 0
        stock = 0

        #localmin: 10, 1
        #stock: 0, 

        for price in prices:
            localmin = min(price,localmin)
            stock = max(stock, price - localmin)
        
        return stock


        