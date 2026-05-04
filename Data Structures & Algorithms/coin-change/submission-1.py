from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def dfs(start,cost):
            if start == amount:
                return cost
            if start > amount:
                return float("inf")

            res = float("inf")
            for coin in coins:
                res = min(res,dfs(start+coin,cost+1))
            return res
        
        ans = dfs(0, 0)
        return ans if ans != float("inf") else -1


            
        