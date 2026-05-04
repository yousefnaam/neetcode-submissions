class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            
            if stone1 - stone2 != 0:
                heapq.heappush(heap,-(stone1-stone2))
        
        if len(heap) == 1: 
            return -heap[-1]
        else:
            return 0


            

        