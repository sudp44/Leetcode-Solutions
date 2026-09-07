# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        if abs(left_height-right_height) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def getHeight(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)

        return  max(left, right) + 1   

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna