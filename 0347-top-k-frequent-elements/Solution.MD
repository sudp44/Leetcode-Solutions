**Top K Frequent Elements** using a min‑heap

---

**Problem**  
Given an array `nums` and an integer `k`, return the `k` most frequent elements (any order).

**Core Idea**  
Use a **min‑heap of size `k`** to keep the largest frequencies.  
Discard the smallest frequency when the heap exceeds `k`. After processing all elements, the heap contains exactly the top `k`.

**Steps**  
1. **Count frequencies** – `Counter(nums)` or manual dictionary.  
2. **Min‑heap of size `k`** – `PriorityQueue()` (or `heapq` list).  
   For each unique number:  
   - `heap.put((freq, num))` – push a **tuple** (frequency first).  
   - If `heap.qsize() > k` → `heap.get()` removes the smallest frequency (root of min‑heap).  
3. **Extract answer** – Pop `k` elements from the heap, collect the `num` values into a list.  
   (Order doesn’t matter, but they come out sorted by frequency ascending.)

**Why tuple `(freq, num)`?**  
- `PriorityQueue` expects **one item**; passing two arguments `(freq, num)` is wrong (interpreted as item and block).  
- Tuple comparison: first by frequency → smallest frequency stays at root.  
- Ties are broken by `num` (prevents comparing incomparable types).

**Why a min‑heap of size `k`?**  
- We want the **largest** frequencies. A min‑heap gives O(1) access to the smallest among the kept elements.  
- If a new element’s frequency is larger than that minimum, the old minimum gets evicted automatically (via push‑then‑pop).  
- Works in O(N log k) instead of O(N log N) sorting.

**Complexity**  
- **Time:** O(N log k) – `N` unique elements, each heap operation O(log k).  
- **Space:** O(N) for the frequency map + O(k) for the heap → O(N).

**Common Mistakes**  
- Forgetting to wrap `(freq, num)` as a tuple → `put(freq, num)` raises error.  
- Using `==` instead of `=` when assigning extracted values to answer list.  
- Returning heap elements in ascending frequency order (fine for any order, but be aware).  
- Using `PriorityQueue` in single‑threaded code is fine; `heapq` on a plain list is lighter.

**Memory Hook**  
> “Count, then keep only the top `k` in a min‑heap. Push tuple, pop smallest when too big.”
