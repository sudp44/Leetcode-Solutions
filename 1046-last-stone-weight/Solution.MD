**Last Stone Weight**, covering both `heapq` (list + `heapq`) and `PriorityQueue`

---

**Problem**  
Repeatedly smash the two heaviest stones. If `x == y`, both are destroyed; if `x != y`, the stone of weight `y‑x` remains. Return the weight of the last stone, or `0` if none.

**Core Technique**  
Simulate a **max‑heap** using a min‑heap by storing **negative** weights. The heaviest stone becomes the smallest negative → first to pop.

---

### Implementation 1 – `heapq` (lighter, preferred)

```python
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)                # push negative

        while len(heap) > 1:
            y = -heapq.heappop(heap)               # heaviest
            x = -heapq.heappop(heap)               # second heaviest
            if x != y:
                heapq.heappush(heap, -(y - x))     # remainder as negative

        return -heap[0] if heap else 0
```

**Notes**  
- `heapq` operates on a plain list, no thread‑safety overhead.  
- Always check `len(heap) > 1` before popping two.  
- Return `-heap[0]` safely because the heap has exactly one element or is empty.

---

### Implementation 2 – `PriorityQueue`

```python
from queue import PriorityQueue

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = PriorityQueue()
        for s in stones:
            pq.put(-s)

        while pq.qsize() > 1:
            y = -pq.get()
            x = -pq.get()
            if x != y:
                pq.put(-(y - x))

        return -pq.get() if pq.qsize() == 1 else 0   # NOTE: qsize() with parentheses!
```

**Notes**  
- `PriorityQueue` is thread‑safe (unnecessary here, but works).  
- **Critical bug avoidance:** `qsize` is a method → must call `qsize()`. Missing parentheses makes it a function object, which is truthy even when queue empty → `get()` raises `Empty`.

---

### Complexity  
- **Time:** O(n log n) – up to n push/pop operations, each O(log n).  
- **Space:** O(n) for the heap/queue.

---

**Common Mistakes**  
- Forgetting to negate when pushing back the remainder.  
- Using `len(heap)` or `pq.qsize()` incorrectly (missing `()` for `qsize`).  
- Not handling the case where heap becomes empty (should return 0).  
- For `heapq`, directly accessing `heap[0]` without checking emptiness (safe if we ensure at most one element).

**Memory Hook**  
> *"Max‑heap from min‑heap: store negatives. Pop two largest (negatives first), smash, push back remainder if non‑zero. Last stone weight or zero."*
