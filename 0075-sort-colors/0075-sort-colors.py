class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo = 0
        hi = len(nums)-1
        current = 0

        while(current <= hi):
            if nums[current] == 0:
                nums[lo], nums[current] = nums[current], nums[lo]
                lo += 1
                current += 1
            elif nums[current] == 2:
                nums[hi], nums[current] = nums[current], nums[hi]
                hi -= 1
            else:
                current += 1

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna