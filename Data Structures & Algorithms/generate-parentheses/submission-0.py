class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        #(()), ()()

        res = []
        current = ""

        def backtrack(openp, closedp, current):

            if openp == n and closedp == n:
                res.append(current)

            if openp < n:
                backtrack(openp + 1, closedp, current + "(")
            if closedp < openp:
                backtrack(openp, closedp + 1, current + ")")
        
        backtrack(0,0,current)
        return res

            





        