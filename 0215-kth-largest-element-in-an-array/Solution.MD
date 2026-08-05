**Kth Largest Element in an Array**

---

**Problem**  
Find the `k`th largest element in an unsorted array. (Not the `k`th distinct element.)

**Core Technique**  
Maintain a **min‑heap** of size `k` that stores the `k` largest elements seen so far.  
After processing all elements, the **smallest** element in this heap is the `k`th largest overall.

---

### Implementation 1 – `heapq` (lighter, preferred)

```python
import heapq

def findKthLargest(self, nums: List[int], k: int) -> int:
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)      # discard smallest of k+1
    return heap[0]                   # root = kth largest
```

---

### Implementation 2 – `PriorityQueue`

```python
from queue import PriorityQueue

def findKthLargest(self, nums: List[int], k: int) -> int:
    pq = PriorityQueue()
    for num in nums:
        pq.put(num)
        if pq.qsize() > k:
            pq.get()                 # discard smallest
    return pq.get()                  # root of min‑heap with k elements
```

---

### How the min‑heap works  
- The heap always keeps the **k largest** numbers encountered.  
- When size exceeds `k`, we pop the **minimum** of the heap (which cannot be the `k`th largest).  
- At the end, the **minimum of the heap** is exactly the `k`th largest overall.

---

### Complexity  
- **Time:** O(n log k) – each element is pushed (and maybe popped) once; heap operations are O(log k).  
- **Space:** O(k) – the heap never holds more than `k` elements.

---

### Common Mistakes  
- Using a max‑heap (must be min‑heap to keep only top `k`).  
- Forgetting to check heap size before popping (always check `len(heap) > k`).  
- In `PriorityQueue`, forgetting parentheses: `pq.qsize()` not `pq.qsize`.  
- Trying to return `heap[0]` when heap could be empty (not an issue if `k ≤ n`, but still guard if needed).  
- If `k` is large (close to `n`), consider building a heap of `n` elements and popping `k` times (O(n + k log n)). But for small `k`, the min‑heap of size `k` is optimal.

---

**Memory Hook**  
> *“Min‑heap of size k holds the big boys. After pouring all numbers, the runt of the big boys is the kth largest.”*  
> *“Push, pop if >k, return root.”*
