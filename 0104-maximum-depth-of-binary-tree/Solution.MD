**quick recall notes** for **Maximum Depth of Binary Tree** (LeetCode 104).

---

**Problem**  
Given the root of a binary tree, find its maximum depth (the number of nodes along the longest path from the root down to the farthest leaf).

**Core Technique**  
Recursive DFS (bottom‑up). The depth of a node is `1 + max(depth of left child, depth of right child)`.

**Algorithm Steps**  
1. Base case: if `root` is `None` (empty tree), return `0`.  
2. Recursively compute `left_depth = maxDepth(root.left)`.  
3. Recursively compute `right_depth = maxDepth(root.right)`.  
4. Return `1 + max(left_depth, right_depth)`.

**Python Code (canonical)**  
```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
```

**Complexity**  
- **Time:** O(n) – each node visited exactly once.  
- **Space:** O(h) – recursion stack, where h is the height of the tree. Worst case O(n) for skewed tree, O(log n) for balanced.

**Key Insights**  
- It’s a post‑order traversal: we first compute depths of children, then the current node.  
- The height of a tree equals `1 + max(left height, right height)`.  
- Leaf nodes have height 1; empty nodes height 0.

**Edge Cases**  
- Empty tree → return 0.  
- Single node → left and right both 0, returns 1.  
- Skewed tree (like linked list) → recursion depth equals n.

**Common Mistakes**  
- Forgetting the base case (`if not root`).  
- Using `min` instead of `max`.  
- Adding 1 before the recursive call (e.g., `1 + self.maxDepth(root.left)` incorrectly).  
- Not returning the value (missing `return`).

**Memory Hook**  
> *“Height = 1 + taller child.”*  
Or: *“Max depth = max(left, right) + 1.”*
