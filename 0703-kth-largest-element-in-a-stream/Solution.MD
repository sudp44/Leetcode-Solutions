**Kth Largest Element in a Stream**

---

**Problem**  
Design a class that receives a stream of numbers and can return the kth largest element at any time.

**Core Technique**  
Maintain a **min‑heap of size exactly k**.  
The smallest element in this heap is the kth largest overall.

**Initialization**  
- `self.k = k`  
- `self.min_heap = []`  
- For each initial number, call `add(num)` to build the heap.

**`add(val)` logic**  
1. If `len(heap) < k` → push `val` (still collecting enough elements).  
2. Else if `val > heap[0]` (the current kth largest):  
   - Pop the smallest (it drops out of the top‑k).  
   - Push `val` (now part of the top‑k).  
3. Return `heap[0]` (always the kth largest).

**Why min‑heap?**  
- We want to quickly know the **smallest among the k largest** elements.  
- The root of a min‑heap gives O(1) access to that element.  
- When a new value arrives that's larger than the root, the root is no longer in the top‑k, so we remove it and insert the new value.

**Complexity**  
- Initial build: O(n log k)  
- Each `add`: O(log k)  
- Space: O(k)

**Python Code Snippet**  
```python
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]
```

**Common Mistakes**  
- Using a max‑heap instead of min‑heap (it would give the kth smallest).  
- Forgetting to handle the case where the heap has fewer than `k` elements (just push).  
- Popping and pushing when `val` equals the root (not necessary; only strictly greater required).  
- Not maintaining the heap property after each operation.

**Memory Hook**  
> *"Min‑heap of size k. Root = kth largest. If new > root, pop root and push new. Always return root."*
