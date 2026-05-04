class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])
        
        while queue:
            node1, node2 = queue.popleft()
            
            # If both are None, continue
            if not node1 and not node2:
                continue
            
            # If one is None, but not the other → not same
            if not node1 or not node2:
                return False
            
            # If values differ → not same
            if node1.val != node2.val:
                return False
            
            # Push children pairs into the queue
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
        
        return True
