class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate  = nums[0]
        count = 1

        for num in nums[1:]:
            if num == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = num
                    count = 1
  
        return candidate # since we are guaranteed to have a majority element

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna