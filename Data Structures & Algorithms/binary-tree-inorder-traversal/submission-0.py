# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#  1,
# 2,3,
#4,5,6,7
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        
        res = []
        
        def inorder(root,res):
            if not root:
                return
            inorder(root.left,res)
            res.append(root.val)
            inorder(root.right,res)
        
        inorder(root,res)

        return res

        