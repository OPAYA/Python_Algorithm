# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        bst, result = deque([root]), []
        
        while bst and bst[0]:
            
            n =len(bst)
            result.append(bst[0].val)
            
            for node in [bst.popleft() for _ in range(n)]:
                
                if node.right:
                    bst.append(node.right)
                    
                if node.left:    
                    bst.append(node.left)
                
        return result