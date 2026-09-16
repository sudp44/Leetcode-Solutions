**Binary Tree Right Side View**

---

**Problem**  
Given a binary tree, return the values of the nodes you would see if you looked at the tree from the right side. That is, for each level, return the rightmost node's value.

**Example**  
```
    1
   / \
  2   3
   \   \
    5   4
```
Output: `[1, 3, 4]`

**Core Technique**  
BFS (level‑order traversal) using a queue. For each level, process all nodes and record the **last** node's value.

**Algorithm Steps**  
1. If `root` is `None`, return `[]`.  
2. `result = []`, `queue = deque([root])`.  
3. While `queue` is not empty:  
   - `level_size = len(queue)`  
   - For `i` in `range(level_size)`:  
     - `current = queue.popleft()`  
     - If `i == level_size - 1`: `result.append(current.val)`  
     - If `current.left`: `queue.append(current.left)`  
     - If `current.right`: `queue.append(current.right)`  
4. Return `result`.

**Python Code (canonical)**  
```python
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        queue = deque([root])
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                current = queue.popleft()
                if i == level_size - 1:
                    result.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        return result
```

**Complexity**  
- **Time:** O(n) – each node visited once.  
- **Space:** O(w) – queue holds at most the width of the tree (O(n) worst case). Output takes O(h) additional.

**Key Insights**  
- BFS processes nodes level by level, left to right.  
- The last node in each level is the rightmost node.  
- Using `deque` for O(1) `popleft()` and `append()`.  
- `level_size` captures the number of nodes at the current level before adding children.

**Common Mistakes**  
- Forgetting to capture `level_size` before the inner loop → levels get mixed.  
- Using a list instead of `deque` → O(n²) time due to `pop(0)`.  
- Not checking `if not root` at the start.  
- Adding children before checking `i == level_size - 1` (order doesn't matter, but be consistent).

**Memory Hook**  
> *“BFS by level. The last node of each level is the right side view.”*  
> Or: *“Queue, level size, record last node's value.”*
