class MyQueue:
    def __init__(self):
        self.in_stack = []   # used as a stack (append/pop)
        self.out_stack = []  # used as a stack

    def push(self, x: int) -> None:
        """Enqueue element x (O(1))."""
        self.in_stack.append(x)

    def pop(self) -> int:
        """Remove and return the front element (amortized O(1))."""
        self._move_if_needed()
        return self.out_stack.pop()

    def peek(self) -> int:
        """Return the front element without removing it (amortized O(1))."""
        self._move_if_needed()
        return self.out_stack[-1]

    def empty(self) -> bool:
        """Return True if the queue is empty, False otherwise."""
        return not self.in_stack and not self.out_stack

    def _move_if_needed(self) -> None:
        """Transfer elements from in_stack to out_stack when out_stack is empty."""
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna