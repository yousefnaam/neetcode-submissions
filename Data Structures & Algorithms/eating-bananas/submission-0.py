class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #given an integer array and each piles represents the amount of bananas in each pile
        #we haves piles, we have h, which is the total number of hours
        # h = # of hours we have
        # k is the minimum rate in which we can eat the bananas,
        #our max rate to eat the bananas is the max of the array,
        #0 -> max[arr]
        #

        #piles = [1,4,3,2], h = 9


        r = max(piles)
        
        l = 1
        res = r

        while l <= r:
            eat = (l + r) // 2
            totaltime = 0
            for p in piles:
                totaltime += math.ceil(float(p) / eat)
            if totaltime <= h:
                res = eat
                r = eat - 1 
            else:
                l = eat + 1
        return res
                    

                    

        

        