class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #This technique is called Binary Search on Answer. You use it when the input data is messy, but the range of potential answers is perfectly sequential and sorted.

        #The Golden Rule of Binary Search Templates: To keep it incredibly simple, match your loop condition to your pointers:If your code uses right = mid, your loop condition must be left < right.If your code uses right = mid - 1, your loop condition must be left <= right (and you must save the answer in a separate variable along the way)

        left = 1
        right = max(piles)

        while(left < right):
            mid = (left+right)//2

            if self.canFinish(piles, mid, h):
                right = mid
            else:
                left = mid + 1
        
        return left

    def canFinish(self, piles: List[int], speed: int, h: int):
        hours = 0
        for pile in piles:
            hours += (pile + speed -1)//speed
        return hours <= h

         

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna