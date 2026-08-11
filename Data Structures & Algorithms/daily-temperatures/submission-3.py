class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        """
        30,38,30,36,35,40,28

        [38,,]
        [1, ,1]
        """

        stack = []
        res = [0] * len(temperatures)

        for idx,temp in enumerate(temperatures):

            while stack and stack[-1][0] < temp:
                num,val = stack.pop()
                res[val] = idx-val
            stack.append((temp,idx))
        return res


        