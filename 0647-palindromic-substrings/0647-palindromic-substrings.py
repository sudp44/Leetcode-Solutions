class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        for i in range(len(s)):
            ans += self.checkPalindrome(s, i, i)
            ans += self.checkPalindrome(s, i, i+1)
        return ans
    
    def checkPalindrome(self, s: str, left: int, right: int) -> int:
        count = 0
        while(left >= 0 and right<len(s) and s[left] == s[right]):
            left -= 1
            right += 1
            count += 1
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna