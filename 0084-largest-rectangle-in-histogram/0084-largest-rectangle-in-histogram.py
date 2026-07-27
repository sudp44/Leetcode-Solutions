class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []        # stores indices of bars in increasing height order
        n = len(heights)

        for i in range(n + 1):
            # Use a virtual bar of height 0 at the end to flush the stack
            current_height = heights[i] if i < n else 0

            # While the current bar is shorter than the bar at the stack's top,
            # pop and calculate the area using the popped bar as the minimum height.
            while stack and current_height < heights[stack[-1]]:
                height = heights[stack.pop()]
                # If stack is empty, the popped bar extends all the way to the left (index 0)
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna