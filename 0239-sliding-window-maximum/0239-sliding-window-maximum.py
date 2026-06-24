class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0:
            return []
        
        n = len(nums)
        result = [0] * (n-k+1)
        queue = deque()

        for i in range(n):
            # Remove indices that are out of the current window
            while queue and queue[0] < i-k+1:
                queue.popleft()
            
            # Remove indices whose corresponding values are less than nums[i]
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            
            # Add the current index to the deque
            queue.append(i)

            # Add the maximum element of the current window to the result
            if i >= k-1:
                result[i-k+1] = nums[queue[0]]
        
        return result
            

            
            




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna