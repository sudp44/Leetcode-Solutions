class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        hs = set()
        for i in range(n):
            if nums[i] in hs:
                return True
            else:
                hs.add(nums[i])
            if len(hs) > k:
                hs.remove(nums[i-k])
        return False

# TC, SC: O(n)

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna