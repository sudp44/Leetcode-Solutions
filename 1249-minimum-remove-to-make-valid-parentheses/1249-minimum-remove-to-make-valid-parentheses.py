class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove_indices = set()      # indices to be removed
        stack = []                  # stores indices of unmatched '('

        # First pass: identify unmatched parentheses
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if not stack:
                    # ')' without a matching '(' → must be removed
                    remove_indices.add(i)
                else:
                    # '(' is matched, remove it from the stack
                    stack.pop()

        # Any remaining '(' in the stack are unmatched → mark them for removal
        remove_indices.update(stack)

        # Second pass: build the result, skipping marked indices
        result = []
        for i, ch in enumerate(s):
            if i not in remove_indices:
                result.append(ch)

        return "".join(result)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna