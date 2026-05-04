class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        res = []
        nums.sort()
    


        def dfs(start,current,path):

            if current == target:
                res.append(path.copy())
                return
            if current > target:
                return
            
            for i in range(start, len(nums)):
                if current + nums[i] > target:
                    return
                path.append(nums[i])
                dfs(i,current + nums[i], path)
                path.pop()
        
        dfs(0,0,[])
        return res



'''
res = []
target = 9
start =


'''
        