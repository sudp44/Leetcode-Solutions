**Balanced Binary Tree** (LeetCode 110)

---

**Problem**  
Given a binary tree, determine if it is height‑balanced. A balanced tree is one where the left and right subtrees of every node differ in height by at most 1.

**Core Technique**  
Recursive height calculation + recursive balance check. This is a **top‑down** approach (not optimal, but simple).

**Algorithm Steps**  
1. If `root` is `None` → return `True` (empty tree is balanced).  
2. Compute `left_height = getHeight(root.left)`.  
3. Compute `right_height = getHeight(root.right)`.  
4. If `abs(left_height - right_height) > 1` → return `False`.  
5. Otherwise, recursively check that both left and right subtrees are balanced:  
   `return self.isBalanced(root.left) and self.isBalanced(root.right)`.

**Helper `getHeight(node)`**  
- If `node` is `None` → return `0`.  
- Recursively compute left and right heights, return `max(left, right) + 1`.

**Python Code (canonical)**  
```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_h = self.getHeight(root.left)
        right_h = self.getHeight(root.right)
        if abs(left_h - right_h) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getHeight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return max(self.getHeight(node.left), self.getHeight(node.right)) + 1
```

**Complexity**  
- **Time:** O(n²) in worst case because for each node, `getHeight` traverses its entire subtree. This is inefficient; the optimal bottom‑up approach is O(n).  
- **Space:** O(h) for recursion stack.

**Why this approach is not optimal**  
- Repeatedly computes heights of the same subtrees.  
- Better solution: use a **bottom‑up** DFS that returns height and checks balance in one pass, giving O(n) time.  
  (If asked, mention you can optimise by returning `-1` or a tuple.)

**Common Mistakes**  
- Forgetting to call `isBalanced` on both subtrees after checking the root’s height difference.  
- Confusing height with depth; height is number of edges on longest path to leaf, here we use nodes count (`None` returns 0).  
- Not handling the case where one subtree is `None` (height 0).  
- Using `or` instead of `and` when combining recursive balance checks.

**Key Insight – What “balanced” means**  
For every node, `|height(left) - height(right)| <= 1`.  
This is a global property: the root can be balanced but a deeper subtree might not.

**Memory Hook**  
> *“Balanced = height diff ≤ 1 at every node. Check root, then check left and right recursively.”*  
Or: *“Height helper plus recursive balance check.”*
