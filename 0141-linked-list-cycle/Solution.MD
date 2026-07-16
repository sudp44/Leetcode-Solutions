**Linked List Cycle** (Floyd’s Tortoise and Hare):

---

### **Algorithm: Fast & Slow Pointers (Floyd’s Cycle Detection)**
- **Idea:** Two pointers move at different speeds. If there’s a cycle, they will eventually meet inside it.

---

### **Steps**
1. Initialize `slow = head`, `fast = head`.
2. **Loop:** `while fast and fast.next:`  
   - `slow = slow.next` (1 step)  
   - `fast = fast.next.next` (2 steps)  
   - **If `slow == fast`** → cycle exists, return `True`.
3. Loop exits → no cycle, return `False`.

---

### **Why the loop condition is `fast` and `fast.next`?**
- `fast` reaches `None` first (moves 2× faster) → no need to check `slow`.
- `fast.next` must exist before trying `fast.next.next` → prevents `AttributeError`.

---

### **Complexity**
- **Time:** O(n) – each node visited at most once by each pointer.
- **Space:** O(1) – only two pointers.

---

### **Edge Cases**
- Empty list (`head = None`) → loop condition `fast` is `None`, returns `False` immediately.
- Single node without cycle → `fast.next = None`, loop exits.
- Single node with cycle (points to itself) → `slow` and `fast` meet at the node.

---

**Visual Snapshot (cycle case):**
```
1 → 2 → 3 → 4
    ↑       ↓
    6 ← 5 ←
```
`slow` and `fast` eventually meet inside the loop (e.g., at node 4).
