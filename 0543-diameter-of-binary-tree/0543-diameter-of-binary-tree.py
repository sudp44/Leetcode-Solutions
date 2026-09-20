# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.getHeight(root)
        return self.max_diameter
    
    def getHeight(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        
        left_height = self.getHeight(node.left)
        right_height = self.getHeight(node.right)

        self.max_diameter = max(self.max_diameter, left_height+right_height)

        return 1+max(left_height,right_height)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna