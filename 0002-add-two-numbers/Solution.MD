**Add Two Numbers**:

---

**Problem**  
Two non‑empty linked lists, each represents a number in reverse order (least significant digit first). Return a new linked list representing the sum, also in reverse order.

**Core Idea**  
Simulate digit‑by‑digit addition with a carry, just like elementary maths. Use a dummy node to simplify building the result list.

**Key Steps**
1. `dummy = ListNode(0)` – fixed anchor; `ans = dummy` – moving pointer.
2. `carry = 0`.
3. **While** `l1 or l2 or carry` (continue while any digit remains or there's a pending carry):
   - `x = l1.val if l1 else 0` (same for `y`).
   - `total = x + y + carry`.
   - `digit = total % 10`   ← **ones place, put in node**.
   - `carry = total // 10`   ← **tens place, carry forward**.
   - `ans.next = ListNode(digit)` – create and link new node.
   - `ans = ans.next` – move builder forward.
   - If `l1`: `l1 = l1.next`; if `l2`: `l2 = l2.next`.
4. Return `dummy.next` (actual head of the sum list).

**Critical Order (common mistake)**  
- `digit = total % 10` (**not** `carry = total % 10`).  
- `carry = total // 10` (**not** `digit = total // 10`).  
- Always create node first (`ListNode(digit)`) then attach, never try `ans.next.val = digit` because `ans.next` is `None`.

**Why `dummy`?**  
- Avoids special handling for the first node.  
- Keep `dummy` fixed, move `ans` to build. Return `dummy.next` (skip the placeholder).

**Complexity**  
- **Time:** O(max(m,n)) – one pass over both lists.  
- **Space:** O(max(m,n)) for the output list; extra variables O(1).

**Edge Cases**  
- Different lengths (shorter list is treated as 0).  
- Final carry creates an extra node (e.g., `5+5` → `0→1`).  
- Both lists empty? Problem guarantees non‑empty, but loop condition `carry` handles it.

**Memory Hook**  
> *“Digit is the remainder (%), carry is the quotient (//). Add first, link a new node, then move on.”*
