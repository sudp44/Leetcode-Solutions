class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        ans = nums[0]

        if len(nums) == 1:
            return nums[0]

        while(left <= right):
            if nums[left] < nums[right]:
                ans = min(ans, nums[left])
                break
            
            mid = (left+right)//2
            ans = min(ans, nums[mid])

            if (nums[left] <= nums[mid]):
                left = mid+1  #left side is sorted so pivot should be in right side
            else:
                right = mid-1

        return ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna