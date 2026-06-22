class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        n = len(nums)
        hs = set()

        for i in range(n):
            if nums[i] in hs:
                return True
            else:
                hs.add(nums[i])
        
        return False

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna