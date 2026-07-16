**Merge Two Sorted Lists**:

---

### **Core Idea**
Use a **dummy node** to simplify edge cases. Repeatedly attach the smaller head of the two lists to the merged list.

---

### **Steps**
1. Create `dummy = ListNode(0)` and a pointer `merge = dummy`.
2. **While** `list1` and `list2` are both non‑empty:  
   - If `list1.val < list2.val` → attach `list1`, move `list1` forward.  
   - Else → attach `list2`, move `list2` forward.  
   - Move `merge = merge.next`.
3. **Attach the remaining list** (the one that still has nodes):  
   `merge.next = list1 if list1 else list2`
4. **Return** `dummy.next` (the real head).

---

### **Key Details & Common Mistakes**
- **Dummy node** avoids handling the empty‑list case separately.  
- **Loop condition** must be `while list1 and list2` – not `or`.  
- **Return value:** `dummy.next`, **not** `merge.next` (which is the tail).  
- **Comparison:** Use `<` or `<=`? Both work for distinct values; `<` keeps stability but doesn't matter here.

---

### **Complexity**
- **Time:** O(m + n) – each node visited once.  
- **Space:** O(1) – only pointers, no extra nodes.

---

### **Edge Cases**
- One or both lists empty → dummy.next correctly returns the other list (or `None`).  
- Lists with equal values → `else` branch picks one, no issue.

---

### **Visual Snapshot**
```
list1: 1 → 3 → 5
list2: 2 → 4

dummy → 1 → 2 → 3 → 4 → 5
```
The `merge` pointer always points to the last node added. After loop, attach remaining `list1` (5).
