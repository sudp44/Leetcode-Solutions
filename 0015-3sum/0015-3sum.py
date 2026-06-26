class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum2(nums, i, result)
            
        return result
    
    def twoSum2(self, nums: list[int], i: int, result: list[list[int]]) -> None:
        left = i+1
        right = len(nums)-1

        while left < right:
            sum = nums[left] + nums[right] + nums[i]

            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left-1]:
                    left += 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna