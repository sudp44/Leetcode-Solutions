**Diameter of Binary Tree**

---

## Problem

Given the root of a binary tree, return the length of the **diameter** of the tree.  
The diameter is the **number of edges** on the longest path between any two nodes in the tree. This path may or may not pass through the root.

**Example**
```
      1
     / \
    2   3
   / \
  4   5
```
Diameter = 3 (path 4 → 2 → 1 → 3 or 5 → 2 → 1 → 3).

---

## Core Technique

**Postorder DFS** that returns the **height** of each subtree while updating a **global maximum diameter**.

Why postorder? Because the diameter through a node depends on the heights of its left and right subtrees, which must be computed first (bottom‑up).

---

## Key Insight

For any node, the longest path **passing through it** is:

```
left_height + right_height
```

where `left_height` and `right_height` are the heights of its left and right subtrees **excluding the current node**.

- Height of an empty subtree = 0.
- Height of a leaf = 1.
- The diameter is measured in **edges**, not nodes.

The overall diameter is the maximum of this value across all nodes.

---

## Algorithm Steps

1. Initialize `self.max_diameter = 0` (instance variable to track global max).
2. Define `get_height(node)`:
   - If `node is None` → return `0`.
   - `left = get_height(node.left)`
   - `right = get_height(node.right)`
   - Update `self.max_diameter = max(self.max_diameter, left + right)`
   - Return `1 + max(left, right)` (height of this subtree, including node)
3. Call `get_height(root)`.
4. Return `self.max_diameter`.

---

## Python Code (canonical)

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.get_height(root)
        return self.max_diameter

    def get_height(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        left = self.get_height(node.left)
        right = self.get_height(node.right)

        # Diameter through this node = left + right (edges)
        self.max_diameter = max(self.max_diameter, left + right)

        # Return height (nodes) to the parent
        return 1 + max(left, right)
```

---

## Why `get_height` returns height but not diameter

- **Height** is needed by the parent to compute its own diameter (`parent_left + parent_right`).
- **Diameter** is a global property. The parent doesn’t need the child’s diameter; it only needs heights. So we store the max diameter in an instance variable.
- This two‑for‑one design lets us solve the problem in a **single pass** (O(n)).

---

## Complexity

- **Time:** O(n) – each node visited exactly once.
- **Space:** O(h) – recursion stack, where h is tree height.  
  Worst case O(n) for skewed tree, O(log n) for balanced.

---

## Why heights exclude the current node

When we do `left = get_height(node.left)`, `left` is the height of the left subtree (including the left child but not the current node).  
The path through the current node goes:
- from the deepest left node, up to the left child (that’s `left - 1` edges),
- then one edge to the current node,
- then one edge to the right child,
- then down to the deepest right node (that’s `right - 1` edges).

Total edges = `(left - 1) + 1 + 1 + (right - 1) = left + right`.

So `left + right` is exactly the diameter (in edges) through the current node.

---

## Common Mistakes

- Confusing **height in nodes** vs **diameter in edges**. The diameter is the sum of heights, no `+1` or `-1` needed.
- Returning the diameter from the recursive function instead of the height → breaks the parent’s calculation.
- Forgetting to use `self.max_diameter` (instance variable) so all recursive calls share the same max.
- Using `>` vs `>=` – doesn’t matter for max, both work.
- Forgetting the base case `if node is None: return 0`.
- Trying to compute the diameter only at the root (it may be entirely within a subtree).

---

## Memory Hook

> *“Postorder returns height; at each node, diameter = left + right; keep global max.”*

Or: *“Height up, diameter global.”*

---

## Example Walkthrough

Tree:
```
      1
     / \
    2   3
   / \
  4   5
```

| Node | left | right | left+right | max_diameter | return |
|------|------|-------|------------|--------------|--------|
| 4    | 0    | 0     | 0          | 0            | 1      |
| 5    | 0    | 0     | 0          | 0            | 1      |
| 2    | 1    | 1     | 2          | 2            | 2      |
| 3    | 0    | 0     | 0          | 2            | 1      |
| 1    | 2    | 1     | 3          | 3            | 3      |

Answer: **3**. ✅
