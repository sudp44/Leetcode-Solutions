**Logic: Middle of the Linked List (Fast & Slow Pointers)**

- **Core idea**: Use two pointers moving at different speeds. When the faster reaches the end, the slower is exactly at the middle.

- **Pointers**:  
  `slow` = moves 1 step per iteration  
  `fast` = moves 2 steps per iteration  

- **Steps**:  
  1. Initialize `slow = head`, `fast = head`  
  2. **While** `fast` is not `None` **and** `fast.next` is not `None`:  
     - `slow = slow.next`  
     - `fast = fast.next.next`  
  3. **Return** `slow` (the middle node)

- **Why it works**:  
  - If `fast` moves twice as fast as `slow`, then when `fast` reaches the end (null), `slow` has covered exactly half the distance.  
  - For **even** number of nodes: the loop stops when `fast` is `None` (after passing the end), and `slow` points to the **second** middle node (as required by LeetCode).  
  - For **odd** number of nodes: `fast.next` becomes `None` at the last node; `slow` stops at the exact middle.

- **Invariant**: At any step, `slow` is at the middle of the traversed part, and the remaining distance for `fast` is roughly twice that of `slow`.

- **Time**: O(n) — one pass  
- **Space**: O(1) — two pointers

**Visual snippet** (even length, 4 nodes):
---
Initially:
s,f
1 → 2 → 3 → 4 → null

After 1st iteration (slow moves once, fast moves twice):
    s       f
1 → 2 → 3 → 4 → null

After 2nd iteration:
        s           f(null)
1 → 2 → 3 → 4 → null
---
