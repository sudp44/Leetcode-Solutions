class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums)-2
        # Go left as long as the elements are increasing or staying the same. Stop at the first element that is smaller than the element to its right.
        while(i>=0 and nums[i+1] <= nums[i]):
            i -= 1

        if i>=0:
            j = len(nums)-1
            while(nums[j] <= nums[i]):
                j -= 1
            nums[i], nums[j] = nums[j], nums[i] #Swapping the numbers increased the value at index i

        nums[i+1:] = nums[i+1:][::-1] #to make the entire permutation as small as possible, turn this suffix into increasing order (min possible value)


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna