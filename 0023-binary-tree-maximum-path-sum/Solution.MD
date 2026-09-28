**Binary Tree Maximum Path Sum**

---

## Python Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        self.max_gain(root)
        return self.max_sum

    def max_gain(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        # Max gain from left and right subtrees (ignore negative gains)
        left_gain = max(self.max_gain(node.left), 0)
        right_gain = max(self.max_gain(node.right), 0)

        # Best path that goes through this node as the highest point
        price_new_path = node.val + left_gain + right_gain
        self.max_sum = max(self.max_sum, price_new_path)

        # Return the max gain if we continue upward through this node
        return node.val + max(left_gain, right_gain)
```

---

## Explanation

### Problem
Given a binary tree, find the maximum path sum. A path is any sequence of nodes from some starting node to any node in the tree along the parent‑child connections. The path must contain at least one node and does not need to go through the root.

### Intuition
For any node, the maximum path sum that **passes through that node** (using it as the highest point) is:

```
node.val + max(0, left_gain) + max(0, right_gain)
```

where `left_gain` and `right_gain` are the maximum sums we can get from the left and right subtrees **if we continue downward from this node**.  
We take `max(0, ...)` because we can choose not to include a subtree if its contribution is negative.

However, when we return the gain to the parent, we can only choose **one** side (the path can’t branch upward). So we return:

```
node.val + max(left_gain, right_gain)
```

We also keep a global `max_sum` updated with the best path sum seen at any node.

### Algorithm Steps
1. Initialize `self.max_sum = -inf`.
2. Define `max_gain(node)`:
   - If `node is None`: return `0`.
   - `left_gain = max(max_gain(node.left), 0)`
   - `right_gain = max(max_gain(node.right), 0)`
   - `price_new_path = node.val + left_gain + right_gain`
   - `self.max_sum = max(self.max_sum, price_new_path)`
   - Return `node.val + max(left_gain, right_gain)`
3. Call `max_gain(root)` and return `self.max_sum`.

### Leap of Faith (Recursion)
**Contract of `max_gain(node)`:**
> Return the maximum sum of a path that starts at `node` and goes downward to some leaf, choosing at most one child at each step. If all such paths have negative sum, return 0 (because we can choose to take no path from this node).

**Leap:** Assume the recursive calls on `node.left` and `node.right` correctly return the maximum downward gains from those subtrees.

**Combine:** At the current node, we compute:
- The best path **through** this node (as the highest point) = `node.val + left_gain + right_gain`. Update global max.
- The best downward gain to return to the parent = `node.val + max(left_gain, right_gain)`.

**Base case:** `None` returns 0 (no gain from an empty subtree).

By induction, the global `max_sum` will hold the maximum path sum over the entire tree.

### Complexity
- **Time:** O(n) – each node visited exactly once.
- **Space:** O(h) – recursion stack, where h is the tree height. Worst case O(n) for skewed tree, O(log n) for balanced.

---

## Quick Recall Notes

**Problem:** Find the maximum path sum in a binary tree. A path can start and end at any nodes, but must follow parent‑child connections.

**Core Technique:** Post‑order DFS that returns the maximum downward gain from each node, while updating a global maximum for paths that pass through the node as the highest point.

**Key Formulas:**
- Gain from a subtree: `max(0, max_gain(child))` – we ignore negative contributions.
- Best path through current node: `node.val + left_gain + right_gain`.
- Return to parent: `node.val + max(left_gain, right_gain)`.

**Leap of Faith:**
> *“Trust the children to return their best downward gains. At each node, compute the best path that uses this node as the peak, update the global max, and return the best single‑branch gain upward.”*

**Complexity:** O(n) time, O(h) space.

**Common Mistakes:**
- Forgetting to take `max(0, gain)` – negative subtrees should be excluded.
- Returning the sum of both children to the parent – the parent can only extend one branch.
- Not updating the global max inside the recursion (must update at every node).
- Using `Integer.MIN_VALUE` equivalent: in Python use `float('-inf')`.
- Forgetting that the path must contain at least one node – the initialization with `-inf` ensures a single node path is considered.

**Memory Hook:**
> *“Left gain, right gain, ignore negatives. Path through me = val + left + right. Return val + max(left, right). Global max tracks the best.”*

**One‑liner:**
> *“Post‑order DFS: best downward gain, best global path through node.”*
