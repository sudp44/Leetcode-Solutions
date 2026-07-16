**Remove Nth Node From End of List** (one‑pass, two‑pointer method).

---

### **Goal**
Delete the node that is `n` positions from the end of a singly linked list in one pass.

---

### **Core Idea**
Use two pointers with a **constant gap** so that when the leading pointer reaches the end, the trailing pointer is exactly **one node before** the target. A **dummy node** handles the head‑removal case uniformly.

---

### **Why `dummy` instead of `head`?**
- To delete a node, we must stand on the node **before** it.
- Starting both pointers at `dummy` (one step left of `head`) guarantees `back` lands on the predecessor of the target.
- Removes the need for a special case when deleting the head (`n == length`) — it becomes a normal deletion.

---

### **Why `n+1` gap?**
- We advance `front` by **`n+1`** steps from `dummy`.  
- When `front` becomes `None`, `back` is exactly `n+1` nodes behind → i.e., at the node just before the target.

---

### **Steps**
1. Create `dummy = ListNode(1)`, set `dummy.next = head`.
2. Set `front = dummy`, `back = dummy`.
3. Move `front` forward `n+1` steps.
4. Move both `front` and `back` until `front` is `None`.
5. Delete target: `back.next = back.next.next`.
6. Return `dummy.next` (new head).

---

### **Complexity**
- **Time:** O(L) – single pass, L = number of nodes.
- **Space:** O(1) – only two extra pointers.

---

### **Edge Cases / Common Mistakes**
- Removing the head → dummy makes it trivial.
- Single node list → dummy ensures safe deletion, returns `None`.
- Advancing `front` only `n` steps (instead of `n+1`) → `back` lands **on** target, not before it.
- Returning `head` directly after deletion (head may have changed) → always return `dummy.next`.

---

### **Memory Hook**
> “Dummy gives us the **one‑before** position; `n+1` gap keeps it there.”
