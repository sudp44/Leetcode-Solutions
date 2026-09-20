**Subtree of Another Tree**

---

**Problem**  
Given the roots of two binary trees `root` and `subRoot`, return `True` if there is a subtree of `root` with the same structure and node values as `subRoot`, otherwise `False`.

**Core Technique**  
Recursive traversal of `root`, checking at each node if the subtree rooted there is identical to `subRoot` using a helper `isSame`.

**Algorithm Steps**  
1. If `root` is `None` → return `False` (no subtree in an empty tree).  
2. If `isSame(root, subRoot)` → return `True` (found a match).  
3. Otherwise, return `isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)` (search left or right).

**Helper `isSame(s, t)`** (Same Tree logic)  
- If both `None` → `True`.  
- If one `None` → `False`.  
- If `s.val != t.val` → `False`.  
- Return `isSame(s.left, t.left) and isSame(s.right, t.right)`.

**Python Code (corrected)**  
```python
class Solution:
    def isSame(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if s.val != t.val:
            return False
        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
```

**Complexity**  
- **Time:** O(m · n) worst case, where m = nodes in `root`, n = nodes in `subRoot`.  
  For each node in `root`, we may run an O(n) `isSame` check.  
- **Space:** O(h) recursion stack for `isSubtree`, plus O(n) for the nested `isSame` recursion.  
  Worst case O(m + n) for skewed trees.

**Key Insights**  
- `isSame` is exactly the Same Tree problem (LeetCode 100).  
- Use **`and`** in `isSame` (both subtrees must match).  
- Use **`or`** in `isSubtree` (match can be in left or right).  
- The base case `if root is None: return False` is essential; it also handles the case where `subRoot` is `None`? Actually, if `subRoot` is `None`, the problem likely considers an empty tree a subtree of any tree? But constraints say subRoot has at least 1 node, so not an issue. Still, `isSame(root, None)` would return `False` unless root is also `None`, which is fine.

**Common Mistakes**  
- Typo: `s in None` instead of `s is None` → `TypeError`.  
- Typo: `self.subTree` instead of `self.isSubtree` → `AttributeError`.  
- Forgetting to check `root is None` at the start of `isSubtree`.  
- Using `and` instead of `or` when recursing in `isSubtree`.  
- Using `or` instead of `and` in `isSame`.

**Memory Hook**  
> *"Find a node where `isSame(root, subRoot)` is true. Check left OR right. `isSame` = both left AND right."*

Or: *"Same Tree helper + traverse root with OR."*
