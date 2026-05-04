class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        res = []
        
        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            cur = queue.popleft()
            res.append(cur)

            for nei in adj[cur]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        if len(res) == numCourses:
            return res
        else:
            return []
