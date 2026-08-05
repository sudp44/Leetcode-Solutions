class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Min‑heap to store the k largest elements seen so far
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)   # remove the smallest among k+1 elements
        # The root of the min‑heap is the kth largest element
        return min_heap[0]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna