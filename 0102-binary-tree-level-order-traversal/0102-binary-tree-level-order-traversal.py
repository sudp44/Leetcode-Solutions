# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        self._order(root, 0, ans)
        return ans
    
    def _order(self, node, level, ans):
        if len(ans) == level:
            ans.append([])
        ans[level].append(node.val)

        if node.left:
            self._order(node.left, level+1, ans)
        if node.right:
            self._order(node.right, level+1, ans)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna