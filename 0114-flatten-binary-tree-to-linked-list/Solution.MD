### Flatten Binary Tree to Linked List (Pre‑order, In‑place)

**Problem**  
Transform a binary tree into a right‑skewed “linked list” that follows **pre‑order** traversal (root → left → right).  
Each node’s `right` points to the next node, and `left` is set to `None`.

**Core Idea**  
Use **post‑order recursion** that returns the **tail** of the flattened subtree.  
The tail allows O(1) connection of the left part to the original right part.

**Why a separate helper (`flattenTree`)?**  
The main method `flatten` returns `void`. The recursion needs to **return the tail** (a `TreeNode`) to link the parts efficiently.  
Doing it without a tail forces traversing the left list each time → O(n²). The helper keeps it O(n).

**Recursive Algorithm (post‑order)**  
1. **Base cases**  
   - `node == None` → return `None`  
   - Leaf (no left/right) → return `node` (tail is itself)

2. **Recursive calls**  
   `leftTail = flattenTree(node.left)`  
   `rightTail = flattenTree(node.right)`

3. **Rewiring (if left subtree exists)**  
   - `leftTail.right = node.right`   // attach left tail to original right child  
   - `node.right = node.left`        // move left subtree to right  
   - `node.left = None`              // clear left pointer

4. **Return the overall tail**  
   - Pre‑order is: root → left → right  
   - If right subtree exists, its tail is the last node → return `rightTail`  
   - Else, the left tail is the last node → return `leftTail`

**Why `rightTail if rightTail else leftTail`?**  
Because in pre‑order, the right subtree is visited **after** the left.  
So the final node of the flattened subtree is the tail of the right side (if it exists), otherwise the left tail.

**Complexity**  
- **Time:** O(n) – each node processed once.  
- **Space:** O(h) recursion stack (h = height). Worst case O(n) for skewed tree.

**Key Pitfalls**  
- Forgetting to set `node.left = None` after moving.  
- Returning the wrong tail (left instead of right when right exists) → breaks connection.  
- Not handling the case where left child is `None` (no rewiring needed, just return appropriate tail).

**Technique Trigger**  
> “Flatten to pre‑order linked list → post‑order recursion that returns tail. Connect left tail to right child, move left to right, return deepest tail.”

---

**Memory Hook**  
> *"Post‑order returns tail; left tail hooks right, swap left to right. Right tail if there, else left."*

- **Post‑order returns tail** – recursion goes left, right, then returns the tail (last node in pre‑order).  
- **Left tail hooks right** – `leftTail.right = node.right` connects the left part to the original right child.  
- **Swap left to right** – `node.right = node.left`, then `node.left = None`.  
- **Right tail if there, else left** – the overall tail is the deepest node: right tail if it exists, otherwise left tail (because pre‑order visits left before right).
