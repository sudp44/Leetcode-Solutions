# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        results = []
        node_queue = deque([root, None])   # None acts as a level delimiter
        level_list = deque()
        is_order_left = True

        while node_queue:
            curr_node = node_queue.popleft()

            if curr_node is not None:
                # Add to the correct end based on current direction
                if is_order_left:
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)

                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)

            else:
                # Finished scanning one level
                results.append(list(level_list))
                level_list = deque()

                # Add a delimiter for the next level if more nodes remain
                if node_queue:
                    node_queue.append(None)

                is_order_left = not is_order_left

        return results

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna