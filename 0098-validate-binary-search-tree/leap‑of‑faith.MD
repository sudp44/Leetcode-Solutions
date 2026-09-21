**leap‑of‑faith** explanation for **Validate Binary Search Tree** using in‑order traversal

---

## Step 1: Define the contract

Before writing any recursion, you must decide exactly what the function promises.

> **Contract of `inorder(node)`:**
> Given that `self.prev` holds the value of the last node visited in the in‑order traversal *so far* (or `None` if none visited yet), the function:
> 1. Returns `True` if the subtree rooted at `node` is a valid BST (respecting the BST property with everything before it in the in‑order sequence).
> 2. Updates `self.prev` to the value of the **last node** visited in the in‑order traversal of this subtree.

The function does **two jobs**: validate the subtree, and advance the in‑order “pointer” (`prev`).

---

## Step 2: Base case

```python
if node is None:
    return True
```

An empty subtree is trivially a valid BST.  
No nodes to visit, so `prev` is left unchanged.

---

## Step 3: The leap of faith

You **assume** that:

- `self.inorder(node.left)` will correctly validate the entire left subtree **and** leave `self.prev` pointing to the **largest** value in that left subtree (because in‑order visits the left subtree last node before the root — that’s the rightmost node of the left subtree).
- `self.inorder(node.right)` will correctly validate the entire right subtree **and** update `self.prev` to the last value visited there.

You **don’t trace** every recursive call. You just trust the contract.

---

## Step 4: What the current node does with the results

```python
# 1. Validate left subtree
if not self.inorder(node.left):
    return False

# 2. Check current node against prev
if self.prev is not None and node.val <= self.prev:
    return False

# 3. Update prev to current node's value
self.prev = node.val

# 4. Validate right subtree
return self.inorder(node.right)
```

Let’s interpret each step with the contract in mind:

- **After step 1:** By the leap of faith, `self.prev` is now the largest value in the left subtree. The left subtree is valid.
- **Step 2:** In a BST, the root must be **strictly greater** than every node in its left subtree. Since `prev` is the largest value in the left subtree, checking `node.val > prev` is sufficient to guarantee the root is larger than all left‑subtree nodes.
- **Step 3:** We update `prev` to the current node’s value because the current node is the next in the in‑order sequence.
- **Step 4:** We return the result of validating the right subtree. The right subtree’s validation will check that its nodes are all greater than `prev` (which is now the current node’s value) — exactly the BST property for the right side.

If step 4 returns `True`, the entire subtree rooted at `node` is a valid BST.  
If it returns `False`, something in the right subtree violated the BST property.

---

## Step 5: Why it works — induction

- **Base case:** `None` returns `True` (empty tree is valid).
- **Inductive step:** Assume `inorder` works correctly for all smaller subtrees.  
  For a tree of height `h`:
  - Left subtree height < h → by induction, it validates correctly and updates `prev` correctly.
  - The root check (`node.val > prev`) is correct because `prev` is the maximum of the left subtree.
  - Right subtree height < h → by induction, it validates correctly.
  - Therefore, the whole tree is validated correctly.

By induction, the function is correct for all trees.

---

## Why the two return styles?

- `if not self.inorder(node.left): return False` — early exit if the left subtree is invalid. We don’t need to check anything else.
- `return self.inorder(node.right)` — the right subtree is the **last** thing to check. Its result **is** the overall result for this subtree. No further work remains in this call.

If you forgot the `return` on the right subtree, the function would implicitly return `None` (falsy), causing valid BSTs to be rejected.

---

## Why `prev` is an instance variable

- `prev` must be **shared across all recursive calls** so that the in‑order sequence is maintained globally.
- If it were a local variable, each recursive call would have its own `prev`, and the comparison between the current node and the previous in‑order node would be lost.

---

## Visual trace (small example)

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

## Memory hook

> *“In‑order: left, me, right. `prev` remembers the last value. If I’m not greater than prev, it’s not a BST. Trust the children to do their part.”*

Or shorter:  
> *“Leap of faith: left subtree returns valid + updates prev. I check myself against prev. Then right subtree.”*
