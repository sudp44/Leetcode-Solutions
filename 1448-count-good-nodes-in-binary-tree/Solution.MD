**Count Good Nodes in Binary Tree**

---

## Problem

Given the root of a binary tree, count the number of **good nodes**.  
A node `X` is **good** if, on the path from the root to `X`, there are **no nodes with a value greater than `X`**.  
In other words, `X` is good if `X.val >= max value seen so far` on that path.

**Example**
```
    3
   / \
  1   4
 /   / \
3   1   5
```
Good nodes: 3 (root), 3 (leftmost), 4, 5 → total **4**.

---

## Core Technique

**Preorder DFS** (root → left → right) carrying the **maximum value seen so far** along the path from the root.

Why preorder?  
Because the information (`max_so_far`) must flow **top‑down**: we need to know the maximum above a node before we can decide if the node itself is good.

---

## Algorithm Steps

1. Start with `max_so_far = -infinity` (since all node values are ≥ 0 in the problem constraints, but -inf works universally).
2. Define a recursive function `countGoodNodes(node, max_so_far)`:
   - **Base case:** if `node is None`, return `0` (empty subtree has no good nodes).
   - Initialize `count = 0` (local count for this subtree).
   - **If `node.val >= max_so_far`**:
     - `count = 1` (current node is good)
     - `max_so_far = node.val` (update the maximum for the path)
   - Recurse left: `count += countGoodNodes(node.left, max_so_far)`
   - Recurse right: `count += countGoodNodes(node.right, max_so_far)`
   - Return `count`.
3. Return `countGoodNodes(root, -inf)`.

---

## Python Code (canonical)

```python
class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        return self.countGoodNodes(root, float('-inf'))

    def countGoodNodes(self, node: Optional[TreeNode], max_so_far: int) -> int:
        if node is None:
            return 0

        count = 0
        if node.val >= max_so_far:
            count = 1
            max_so_far = node.val

        count += self.countGoodNodes(node.left, max_so_far)
        count += self.countGoodNodes(node.right, max_so_far)
        return count
```

---

## Complexity

- **Time:** O(n) – each node visited exactly once.
- **Space:** O(h) – recursion stack, where h is the height of the tree.  
  Worst case O(n) for a skewed tree, O(log n) for a balanced tree.

---

## Key Insights (Why the code works)

- **Preorder is necessary** because the parent’s value (and the max above it) must be known before checking children.  
- **`>=` not `>`** – a node that ties the current maximum is still good (no strictly greater value on the path).  
- **Base case `None` returns 0** – `None` is not a node; it has no value, so it cannot be good. Returning 0 correctly handles empty subtrees.  
- **`count = 0` inside each call** – each recursive call counts good nodes **only in its own subtree**. The parent aggregates children’s counts by addition.  
- **Root is always good** – because `max_so_far` starts at `-inf` and `root.val >= -inf` is always true.

---

## Common Mistakes

- Using `>` instead of `>=` → misses nodes that tie the maximum.
- Forgetting the base case `if node is None: return 0` → `AttributeError` when accessing `node.val`.
- Updating `max_so_far` but not using the updated value in recursive calls (i.e., passing the old max).
- Trying to use a global/nonlocal counter without proper resetting → messy and error‑prone.
- Using postorder or inorder by mistake → incorrect max propagation.

---

## Memory Hook

> *“Preorder DFS carrying max. If node ≥ max, it’s good and max updates. Count left + right. Base: None → 0.”*

Or shorter:  
> *“Top‑down max, count good nodes, recurse left and right.”*

---

## Example Walkthrough (for quick mental check)

Tree:
```
    3
   / \
  1   4
 /   / \
3   1   5
```

- `3`: max=-inf → good, max=3 → count=1
- left `1`: max=3 → 1≥3? No → count=0
  - left `3`: max=3 → 3≥3? Yes → good, count=1, max stays 3
- right `4`: max=3 → 4≥3? Yes → good, count=1, max=4
  - left `1`: max=4 → 1≥4? No → count=0
  - right `5`: max=4 → 5≥4? Yes → good, count=1
- Total = 1 + 0 + 1 + 1 + 0 + 1 = 4 ✅

---

These notes should give you everything you need for a quick and thorough review.
