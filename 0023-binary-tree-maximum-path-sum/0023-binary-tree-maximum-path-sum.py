# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.max_sum = float('-inf')
        self.max_gain(root)
        return self.max_sum
    
    def max_gain(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        # Max gain from left and right subtrees (ignore negative gains)
        left_gain = max(self.max_gain(node.left), 0)
        right_gain = max(self.max_gain(node.right), 0)

        # Best path that goes through this node as the highest point
        price_new_path = node.val + left_gain + right_gain
        self.max_sum = max(self.max_sum, price_new_path)

        # Return the max gain if we continue upward through this node
        return node.val + max(left_gain, right_gain)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna