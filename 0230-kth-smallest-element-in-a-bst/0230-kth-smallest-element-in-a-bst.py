# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, root: Optional[TreeNode], arr: List[int]) -> List[int]:
        if root is None:
            return arr
        self.inOrder(root.left, arr)
        arr.append(root.val)
        self.inOrder(root.right, arr)
        return arr

    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        nums = []
        self.inOrder(root, nums)
        return nums[k-1]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna