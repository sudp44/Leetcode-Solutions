# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        self.prev = None
        return self.inorder(root)
    
    def inorder(self, node: Optional[TreeNode]) -> bool:
        if node is None:
            return True

        if not self.inorder(node.left):
            return False
        
        if self.prev is not None and node.val <= self.prev:
            return False
        self.prev = node.val
        
        return self.inorder(node.right)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna