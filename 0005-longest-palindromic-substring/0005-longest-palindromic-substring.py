class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        left, right = 0, 0

        for i in range(len(s)):
            len1 = self.checkPalindrome(s, i, i)       
            len2 = self.checkPalindrome(s, i, i+1)

            max_len = max(len1, len2)

            if max_len > right - left + 1:
                left = i - (max_len-1) // 2
                right = i + max_len // 2
        
        return s[left:right+1]

    def checkPalindrome(self, s:str, left:int, right:int)-> int:
        while(left >= 0 and right<len(s) and s[left] == s[right]):
            left -= 1
            right += 1
            
        return right-left-1 #(right-1)-(left+1)+1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna