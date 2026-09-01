**Same Tree**

---

**Problem**  
Given two binary trees, determine if they are structurally identical and have the same node values.

**Core Technique**  
Recursive simultaneous traversal of both trees. Compare current nodes, then recurse on left and right.

**Algorithm Steps**  
1. **If both nodes are `None`** → return `True` (both empty positions are identical).  
2. **If exactly one node is `None`** (other is not) → return `False` (structure mismatch).  
3. **If `p.val != q.val`** → return `False` (value mismatch).  
4. **Recurse** on left and right subtrees:  
   `return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)`

**Python Code**  
```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

**Complexity**  
- **Time:** O(n) – worst case visits all nodes.  
- **Space:** O(h) – recursion stack, h = height of tree.

**Key Insight – How `True` is returned without an explicit `return True` after comparing values**  
- The only explicit `return True` is in the base case `p is None and q is None`.  
- For a tree with equal values, recursion reaches leaves where both left/right are `None`. Those calls return `True`.  
- The `and` operator combines these `True`s: `True and True = True`.  
- That `True` propagates upward as each level returns the result of `and` on its children.  
- Example: two single‑node trees with value 5:  
  - `left = True` (both None)  
  - `right = True` (both None)  
  - final `return True and True = True`

**Edge Cases**  
- Both empty → `True`.  
- One empty, one not → `False`.  
- Same values but different shapes → `False` because one subtree may be `None` while the other isn’t.  
- Deep identical trees → recursion depth h.

**Common Mistakes**  
- Missing the `p is None or q is None` base case → `AttributeError` when trying to access `.val` on `None`.  
- Using `or` instead of `and` in recursive return.  
- Forgetting that value equality alone doesn't return `True`; it only filters out mismatches. The `True` comes from the base case and `and` propagation.

**Memory Hook**  
> *"Both null? True. One null? False. Value mismatch? False. Otherwise: check left AND right; the ANDs make the final True."*

**Extra Clarification (if asked)**  
- The recursive function never explicitly returns `True` for a non‑empty node with equal values. It returns the logical AND of its children’s results. The base case `(None, None)` provides the `True` values that are combined up the tree. This is a clean example of recursive truth propagation.
