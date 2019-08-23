class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        stack, ret = [root], [str(id(root))]
        while stack:
            node = stack.pop()
            if not node:
                continue
            val, left, right = node.val, node.left, node.right
            s = ",".join(map(str, [id(node), val, id(left), id(right)]))
            ret.append(s)
            stack.extend([left, right])
        return "/".join(ret)
root = [1,2,3,None,None,4,5]
codec = Codec()
print(codec.serialize(root))
#codec.deserialize(codec.serialize(root))