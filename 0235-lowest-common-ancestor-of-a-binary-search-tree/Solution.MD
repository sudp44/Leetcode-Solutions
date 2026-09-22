**Lowest Common Ancestor of a Binary Search Tree** including the leap‑of‑faith explanation for recursion

---

## Problem
Given a **Binary Search Tree (BST)** and two nodes `p` and `q`, find their **lowest common ancestor (LCA)**.  
The LCA is the lowest node in the tree that has both `p` and `q` as descendants (a node can be a descendant of itself).

## Core Idea
In a BST:
- Left subtree values < node.val
- Right subtree values > node.val

The LCA is the **first node** where `p` and `q` “split” — i.e., one is on the left and the other on the right (or one equals the node).  
If both `p` and `q` are greater than the current node, the LCA must be in the right subtree.  
If both are smaller, it must be in the left subtree.  
Otherwise, the current node is the LCA.

## Algorithm Steps
1. Start at `root`.
2. If `p.val > root.val` **and** `q.val > root.val` → recurse on `root.right`.
3. Else if `p.val < root.val` **and** `q.val < root.val` → recurse on `root.left`.
4. Else → return `root` (this is the split point or one node equals root).

## Python Code (Recursive)
```python
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
```

## Iterative Version (O(1) space)
```python
def lowestCommonAncestor(self, root, p, q):
    while root:
        if p.val > root.val and q.val > root.val:
            root = root.right
        elif p.val < root.val and q.val < root.val:
            root = root.left
        else:
            return root
```

## Leap of Faith (Recursion)
**Contract:** `lowestCommonAncestor(node, p, q)` returns the LCA of `p` and `q` in the BST rooted at `node`.

**Leap:** Assume the recursive call on the chosen subtree (`left` or `right`) will correctly return the LCA within that subtree. You don't trace every call.

**Combine:** At the current node, you check the BST property:
- If both targets are greater, the LCA must be in the right subtree → return whatever the right recursive call returns.
- If both are smaller, it must be in the left → return whatever the left recursive call returns.
- Otherwise, they split here (or one is the current node) → the current node is the LCA, so return it.

By induction (base case: if the current node is the LCA, we return it; otherwise we recurse into the correct subtree), the function works for all BSTs.

## Complexity
- **Time:** O(h) – visit at most the height of the tree.
- **Space:** O(h) for recursion; O(1) for iterative.

## Common Mistakes
- **Missing `return` on recursive calls** → function returns `None`.  
  (This was the bug in your code: `self.lowestCommonAncestor(...)` without `return`.)
- Using this logic on a **general binary tree** (it only works for BST). For a general tree, use LeetCode 236 solution (post‑order DFS).
- Forgetting that the nodes are guaranteed to exist, so no base case for `None` is strictly needed.

## Memory Hook
> *“Both right? Go right. Both left? Go left. Otherwise, you’re the ancestor.”*

Or: *“BST LCA = first split point.”*
