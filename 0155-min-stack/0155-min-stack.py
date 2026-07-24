class MinStack:
    class Node:
        def __init__(self, val: int, min_val: int, next_node: Optional['MinStack.Node']):
            self.val = val
            self.min = min_val
            self.next = next_node

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if self.head is None:
            self.head = self.Node(val, val, None)
        else:
            self.head = self.Node(val, min(val, self.head.min), self.head)

    def pop(self) -> None:
        if self.head:
            self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna