class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        occurance = [0]*26
        maxOccurance = 0
        ans = 0

        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            occurance[idx] += 1
            
            maxOccurance = max(occurance[idx], maxOccurance)

            if ((right-left+1) - maxOccurance) > k:
                occurance[ord(s[left]) - ord('A')] -= 1
                left += 1

            ans = max(ans, right-left+1)   

        return ans    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna