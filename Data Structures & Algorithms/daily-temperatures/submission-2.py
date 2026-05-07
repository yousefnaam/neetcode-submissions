class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        #[30,38,30,36,35,40,28]
        #stack = [40,28]
        #[1,]
        res = [0] * len(temperatures)

        stack = []
        for i,temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                _,index = stack.pop()
                res[index] = i - index
            stack.append((temp,i))
        
        return res



        
        