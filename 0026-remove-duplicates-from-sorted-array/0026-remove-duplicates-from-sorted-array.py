class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_index = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[insert_index] = nums[i]
                insert_index += 1

        return insert_index        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna