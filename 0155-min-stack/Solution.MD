**Min Stack** (linked‑list with per‑node minimum)

---

**Problem**  
Design a stack that supports `push`, `pop`, `top`, and `getMin` — all in **O(1)** time.

**Core Idea**  
Implement the stack as a **singly linked list** where:
- `head` = top of the stack.
- Each **node** stores three things:
  - `val` – the element
  - `min` – the minimum value in the substack **from this node downwards**
  - `next` – pointer to the previous top (next element below)

**Why a linked list?**  
- A stack needs LIFO (last‑in‑first‑out).  
- Inserting/removing at the head of a linked list is O(1).  
- No array resizing needed.

**How the list is “created”**  
- No separate `LinkedList` class.  
- `__init__` sets `self.head = None` (empty stack).  
- Each `push(value)` creates one `Node` and makes it the new head, linking it to the old head.  
- The chain of `Node` objects forms the linked list automatically.

**Operations (all O(1))**  
```python
def push(self, value):
    if not self.head:
        self.head = Node(value, value, None)
    else:
        self.head = Node(value, min(value, self.head.min), self.head)

def pop(self):
    self.head = self.head.next          # discard top

def top(self):
    return self.head.val

def getMin(self):
    return self.head.min
```

**Why the `min` field works**  
- For a node, the minimum of the substack consisting of itself and everything below is:  
  `min( my value , minimum of the rest )`.
- The rest’s minimum is exactly `self.head.min` of the old head.
- So `new_min = min(value, old_head.min)`.

**Complexity**  
- **Time:** O(1) for all operations.  
- **Space:** O(n) for n elements (one node per element).

**Common Mistake**  
- Parameter name mismatch: `push(self, value)` but using `val` in the body → `NameError`.

**Memory Hook**  
> *“Stack = head of linked list. Each node: `(val, min_so_far, next)`. Push: new head = `Node(val, min(val, head.min), head)`. Min always at `head.min`.”*
