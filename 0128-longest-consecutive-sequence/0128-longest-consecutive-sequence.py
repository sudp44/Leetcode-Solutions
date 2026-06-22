class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 :
            return 0
        
        numSet = set(nums)
        lcs = 1

        for num in numSet:
            currentNum = num
            if (currentNum-1) in numSet:
                continue
            else:
                cs = 1
                while(currentNum+1) in numSet:
                    cs += 1
                    currentNum += 1
                if (cs>lcs):
                    lcs = cs
        
        return  lcs


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna