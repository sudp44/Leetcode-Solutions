class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        
        hm = {}
        
        for i in range(n):
            k = target-nums[i]
            if k in hm:
                return [hm[k], i]
            else:
                hm[nums[i]] = i
        return []

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna