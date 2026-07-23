class Solution:
    def isValid(self, s: str) -> bool:
        # Map each closing bracket to its corresponding opening bracket
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for c in s:
            # If it's an opening bracket, push onto stack
            if c not in bracket_map:
                stack.append(c)
            else:
                # If it's a closing bracket, the stack must not be empty
                if not stack:
                    return False
                top = stack.pop()
                # The popped opening bracket must match the closing one
                if bracket_map[c] != top:
                    return False

        # If stack is empty, all brackets were correctly matched
        return not stack
                           


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna