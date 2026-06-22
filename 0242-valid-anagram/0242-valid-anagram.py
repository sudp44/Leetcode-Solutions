class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        charCounts = [0]*26
        for i in range(len(s)):
            charCounts[ord(s[i]) - ord('a')] += 1
            charCounts[ord(t[i]) - ord('a')] -= 1
        for count in charCounts:
            if (count != 0):
                return False
        return True
# TC: O(n), SC: O(1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna