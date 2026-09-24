**Serialize and Deserialize Binary Tree**

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        def rec_serialize(node, string):
            if node is None:
                string += "null,"
            else:
                string += str(node.val) + ","
                string = rec_serialize(node.left, string)
                string = rec_serialize(node.right, string)
            return string

        return rec_serialize(root, "")

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        def rec_deserialize(nodes):
            if nodes[0] == "null":
                nodes.pop(0)
                return None
            root = TreeNode(int(nodes[0]))
            nodes.pop(0)
            root.left = rec_deserialize(nodes)
            root.right = rec_deserialize(nodes)
            return root

        node_list = data.split(",")
        # Remove the trailing empty string caused by the final comma
        if node_list and node_list[-1] == "":
            node_list.pop()
        return rec_deserialize(node_list)
```

**Note:** The above uses `list.pop(0)` which is O(n). For better performance, you can use an iterator or an index pointer. Below is an optimized version using an index:

```python
class Codec:
    def serialize(self, root: TreeNode) -> str:
        def rec_serialize(node):
            if node is None:
                return "null,"
            return str(node.val) + "," + rec_serialize(node.left) + rec_serialize(node.right)
        return rec_serialize(root)

    def deserialize(self, data: str) -> TreeNode:
        nodes = data.split(",")
        self.index = 0
        def rec_deserialize():
            if nodes[self.index] == "null":
                self.index += 1
                return None
            root = TreeNode(int(nodes[self.index]))
            self.index += 1
            root.left = rec_deserialize()
            root.right = rec_deserialize()
            return root
        return rec_deserialize()
```

Both work; the second is more efficient.

---

## Explanation

### Serialization (Preorder)
- Traverse the tree in **preorder** (root → left → right).
- For each node, append its value followed by a comma.
- For `None`, append `"null,"`.
- This produces a string like `"1,2,null,null,3,4,null,null,5,null,null,"`.

### Deserialization
- Split the string by commas into a list.
- Use a pointer (or pop from front) to process nodes recursively.
- If the current token is `"null"`, return `None`.
- Otherwise, create a node with the integer value, then recursively build its left and right subtrees.
- The preorder sequence ensures the root is always the first token, then left subtree, then right subtree.

### Leap of Faith (Recursion)
**Contract of `rec_deserialize`:**
> Consume the next token from the list, build the subtree rooted at that token (or `None` if null), and return its root.

**Leap:** Assume the recursive calls for left and right correctly build and return their subtrees.

**Combine:** Create the root from the current token, then assign `root.left` and `root.right` to the results of the recursive calls. Return the root.

**Base case:** If token is `"null"`, return `None`.

By induction, the whole tree is reconstructed.

### Complexity
- **Time:** O(n) — each node visited once in both serialize and deserialize.
- **Space:** O(n) — for the string and the recursion stack (O(h)).

---

## Quick Recall Notes

**Problem:** Design an algorithm to serialize and deserialize a binary tree.

**Core Technique:** Preorder traversal with `"null"` markers.

**Serialize:**
- Recursive preorder: root, left, right.
- For null, append `"null,"`; otherwise append `val + ","`.

**Deserialize:**
- Split by `","` into a list.
- Use a pointer (or pop from front) to process tokens.
- Recursively: if token is `"null"` → `None`; else create node, set left and right recursively.

**Leap of Faith:**
> *"Trust the recursive calls to build left and right subtrees. I just create the root from the next token and connect them."*

**Complexity:** O(n) time, O(n) space.

**Common Mistakes:**
- Forgetting the trailing comma handling (empty string after split).
- Using `pop(0)` repeatedly (O(n²)) — prefer index pointer.
- Not handling empty tree (`root = None`).
- Mixing up preorder with inorder/postorder.

**Memory Hook:**
> *"Preorder + null markers. Split, recurse, connect."*

**Optimized Code Snippet (index pointer):**
```python
def deserialize(self, data: str) -> TreeNode:
    nodes = data.split(",")
    self.index = 0
    def rec():
        if nodes[self.index] == "null":
            self.index += 1
            return None
        root = TreeNode(int(nodes[self.index]))
        self.index += 1
        root.left = rec()
        root.right = rec()
        return root
    return rec()
```
