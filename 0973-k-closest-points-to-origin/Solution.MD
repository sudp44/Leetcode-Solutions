**K Closest Points to Origin**

---

**Problem**  
Given an array of `[x, y]` points and an integer `k`, return the `k` closest points to the origin `(0,0)`. Distance = `x² + y²`. Any order is accepted.

**Core Technique**  
Maintain a **max‑heap** of size `k` that always stores the `k` closest points seen so far.  
When size exceeds `k`, pop the farthest point (largest distance).  
At the end, the heap contains exactly the `k` closest points.

**Why max‑heap (not min‑heap)?**  
- We need to quickly evict the **worst** (farthest) point among the `k` candidates.  
- A max‑heap gives O(1) access to the largest distance.  
- Python only has a min‑heap, so we simulate max‑heap by storing **negative** distances.

---

**Implementation (`heapq`)**  

```python
import heapq

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    heap = []                           # max‑heap via negative distances
    for x, y in points:
        d = x*x + y*y
        heapq.heappush(heap, (-d, x, y))    # store as tuple
        if len(heap) > k:
            heapq.heappop(heap)             # remove farthest (smallest negative distance)
    return [[x, y] for (_, x, y) in heap]
```

**How the tuple `(-d, x, y)` works**  
- The heap is a min‑heap, so it sorts by the **first element** (`-d`) first.  
- The smallest `-d` means the largest `d` → farthest point.  
- If distances tie, Python compares `x`, then `y` – irrelevant for correctness.

**Complexity**  
- **Time:** O(n log k) – each point pushed/popped at most once.  
- **Space:** O(k) for the heap.

**Common Mistakes**  
- Forgetting to negate the distance → min‑heap would keep the farthest points instead of closest.  
- Not storing coordinates in the tuple (e.g., only storing distance) – can’t return points.  
- Using `PriorityQueue` incorrectly (must call `qsize()` with parentheses).  
- Returning heap in arbitrary order (allowed, but be aware).

**Memory Hook**  
> *"Max‑heap of size k with negative distances. Push `(-d, x, y)`, pop if >k. The heap keeps the k closest; the farthest among them is the root."*
