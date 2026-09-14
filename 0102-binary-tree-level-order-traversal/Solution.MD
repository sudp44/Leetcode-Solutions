**Binary Tree Level Order Traversal**

---

**Problem**  
Given a binary tree, return its level‑order traversal as a list of lists, where each inner list contains node values at that depth (left to right).

**Example**  
```
    3
   / \
  9   20
     /  \
    15   7
```
Output: `[[3], [9, 20], [15, 7]]`

---

**Core Idea**  
Use **DFS with a level parameter** (or BFS with a queue).  
- Maintain a list `ans` where `ans[level]` holds all values at that depth.  
- When visiting a node at `level`, if `len(ans) == level`, append a new empty list.  
- Then append the node’s value to `ans[level]`.  
- Recurse left and right with `level + 1`.

---

**Algorithm Steps (DFS)**  
1. If `root` is `None`, return `[]`.  
2. Define nested function `order(node, level)`.  
3. In `order`:  
   - If `len(ans) == level`: `ans.append([])`  
   - `ans[level].append(node.val)`  
   - If `node.left`: `order(node.left, level + 1)`  
   - If `node.right`: `order(node.right, level + 1)`  
4. Call `order(root, 0)` and return `ans`.

---

**Python Code (DFS – canonical)**  
```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        def order(node: TreeNode, level: int) -> None:
            if len(ans) == level:
                ans.append([])
            ans[level].append(node.val)
            if node.left:
                order(node.left, level + 1)
            if node.right:
                order(node.right, level + 1)

        order(root, 0)
        return ans
```

**Python Code (BFS – alternative)**  
```python
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(level)
        return ans
```

---

**Complexity**  
- **Time:** O(n) – each node visited once.  
- **Space:**  
  - DFS: O(h) recursion stack + O(n) output.  
  - BFS: O(w) queue + O(n) output, where w is max width.

---

**Key Insights**  
- The `if len(ans) == level` check works because we always reach a new level for the first time from its leftmost node.  
- DFS order doesn’t matter; the level parameter ensures correct placement.  
- Nested `order` function avoids passing `ans` around and keeps code clean.  
- BFS uses a queue and processes level by level naturally.

---

**Common Mistakes**  
- Forgetting to check `if not root` before calling `order`.  
- Using `len(ans) <= level` instead of `==` (would create duplicate lists).  
- Appending to `ans` instead of `ans[level]`.  
- In BFS, not capturing the current level size before the for loop, causing mixing of levels.  
- Forgetting to recurse left and right with `level + 1`.

---

**Memory Hook**  
> *“DFS with level: new list when `len(ans) == level`, append value, recurse left/right with `level+1`.”*  
> *“BFS: queue, process level by level.”*
