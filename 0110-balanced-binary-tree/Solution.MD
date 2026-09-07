**Balanced Binary Tree (LeetCode 110)**, including both the simple top‑down and the optimal bottom‑up approaches.

---

**Problem**  
Given a binary tree, determine if it is height‑balanced: for every node, the height difference between its left and right subtrees is at most 1.

**Approach 1: Top‑Down (Simple but O(n²) time)**  
- Compute height of left and right subtrees at each node, check difference, then recursively check left and right children.  
- Recomputes heights many times.

**Approach 2: Bottom‑Up (Optimal, O(n) time)**  
- Use a post‑order DFS that returns the height of the subtree if balanced, or `-1` if unbalanced.  
- Avoids recomputation by propagating height and balance status in a single pass.

---

### Python Code (Optimal Bottom‑Up)

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.check(root) != -1

    def check(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left = self.check(node.left)
        if left == -1:
            return -1

        right = self.check(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return max(left, right) + 1
```

---

### Complexity

| Approach | Time   | Space |
|----------|--------|-------|
| Top‑Down | O(n²) | O(h)  |
| Bottom‑Up| O(n)   | O(h)  |

`h` = height of tree (worst case O(n) for skewed, O(log n) for balanced).

---

### Key Intuition

- A tree is balanced if **every** node's subtrees differ in height by ≤ 1.
- In the bottom‑up method, a sentinel `-1` indicates "unbalanced".  
- If any child returns `-1`, the current node immediately returns `-1` without further checks.
- Height of a node = `1 + max(left_height, right_height)`.

---

### Common Mistakes

- Forgetting to check both subtrees recursively in the top‑down approach.
- Returning `0` for empty node and then adding 1 inconsistently.
- In bottom‑up, forgetting to propagate `-1` early (leads to wrong result or extra work).
- Using `or` instead of `and` in top‑down recursive calls.
- Not handling the case where a subtree is empty (height 0).

---

### Memory Hooks

- **Top‑Down:** *"Check root, then left and right. Height helper repeated."*
- **Bottom‑Up:** *"Return -1 for unbalanced, height otherwise. Check left, check right, compare heights."*
- **One‑liner:** *"Balanced = height diff ≤ 1 everywhere. Optimal = single pass from bottom."*
