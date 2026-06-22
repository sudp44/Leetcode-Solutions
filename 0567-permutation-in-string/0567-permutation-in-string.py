class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False
        
        s1Map = [0]*26
        s2Map = [0]*26

        for i in range(len(s1)):
            s1Map[ord(s1[i]) - ord('a')] += 1
            s2Map[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s2)-len(s1)):
            if (s1Map == s2Map):
                return True
            #sliding through s2, the current window didn't match so slide the window
            s2Map[ord(s2[i + len(s1)]) - ord('a')] += 1
            s2Map[ord(s2[i]) - ord('a')] -= 1
        
        #check the last window
        return (s1Map == s2Map)



         

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna