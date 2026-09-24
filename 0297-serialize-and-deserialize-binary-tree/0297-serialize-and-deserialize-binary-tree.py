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
        def rec_serialize(node, string):
            if node is None:
                string += "null,"
            else:
                string += str(node.val) + ","
                string = rec_serialize(node.left, string)
                string = rec_serialize(node.right, string)
            return string

        return rec_serialize(root, "")
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def rec_deserialize(nodes):
            if nodes[0] == "null":
                nodes.pop(0)
                return None
            root = TreeNode(int(nodes[0]))
            nodes.pop(0)
            root.left = rec_deserialize(nodes)
            root.right = rec_deserialize(nodes)
            return root
        
        node_list = data.split(",")
        # Remove the trailing empty string caused by the final comma
        if node_list and node_list[-1] == "":
            node_list.pop()
        return rec_deserialize(node_list)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna