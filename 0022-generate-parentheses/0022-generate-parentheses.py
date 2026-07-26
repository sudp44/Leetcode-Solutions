class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        # Use a list as a mutable string builder
        self.backtrack(ans, [], 0, 0, n)
        return ans

    def backtrack(self, ans: List[str], cur: List[str], open_count: int, close_count: int, max_pairs: int):
        # Base case: valid combination reached the target length (2 * max_pairs)
        if len(cur) == max_pairs * 2:
            ans.append("".join(cur))       # convert list of chars to string
            return

        # Add an opening parenthesis if we still have room
        if open_count < max_pairs:
            cur.append("(")
            self.backtrack(ans, cur, open_count + 1, close_count, max_pairs)
            cur.pop()                      # backtrack – remove the last character

        # Add a closing parenthesis if it wouldn't break the validity
        if close_count < open_count:
            cur.append(")")
            self.backtrack(ans, cur, open_count, close_count + 1, max_pairs)
            cur.pop()                      # backtrack

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna