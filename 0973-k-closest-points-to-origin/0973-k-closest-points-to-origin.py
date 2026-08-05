class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Max‑heap (store negative distance to simulate max‑heap)
        max_heap = []
        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(max_heap, (-dist, x, y))
            if len(max_heap) > k:
                heapq.heappop(max_heap)   # remove the farthest point (largest distance)
        
        # Extract the k closest points from the heap
        return [[x, y] for (_, x, y) in max_heap]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna