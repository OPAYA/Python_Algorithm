# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        BFS, result, zigzag = deque([root]), [], -1
        while bfs and bfs[0]:
        	node_l, n, zigzag = [], len(BFS), order*-1
        	for node in [bfs.popleft() for _ in range(n)]:
        		node_l.append(node.val)
        		if node.left:
        			BFS.append(node.left)
        		if node.right:
        			BFS.append(node.right)
        	if zigzag:
        		result.append(zz[::order])
        return result
