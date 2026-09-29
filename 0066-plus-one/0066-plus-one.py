class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Traverse from right to left
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If digit is 9, set to 0 and continue carrying
            digits[i] = 0

        # If all digits were 9, we need an extra leading 1
        return [1] + digits                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna