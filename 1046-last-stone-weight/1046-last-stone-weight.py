class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Create a max‑heap by pushing negative weights
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)

        # Smash the two heaviest stones repeatedly
        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)   # heaviest
            x = -heapq.heappop(max_heap)   # second heaviest
            if x != y:
                heapq.heappush(max_heap, -(y - x))   # remaining stone weight

        # Return the last stone weight, or 0 if heap is empty
        return -max_heap[0] if max_heap else 0
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna