class MedianFinder:

    def __init__(self):
        self.lo = []   # max‑heap (store negative values to simulate)
        self.hi = []   # min‑heap (store positive values)
        

    def addNum(self, num: int) -> None:
        # Add to max‑heap (lo)
        heapq.heappush(self.lo, -num)

        # Move the largest of lo to hi (balance)
        largest_in_lo = -heapq.heappop(self.lo)
        heapq.heappush(self.hi, largest_in_lo)

        # Ensure lo's size >= hi's size (lo can have at most one more element)
        if len(self.lo) < len(self.hi):
            smallest_in_hi = heapq.heappop(self.hi)
            heapq.heappush(self.lo, -smallest_in_hi)
        

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            # Odd total count, median is the top of lo (largest of the smaller half)
            return -self.lo[0]
        else:
            # Even total count, median is average of the two middle values
            return (-self.lo[0] + self.hi[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna