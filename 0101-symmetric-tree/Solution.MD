**Symmetric Tree**

---

**Problem**  
Given a binary tree, check whether it is a mirror of itself (symmetric around its center).  
Example:  
- Symmetric: `[1,2,2,3,4,4,3]`  
- Not symmetric: `[1,2,2,null,3,null,3]`

**Core Technique**  
Recursive mirror comparison of two subtrees. A tree is symmetric if its left and right subtrees are mirror images.

**Key Idea**  
For a tree to be symmetric, two conditions must hold for every pair of nodes `(left, right)`:
1. Both are `None` → symmetric (base case).
2. One is `None`, the other is not → not symmetric.
3. Both have the same value → then check mirror properties:
   - `left.left` mirrors `right.right`
   - `left.right` mirrors `right.left`

**Algorithm Steps**  
1. If `root` is `None` → return `True` (empty tree is symmetric).  
2. Call a helper `isMirror(root.left, root.right)`.  
3. In `isMirror(left, right)`:
   - If both `None` → return `True`.  
   - If only one `None` → return `False`.  
   - If `left.val != right.val` → return `False`.  
   - Recursively check:
     - `isMirror(left.left, right.right)` and  
     - `isMirror(left.right, right.left)`  
   - Return the `and` of both.

**Python Code (canonical)**  
```python
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return (self.isMirror(left.left, right.right) and
                self.isMirror(left.right, right.left))
```

**Complexity**  
- **Time:** O(n) – each node is visited once (n = number of nodes).  
- **Space:** O(h) – recursion stack, h = height of tree (worst case O(n) skewed, O(log n) balanced).

**Common Mistakes**  
- Missing the base case `if left is None or right is None` → `AttributeError`.  
- Forgetting to check `left.val != right.val` before recursing → wrong result because recursion only returns `True` if values match and subtrees mirror; but if values differ, it should return `False` immediately.  
- Returning `None` implicitly when values differ (forgetting `return False`). While `None` is falsy and may still work due to `and` short‑circuit, it’s bad practice and can cause confusion. Always return explicit `False`.  
- Mixing up mirror pairs: left‑left with right‑right, left‑right with right‑left.

**Key Insight – Why mirror pair order matters**  
Symmetry is not the same as equality of left and right subtrees. For two nodes to mirror:
- The left subtree of the left node must mirror the right subtree of the right node.
- The right subtree of the left node must mirror the left subtree of the right node.
That is, we compare **outer** and **inner** pairs:  
`(left.left, right.right)` and `(left.right, right.left)`.

**Memory Hook**  
> *"Two nodes mirror if values equal and left‑left mirrors right‑right, left‑right mirrors right‑left."*  
Or shorter: *"Outer mirror + inner mirror."*

**Edge Cases**  
- Empty tree → `True`.  
- Single node → `True` (both children `None`).  
- Tree with one side missing at any level → `False`.
