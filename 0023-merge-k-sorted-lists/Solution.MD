**Merge k Sorted Lists** (using a min‑heap / PriorityQueue)

---

**Problem**  
Given an array of `k` sorted linked lists, merge them into one sorted linked list.

**Core Idea (Simple Heap Approach)**  
Collect **all node values** into a min‑heap.  
Then keep extracting the smallest value and building a new sorted list.

**Steps**
1. Create a `PriorityQueue` (or `heapq` list).  
2. Iterate over every list: for each node, `min_heap.put(node.val)`.  
3. Build result list:
   - `dummy = ListNode(1)`, `merge = dummy`.
   - `while not min_heap.empty():`  
     `val = min_heap.get()`  
     `merge.next = ListNode(val)`  
     `merge = merge.next`
4. Return `dummy.next`.

**Time & Space Complexity**
- **Time:** O(N log N) where N = total nodes. Each push/pop is O(log N).  
- **Space:** O(N) for the heap.

**Common Mistakes / Pitfalls**
- ❌ `while min_heap:` – does **not** work with `PriorityQueue` (object is always truthy).  
  ✅ Use `while not min_heap.empty():` instead.
- ❌ `merge.next = val` – `val` is an integer, not a `ListNode`.  
  ✅ Always wrap: `merge.next = ListNode(val)`.
- Alternative lightweight approach: use `heapq` + list: `heapq.heappush(heap, val)` / `heapq.heappop(heap)`.
- For optimal O(N log k) solution, push only the head of each list into the heap along with list index, then advance the chosen list. But the simple “dump all values” is easier and passes if allowed.

**Memory Hook**  
> “Collect all values → dump into min‑heap → pop and build new list. Remember: `not empty()` check, and always `ListNode(val)`.”
