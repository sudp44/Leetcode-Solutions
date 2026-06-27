class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1

        left_max = height[left]
        right_max = height[right]

        total = 0

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                total += left_max-height[left] #no redundant leftMax - height[left] > 0 checks because left_max - height[left] will naturally equal 0 whenever a new maximum is found
                left += 1
            else:
                right_max = max(right_max, height[right])
                total += right_max-height[right]
                right -= 1

        return total

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna