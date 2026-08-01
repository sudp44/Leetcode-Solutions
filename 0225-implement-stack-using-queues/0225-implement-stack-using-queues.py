from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()   # primary queue
        self.q2 = deque()   # auxiliary queue

    def push(self, x: int) -> None:
        """Push element x onto stack."""
        self.q1.append(x)

    def pop(self) -> int:
        """Removes and returns the top element (the most recently pushed)."""
        # Move all but the last element from q1 to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        # The last element in q1 is the top of the stack
        top = self.q1.popleft()
        # Swap q1 and q2 so that q1 always holds the current stack
        self.q1, self.q2 = self.q2, self.q1
        return top

    def top(self) -> int:
        """Returns the top element without removing it."""
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        top = self.q1[0]   # peek the last remaining element
        self.q2.append(self.q1.popleft())  # move it to q2 as well
        self.q1, self.q2 = self.q2, self.q1
        return top

    def empty(self) -> bool:
        """Returns True if the stack is empty."""
        return not self.q1 and not self.q2

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna