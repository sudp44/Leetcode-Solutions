# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        self.preorder_index = 0
        self.inorder_index_map = {}

        # Map each value to its index in the inorder array
        for i in range(len(inorder)):
            self.inorder_index_map[inorder[i]] = i

        return self.array_to_tree(preorder, 0, len(preorder) - 1)
    
    def array_to_tree(self, preorder: List[int], left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None

        # Pick the current root from preorder and advance the pointer
        root_value = preorder[self.preorder_index]
        self.preorder_index += 1

        root = TreeNode(root_value)

        # Build left and right subtrees using the inorder index map
        root.left = self.array_to_tree(preorder, left, self.inorder_index_map[root_value] - 1)
        root.right = self.array_to_tree(preorder, self.inorder_index_map[root_value] + 1, right)

        return root
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna