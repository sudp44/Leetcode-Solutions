# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flattenTree(root)
    

    def flattenTree(self, node: TreeNode) -> TreeNode:
         # Returns the tail of the flattened subtree rooted at `node`
        if not node:
            return None

        # Leaf node: its tail is itself
        if not node.left and not node.right:
            return node

        # Recursively flatten left and right subtrees
        leftTail = self.flattenTree(node.left)
        rightTail = self.flattenTree(node.right)

        # If left subtree exists, rewire connections
        if leftTail:
            leftTail.right = node.right    # Connect left tail to original right child
            node.right = node.left         # Move left subtree to right
            node.left = None               # Set left to None

        # Return the tail of the entire flattened subtree
        # If right tail exists, that's the overall tail; otherwise left tail is the tail
        return rightTail if rightTail else leftTail

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna