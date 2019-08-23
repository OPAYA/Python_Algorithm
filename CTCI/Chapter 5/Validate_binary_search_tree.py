# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        lst = []
        def recursive(node: TreeNode):
           
            if node==None:
                return 
           
            recursive(node.left)
            lst.append(node.val)
            recursive(node.right)
            
        recursive(root)
        
        prev = float('-inf')
        for curr in lst:
            print(curr)
            if prev >= curr:
                return False
            prev = curr
        
        return True