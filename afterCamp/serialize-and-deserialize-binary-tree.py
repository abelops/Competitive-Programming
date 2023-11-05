# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preOrd(node):
            if not node:
                return ["*"]
            return [str(node.val)] + preOrd(node.left) + preOrd(node.right)
        return ",".join(preOrd(root))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        l = len(data)
        i = 0
        def build():
            nonlocal i
            if data[i] == "*":
                i+=1
                return None
            node = TreeNode(int(data[i]))
            i+=1
            node.left = build()
            node.right = build()
            return node
        return build()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))