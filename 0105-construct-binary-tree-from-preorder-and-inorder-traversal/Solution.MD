**Construct Binary Tree from Preorder and Inorder Traversal**

## Explanation

### Intuition
- **Preorder** visits nodes in the order: root → left → right. So the first element of `preorder` is always the root of the current subtree.
- **Inorder** visits nodes in the order: left → root → right. So the position of the root in `inorder` divides the array into the **left subtree** (everything to its left) and the **right subtree** (everything to its right).
- By combining these two properties, we can recursively build the tree:
  1. Take the next element from `preorder` as the root.
  2. Find its index in `inorder` (using a hash map for O(1) lookup).
  3. Recursively build the left subtree from `inorder[left … rootIndex-1]`.
  4. Recursively build the right subtree from `inorder[rootIndex+1 … right]`.

### Why the hash map?
Finding the root's index in `inorder` each time would be O(n) per node, leading to O(n²) total. Precomputing the value → index mapping makes each lookup O(1), so the whole construction is O(n).

### Leap of Faith (Recursion)
**Contract of `array_to_tree(preorder, left, right)`:**
> Build and return the root of the subtree whose in-order range is `inorder[left..right]`, using the next unused value from `preorder` as the root.

**Leap:** Assume the recursive calls on the left and right ranges correctly build and return their subtrees.

**Combine:**
- Pop the next value from `preorder` (advancing `preorder_index`) — this is the current root.
- Look up its position in `inorder` to determine the split.
- Recursively build left and right subtrees over the appropriate ranges.
- Attach them to the current root and return it.

**Base case:** `left > right` → empty range → return `None`.

By induction, the function builds the correct tree for any valid preorder/inorder pair.

## Complexity
- **Time:** O(n) — each node is created once, and the hash map lookup is O(1).
- **Space:** O(n) — for the hash map, plus O(h) recursion stack (worst case O(n)).

## Quick Recall Notes

**Problem:** Reconstruct a binary tree from its preorder and inorder traversals.

**Core Idea:**
- Preorder gives the root first.
- Inorder gives the split between left and right subtrees.

**Algorithm Steps:**
1. Build a hash map: `inorder value → index`.
2. Maintain a global `preorder_index` starting at 0.
3. Recursively:
   - If range invalid (`left > right`) → `None`.
   - Pick `root_value = preorder[preorder_index]`, increment index.
   - Find split point via hash map.
   - Recurse on left range and right range.
   - Return root.

**Leap of Faith:**
> *"Trust the recursive calls to build left and right subtrees. I just pick the root, find the split, and connect them."*

**Complexity:** O(n) time, O(n) space.

**Common Mistakes:**
- Forgetting to increment `preorder_index` — infinite loop or wrong root.
- Using `inorder.index(root_value)` instead of a hash map → O(n²).
- Mixing up the ranges for left/right recursion.
- Using `left < right` instead of `left > right` for the base case.

**Memory Hook:**
> *"Preorder picks root; inorder splits. Hash map for O(1) splits."*
