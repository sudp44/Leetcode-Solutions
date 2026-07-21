"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.visited = {}                     # maps original node → cloned node
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        # If already cloned, return the existing clone
        if head in self.visited:
            return self.visited[head]

        # Clone the node (without setting next/random yet)
        clone = Node(head.val)
        self.visited[head] = clone          # store BEFORE recursion to handle cycles

        # Recursively copy the rest
        clone.next = self.copyRandomList(head.next)
        clone.random = self.copyRandomList(head.random)

        return clone
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna