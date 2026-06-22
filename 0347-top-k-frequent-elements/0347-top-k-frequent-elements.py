from collections import Counter
from queue import PriorityQueue

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        count = Counter(nums)

        heap = PriorityQueue()

        for num in count.keys():
            heap.put((count[num], num))
            if heap.qsize() > k:
                heap.get()
        
        ans = [0]*k
        for i in range(k):
            freq, val = heap.get()
            ans[i] = val
        
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna