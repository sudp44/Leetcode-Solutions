**Logic: Reverse a Linked List (Iterative)**

- **Core idea**: Reverse `next` pointers one node at a time using three pointers.

- **Pointers**:  
  `prev` = already reversed portion (initially `None`)  
  `curr` = current node being reversed (starts at `head`)  
  `temp` = saves remaining list before breaking the link

- **Steps**:  
  1. `prev = None`, `curr = head`  
  2. **While** `curr != None`:  
     a. `temp = curr.next` — save next node  
     b. `curr.next = prev` — reverse link  
     c. `prev = curr` — move prev forward  
     d. `curr = temp` — move curr forward  
  3. **Return** `prev` (new head)

- **Invariant**: At each step, `prev` is the head of the already‑reversed part, and `curr` is the first node of the remaining part.

- **Time**: O(n) — one pass.  
- **Space**: O(1) — only three variables.

**Visual snippet (after one iteration)**:
```
null ← 1    2 → 3 → 4
       ↑    ↑
      prev  curr
```
Then `curr` moves to 2, `prev` to 1, and so on.
