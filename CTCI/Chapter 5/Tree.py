class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

node = TreeNode(1)
#node.val = 1
node.left = 2
node.right = 3
print(node.left)