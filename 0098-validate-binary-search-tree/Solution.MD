**Validate Binary Search Tree**

---

# Validate Binary Search Tree – Complete Notes

## Problem

Given the root of a binary tree, determine if it is a valid **Binary Search Tree (BST)**.

A valid BST satisfies:
- The left subtree of a node contains only nodes with values **strictly less** than the node's value.
- The right subtree of a node contains only nodes with values **strictly greater** than the node's value.
- Both left and right subtrees are themselves valid BSTs.

**Example (valid):**
```
    2
   / \
  1   3
```

**Example (invalid):**
```
    5
   / \
  1   4
     / \
    3   6
```
Node `3` is in the right subtree of `5` but `3 < 5` → invalid.

---

## Core Technique

**In‑order traversal (left → root → right)** using recursion, while maintaining a `prev` pointer that stores the value of the previously visited node.

**Key insight:** In a BST, an in‑order traversal yields values in **strictly increasing order**. So we just need to verify that each node's value is greater than the previous one.

---

## Algorithm Steps

1. Initialize `self.prev = None` (instance variable shared across recursive calls).
2. Define `inorder(node)`:
   - **Base case:** if `node is None` → return `True` (empty subtree is valid).
   - Recurse left: `if not self.inorder(node.left): return False`
   - Check current: `if self.prev is not None and node.val <= self.prev: return False`
   - Update `self.prev = node.val`
   - Return `self.inorder(node.right)`
3. Call `inorder(root)` and return its result.

---

## Python Code (canonical)

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        return self.inorder(root)

    def inorder(self, node: Optional[TreeNode]) -> bool:
        if node is None:
            return True

        if not self.inorder(node.left):
            return False

        if self.prev is not None and node.val <= self.prev:
            return False
        self.prev = node.val

        return self.inorder(node.right)
```

---

## Why `prev` is an instance variable

`prev` must be shared across **all recursive calls** so that the in‑order sequence is maintained globally.  
If it were a local variable, each recursive call would have its own `prev`, and the comparison between the current node and the previous in‑order node would be lost.

---

## Why `if node is None: return True`

An empty subtree is **trivially a valid BST** — there are no nodes, so there is nothing that can violate the BST property.  
Returning `True` acts as the neutral element for the recursive validation: it tells the parent "this side is fine, continue with your checks."

If we returned `False`, every leaf's empty children would be flagged invalid, incorrectly rejecting valid trees.

---

## Why `return self.inorder(node.right)`

The function follows **in‑order traversal**: left → root → right.

- Left subtree: validated first, and if invalid, we return `False` immediately.
- Current node: checked against `prev`. If invalid, return `False`.
- Right subtree: validated last. Its result **is** the overall result for this subtree, because there is nothing else to check.

If we wrote just `self.inorder(node.right)` without `return`, the function would fall off the end and implicitly return `None` (falsy), causing valid BSTs to be rejected.

---

## The Leap of Faith (Why recursion works here)

**Contract of `inorder(node)`:**
> Given that `self.prev` holds the value of the last node visited in the in‑order traversal so far (or `None` if none), the function:
> 1. Returns `True` if the subtree rooted at `node` is a valid BST.
> 2. Updates `self.prev` to the value of the last node visited in the in‑order traversal of this subtree.

**The leap:** You assume that `self.inorder(node.left)` correctly validates the left subtree and leaves `self.prev` pointing to the **largest** value in that left subtree (which is the last node visited in in‑order within that subtree). You don't trace every recursive call.

**Combining at the current node:**
- After the left call, `prev` = max value in the left subtree.
- The root must be strictly greater than that max: check `node.val > prev`.
- Update `prev` to `node.val`.
- The right subtree's validation will ensure its nodes are all greater than `node.val`.

**Induction proof:**
- **Base case:** `None` returns `True` (empty tree is valid).
- **Inductive step:** Assume the function works for all smaller subtrees. For a tree of height `h`:
  - Left subtree (height < h) validates correctly and updates `prev` correctly.
  - Root check is correct because `prev` is the max of the left subtree.
  - Right subtree (height < h) validates correctly.
  - Therefore, the whole tree is validated correctly.

By induction, the function is correct for all trees.

---

## Visual Trace (small example)

Tree:
```
    2
   / \
  1   3
```

| Call | Action | prev after | Return |
|------|--------|------------|--------|
| inorder(2) | → left inorder(1) | | |
| inorder(1) | → left None → True | None | |
| | check 1 > None → ok | 1 | |
| | → right None → True | 1 | **True** |
| back to 2 | left returned True | 1 | |
| | check 2 > 1 → ok | 2 | |
| | → right inorder(3) | | |
| inorder(3) | left None → True | 2 | |
| | check 3 > 2 → ok | 3 | |
| | right None → True | 3 | **True** |
| back to 2 | return True | 3 | **True** |

Result: `True`. ✅

---

## Complexity

- **Time:** O(n) – each node visited exactly once.
- **Space:** O(h) – recursion stack, where h is the tree height.  
  Worst case O(n) for skewed tree, O(log n) for balanced.

---

## Common Mistakes

- Using `prev` as a local variable instead of an instance variable → comparison lost between calls.
- Forgetting the base case `if node is None: return True` → `AttributeError`.
- Using `<=` vs `<` incorrectly. The check must be `node.val <= prev → return False` (strictly greater required).
- Forgetting the `return` on the right subtree call → function returns `None` (falsy) and rejects valid trees.
- Not checking left before updating `prev` – order matters in in‑order.
- Trying to validate using only local min/max at each node without global tracking (works but more complex).

---

## Alternative Approach (Min/Max bounds)

Instead of `prev`, you can pass down `low` and `high` bounds:

```python
def valid(node, low=float('-inf'), high=float('inf')):
    if not node:
        return True
    if not (low < node.val < high):
        return False
    return (valid(node.left, low, node.val) and
            valid(node.right, node.val, high))
```

Both are O(n). The in‑order approach is more elegant once you understand it.

---

## Memory Hook

> *“In‑order: left, me, right. `prev` remembers the last value. If I’m not greater than prev, it’s not a BST. Trust the children to do their part.”*

Or shorter:  
> *“Leap of faith: left subtree returns valid + updates prev. I check myself against prev. Then right subtree.”*

Or even shorter:  
> *“BST in‑order is sorted. Check each node is strictly greater than previous.”*
