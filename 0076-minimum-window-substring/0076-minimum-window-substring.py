class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Check edge cases based on string lengths
        if len(s) == 0 or len(t) == 0 or len(s) < len(t):
            return ""
        
        # Frequency map for string t
        mapT = {}
        for c in t:
            mapT[c] = mapT.get(c, 0) + 1
            
        required = len(mapT)
        l, r = 0, 0
        create = 0
        ans = [-1, 0, 0]
        subStringMap = {}
        
        while r < len(s):
            c = s[r]
            # Update frequency in sliding window map
            subStringMap[c] = subStringMap.get(c, 0) + 1
            
            # If current character frequency matches the required frequency in t
            if c in mapT and subStringMap[c] == mapT[c]:
                create += 1
                
            # Try to shrink the window from the left side
            while l <= r and required == create:
                c = s[l]
                # Save the smallest window details found so far
                if ans[0] == -1 or ans[0] >= r - l + 1:
                    ans[0] = r - l + 1
                    ans[1] = l
                    ans[2] = r
                    
                # Reduce frequency as we slide the left pointer out
                subStringMap[c] -= 1
                if c in mapT and subStringMap[c] < mapT[c]:
                    create -= 1
                    
                l += 1
            r += 1
            
        # Return empty string if no window was found, otherwise return the substring
        if ans[0] == -1:
            return ""
        else:
            return s[ans[1] : ans[2] + 1]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna