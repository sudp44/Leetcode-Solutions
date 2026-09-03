**Invert Binary Tree**

---

**Problem**  
Given the root of a binary tree, invert the tree (swap left and right children at every node) and return the new root.

**Core Technique**  
Recursive post‑order traversal. Swap children after inverting subtrees.

**Algorithm Steps**  
1. Base case: if `root` is `None`, return `None`.  
2. Recursively invert the left subtree: `left = invertTree(root.left)`.  
3. Recursively invert the right subtree: `right = invertTree(root.right)`.  
4. Swap: `root.left = right`, `root.right = left`.  
5. Return `root`.

**Python Code (canonical)**  
```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # Recursive swap
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root
```

**Alternatively, more concise**  
```python
def invertTree(self, root):
    if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    return root
```

**Complexity**  
- **Time:** O(n) – each node visited once.  
- **Space:** O(h) – recursion stack, h = height of tree.

**Key Insights**  
- Inversion = swapping left and right subtrees at each node.  
- The order of recursion doesn't matter as long as you swap correctly.  
- Can also be done iteratively with a stack/queue (BFS or DFS).

**Edge Cases**  
- Empty tree → return `None`.  
- Single node → left/right both `None`, swap does nothing, returns node.

**Common Mistakes**  
- Swapping values instead of node pointers.  
- Forgetting to store inverted subtrees before assignment (if you do `root.left = invertTree(root.right)` and `root.right = invertTree(root.left)` in the wrong order, you may overwrite the original reference). Use temporary variables or simultaneous assignment.  
- Returning `None` for non‑empty root (must return root).

**Memory Hook**  
> *"Invert = swap left and right. Recursively invert children first, then swap them."*  
Or: *"Post‑order: invert left, invert right, swap."*
