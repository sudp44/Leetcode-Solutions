**Find Leaves of Binary Tree** (LeetCode 366 – Premium)

---

## Problem Description

```
366. Find Leaves of Binary Tree
Level
Medium

Description
Given the root of a binary tree, collect a tree's nodes as if you were doing this:
- Collect all the leaf nodes.
- Remove all the leaf nodes.
- Repeat until the tree is empty.

Return a list of lists, where each inner list contains the leaf nodes collected at each step.

Example 1:
Input: root = [1,2,3,4,5]
        1
       / \
      2   3
     / \
    4   5
Output: [[4,5,3],[2],[1]]

Example 2:
Input: root = [1]
Output: [[1]]

Constraints:
- The number of nodes in the tree is in the range [1, 100].
- -100 <= Node.val <= 100
```

---

## Complete Runnable Python Code

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def collectLeaves(self, root):
        result = []
        while root is not None:
            leaves = []
            root = self.removeLeaves(root, leaves)
            result.append(leaves)
        return result

    def removeLeaves(self, node, leaves):
        if node is None:
            return None
        # If it's a leaf, add to leaves and remove it (return None)
        if node.left is None and node.right is None:
            leaves.append(node.val)
            return None
        # Otherwise, recursively remove leaves from children
        node.left = self.removeLeaves(node.left, leaves)
        node.right = self.removeLeaves(node.right, leaves)
        return node


# ------------------ Test ------------------
if __name__ == "__main__":
    # Build tree: [1,2,3,4,5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    sol = Solution()
    print(sol.collectLeaves(root))   # Expected: [[4, 5, 3], [2], [1]]

    # Single node test
    root2 = TreeNode(1)
    print(sol.collectLeaves(root2))  # Expected: [[1]]
```

**How to run**: Copy the entire block into any Python 3 online compiler (Replit, Programiz, etc.) and click Run.

---

## Explanation

### Intuition
At each round:
1. Traverse the whole tree and find every leaf (node with no children).
2. Record the leaf values in the current round's list.
3. Remove those leaves from the tree.
4. Repeat until the tree is completely gone.

This naturally produces leaves in increasing order of "height from the bottom": nodes removed first are those deepest from the root.

### `removeLeaves(node, leaves)` — the helper
- **Base case:** `node is None` → return `None` (nothing to remove).
- **Leaf case:** If `node.left` and `node.right` are both `None`, it's a leaf. Append its value to `leaves` and return `None` (removes it from the tree by returning `None` to its parent).
- **Recursive case:** Recurse on left and right children, then assign the results back:
  ```python
  node.left = self.removeLeaves(node.left, leaves)
  node.right = self.removeLeaves(node.right, leaves)
  return node
  ```
  Assigning the results back effectively **detaches** any children that were leaves.

### `collectLeaves(root)` — the main loop
- While `root` is not `None`:
  - Create a new list `leaves`.
  - Call `removeLeaves(root, leaves)` to remove all leaves of the current tree and collect them.
  - The returned value is the new root (after removing leaves). It may be `None` if the tree became empty.
  - Append `leaves` to `result`.

### Walkthrough (Example 1)

```
Initial tree:
        1
       / \
      2   3
     / \
    4   5

Round 1: Leaves = [4, 5, 3]
        1
       /
      2

Round 2: Leaves = [2]
        1

Round 3: Leaves = [1]
        (empty)

Result: [[4,5,3],[2],[1]]
```

---

## Leap of Faith (Recursion)

**Contract of `removeLeaves(node, leaves)`:**  
> Remove all leaves in the subtree rooted at `node`, append their values to `leaves`, and return the root of the modified subtree (which may be `None` if `node` itself was a leaf).

**Leap:** Assume the recursive calls on `node.left` and `node.right` correctly remove all leaves in their subtrees and return the pruned subtrees.

**Combine:** At the current node:
- If `node` is itself a leaf, we handle it directly (append, return `None`).
- Otherwise, we reassign `node.left` and `node.right` to the pruned subtrees returned by the recursive calls. This **detaches** any children that became `None` (i.e., were leaves).
- Return `node` — the pruned subtree's root.

**Base case:** `None` → return `None` (empty tree, no leaves).

By induction, `removeLeaves` correctly removes all current leaves and prunes the tree.

---

## Complexity

Let `n` = total number of nodes, `h` = height of tree.

- **Time:** O(n²) in the worst case.  
  Each round, `removeLeaves` traverses the entire remaining tree (up to O(n) work). The number of rounds equals the height `h`. In a skewed tree, `h = n`, giving O(n²). In a balanced tree, `h = log n`, giving O(n log n).
- **Space:** O(n) for the result + O(h) recursion stack.

A more efficient O(n) approach assigns each node a "height" (distance to nearest leaf) and groups by height, but the iterative removal approach is the intuitive one shown here.

---

## Quick Recall Notes

**Problem**  
Repeatedly remove all leaves and record them in rounds until the tree is empty.

**Core Technique**  
Iterative removal + recursive leaf pruning. Each round = one full DFS that removes all current leaves.

**Key Steps**
1. `while root:` loop.
2. For each round: `leaves = []`, `root = removeLeaves(root, leaves)`.
3. `removeLeaves`: if leaf → append to `leaves`, return `None`. Else → recurse left and right, reassign children, return node.
4. Append `leaves` to result.

**Leap of Faith**  
Contract: `removeLeaves(node, leaves)` removes all leaves in the subtree, appends their values to `leaves`, and returns the pruned root.  
Leap: trust the recursive calls to handle their subtrees. Combine by reassigning `node.left` and `node.right` to the returned pruned subtrees.

**Complexity**  
- Time: O(n²) worst case (skewed), O(n log n) balanced.  
- Space: O(n) for output + O(h) recursion.

**Common Mistakes**  
- Forgetting to assign the result of the recursive call back (`node.left = removeLeaves(...)`) — leaves won't actually be removed.  
- Confusing "remove leaves" with "traverse leaves" — we must actually detach them by returning `None`.  
- Forgetting to append the leaf value before returning `None`.

**Memory Hook**  
> *"Loop until tree is gone. Each round: DFS, collect leaves, detach them. Repeat."*  
> Or: *"Peel the tree like an onion, one leaf layer at a time."*

**Leap of Faith one‑liner:**  
> *"Trust the children to prune their subtrees; I just handle myself and reconnect."*