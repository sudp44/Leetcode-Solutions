class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n
        pre = 1
        post = 1

        for i in range(n):
            result[i] = pre
            pre = pre * nums[i]

        for i in range(n-1, -1, -1):
            result[i] = post * result[i]
            post = post * nums[i]
        
        return result
        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna