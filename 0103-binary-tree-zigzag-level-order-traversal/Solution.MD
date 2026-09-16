**Binary Tree Zigzag Level Order Traversal**

---

**Problem**  
Return the zigzag level order traversal of a binary tree: level 0 left→right, level 1 right→left, level 2 left→right, alternating.

**Example**  
```
        1
       / \
      2   3
     / \   \
    4   5   6
```
Output: `[[1], [3,2], [4,5,6]]`

---

**Core Technique**  
BFS with a **`None` sentinel** to mark the end of each level.  
Use a `deque` for the node queue and another `deque` for the current level's values, inserting at the right or left depending on direction.

---

**Algorithm Steps**  
1. If `root` is `None`, return `[]`.  
2. `results = []`  
3. `node_queue = deque([root, None])` – `None` marks level end.  
4. `level_list = deque()`  
5. `is_order_left = True`  
6. While `node_queue`:  
   - `curr = node_queue.popleft()`  
   - If `curr` is not `None`:  
     - If `is_order_left`: `level_list.append(curr.val)`  
     - Else: `level_list.appendleft(curr.val)`  
     - Add `curr.left` and `curr.right` to `node_queue` if they exist.  
   - Else (sentinel):  
     - `results.append(list(level_list))`  
     - `level_list = deque()`  
     - If `node_queue` still has nodes: `node_queue.append(None)`  
     - `is_order_left = not is_order_left`  
7. Return `results`

---

**Python Code (canonical)**  
```python
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        results = []
        node_queue = deque([root, None])
        level_list = deque()
        is_order_left = True

        while node_queue:
            curr = node_queue.popleft()
            if curr is not None:
                if is_order_left:
                    level_list.append(curr.val)
                else:
                    level_list.appendleft(curr.val)
                if curr.left: node_queue.append(curr.left)
                if curr.right: node_queue.append(curr.right)
            else:
                results.append(list(level_list))
                level_list = deque()
                if node_queue:
                    node_queue.append(None)
                is_order_left = not is_order_left

        return results
```

---

**Why `deque` for `node_queue`?**  
- BFS requires **FIFO**: `popleft()` for O(1) removal from front, `append()` for O(1) addition to back.  
- A list would make `pop(0)` O(n), leading to O(n²) overall.  
- `deque` gives O(1) at both ends; it’s the standard Python queue for BFS.

**Why `deque` for `level_list`?**  
- We need to build a level in either normal or reverse order.  
- `append` (right) for left→right, `appendleft` for right→left.  
- Both are O(1) with `deque`.

---

**Complexity**  
- **Time:** O(n) – each node visited once.  
- **Space:** O(n) – queue can hold up to O(n) nodes, plus output.

---

**Key Insights**  
- The `None` sentinel marks the end of a level. After popping it, we finalize the level, add a new sentinel if more nodes remain, and flip the direction.  
- Using `appendleft` for reverse levels avoids reversing the list later.  
- The direction flag toggles after every level.

---

**Common Mistakes**  
- Forgetting to add a new `None` sentinel after finishing a level if the queue is not empty.  
- Using a list instead of `deque` for `node_queue` – causes O(n²) time.  
- Mixing up `append` and `appendleft` for the zigzag order.  
- Not checking `if not root` at the start.  
- Forgetting to convert `level_list` to a list before adding to results (if using deque).

---

**Memory Hook**  
> *“BFS with `None` sentinel. Build level in deque: append right for L→R, appendleft for R→L. On `None`, save level, add new sentinel, flip direction.”*

Or: *“Queue with sentinel, deque for zigzag, flip flag each level.”*
