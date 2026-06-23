class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        left = 0
        right = 0
        ans = 0
        char_set = set()

        while(right < len(s)):
            c = s[right]
            # Shrink the window from the left until the duplicate is removed
            while c in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(c)
            ans = max(ans, right-left+1)
            right += 1
        
        return ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna