**Reorder List**:

---

### Goal
Rearrange list from `L0→L1→…→Ln-1→Ln` into `L0→Ln→L1→Ln-1→L2→Ln-2→…` **in‑place**.

---

### Core Idea (Three‑step process)
1. **Find middle** – slow/fast pointers (`slow = slow.next`, `fast = fast.next.next`).  
   `slow` ends at the start of the second half.
2. **Reverse second half** – standard iterative reversal from `slow` to end.  
   After reversal, `prev` is head of reversed second half.
3. **Merge two halves** – interleave first half (`head`) and reversed second half (`prev`).

---

### Merge Loop – Key Details

**Why `while second.next`? (not `while second`)**
- For **odd** length, the two halves share the last node.  
  If we looped until `second` is null, we would make the shared node point to itself, creating a cycle.  
  `while second.next` stops exactly one step before the shared tail, avoiding the self‑loop.

**Why save `temp1 = first.next` and `temp2 = second.next` before rewiring?**
- We need to **remember the next unmerged nodes** because `first.next` and `second.next` are about to be overwritten.
- After inserting `second` after `first` and connecting `second.next` to `temp1`, we advance:
  - `first = temp1` (next node of original first half)
  - `second = temp2` (next node of reversed second half)

**Merge code snippet:**
```python
while second.next:
    temp1 = first.next
    temp2 = second.next
    first.next = second
    second.next = temp1
    first = temp1
    second = temp2
```

---

### Complexity
- **Time:** O(n) – three linear passes.
- **Space:** O(1) – only a few pointers.

---

### Edge Cases / Common Mistakes
- Empty list or single node → nothing to do.
- Forgetting to use `while second.next` → cycle for odd length.
- Not saving `first.next` / `second.next` before modifying them → lost nodes.
- Using extra arrays (cheating) → not O(1) space. This pointer method is the intended solution.

---

### Memory Hook
> “Middle, reverse, merge — stop before the shared tail (`while second.next`) to keep it acyclic.”
