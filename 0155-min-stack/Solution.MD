## 1. Min Stack – Problem‑Specific Quick Recall Notes

**Problem**  
Design a stack that supports `push`, `pop`, `top`, and `getMin` — all in **O(1)** time.

**Core Idea**  
Implement the stack as a **singly linked list** where:
- `head` = top of the stack.
- Each **node** stores:
  - `val` – the element
  - `min` – the minimum value in the substack from this node downwards
  - `next` – pointer to the previous top (next element below)

**Why a linked list?**  
- Stack = LIFO. Inserting/removing at the head of a linked list is O(1).  
- No array resizing needed.

**How the list is created**  
- No separate `LinkedList` class.  
- `__init__` sets `self.head = None` (empty stack).  
- Each `push(value)` creates a `Node` and makes it the new head, linking it to the old head.  
- The chain of `Node` objects forms the list automatically.

**Operations (all O(1))**  
```python
def push(self, value):
    if not self.head:
        self.head = self.Node(value, value, None)   # self.Node because Node is inner class
    else:
        self.head = self.Node(value, min(value, self.head.min), self.head)

def pop(self):
    if self.head:
        self.head = self.head.next

def top(self):
    return self.head.val

def getMin(self):
    return self.head.min
```

**Why the `min` field works**  
- For a node, the minimum of its substack is: `min(my value, minimum of the rest)`.
- The rest’s minimum is exactly `old_head.min`.
- So `new_min = min(value, old_head.min)`.

**Complexity**  
- **Time:** O(1) for all operations.  
- **Space:** O(n) for n elements.

**Common Mistakes**  
- Parameter name mismatch: `push(self, value)` but using `val` in the body → `NameError`.
- Forgetting to check `if self.head` in `pop` (would crash on empty stack).
- Using `Node` instead of `self.Node` for the inner class (Python scoping rule).
- Trying to access `self.head.min` when the stack is empty (`self.head` is `None`).

**Memory Hook**  
> *“Stack = head of linked list. Each node: `(val, min_so_far, next)`. Push: new head = `Node(val, min(val, head.min), head)`. Min always at `head.min`.”*

---

## 2. Python OOP Concepts – Quick Recall Notes

### Instance Variables (`self.xyz`)
- **Instance variable** = a variable that belongs to a particular object (instance) of a class.  
- Created with `self.<name>` inside methods.  
- Each object has its own independent copy.  
- In `MinStack`, `self.head` is an instance variable: it stores the top node of that specific stack. Two stacks don’t share it.

### `self` Keyword
- `self` refers to the current instance.  
- When you call `s1.push(5)`, inside `push`, `self` is `s1`.  
- It lets methods access and modify the instance’s attributes (e.g., `self.head`).

### `__init__` vs. `Node.__init__`
- **`MinStack.__init__`** initialises the stack itself: sets `self.head = None`.  
- **`Node.__init__`** initialises a single node: sets `val`, `min`, `next`.  
- Both are separate constructors because there are two classes (`MinStack` and its inner class `Node`).

### Why `self.Node(...)` and not just `Node(...)`
- `Node` is an **inner class** (nested inside `MinStack`).  
- Inside methods of `MinStack`, `Node` is not automatically available as a local name.  
- You must access it via the instance or the class: `self.Node` or `MinStack.Node`.  
- Plain `Node` would raise `NameError` because Python doesn’t search enclosing class scopes for names.

### `Optional['MinStack.Node']` Type Hint
- `Optional[X]` means “either X or None”.  
- `'MinStack.Node'` is a **string forward reference** because the `Node` class isn’t fully defined when we’re inside its own `__init__`.  
- The quotes prevent a `NameError` at runtime; type checkers resolve it later.  
- `MinStack.Node` is the fully qualified path to the inner class.

### `self.head.min` How It Works
- `self.head` starts as `None`.  
- After pushing, `self.head` becomes a `Node` object.  
- `Node` objects have a `min` attribute (set in `Node.__init__`).  
- So `self.head.min` accesses the `min` attribute of the top node.  
- The `push` method only accesses `.min` when `head` is not `None`.

### Static Functionality in Python
- **Class variables** – defined inside the class but outside methods; shared by all instances.
- **`@staticmethod`** – method that doesn’t use `self` or `cls`.
- **`@classmethod`** – method that receives the class (`cls`) as first argument; can be alternative constructors.
- **Module‑level function** – plain function defined at the top level (not inside any class).  
- In `MinStack`, no static functionality was needed; but if you wanted a utility helper, you could place it as a static method or a module function.

### Instance Variable vs Class Variable
- **Instance variable**: unique per object. Created with `self.<name>`.
- **Class variable**: shared by all objects. Defined directly in class body.  
  Example:
  ```python
  class Dog:
      species = "Canis familiaris"  # class variable
      def __init__(self, name):
          self.name = name          # instance variable
  ```

### Notes on `pop`
- `pop` simply moves the head pointer: `self.head = self.head.next`.  
- No explicit deletion needed; Python’s garbage collector reclaims the old node.

---

**Memory Hook for OOP Concepts**  
> *“Instance variable = own copy per object, created with `self.`; `self` is the current object. Inner class? Use `self.Node` or `MinStack.Node`. `Optional['MinStack.Node']` uses string forward ref because the inner class isn’t ready yet. Static? Use `@staticmethod`, `@classmethod`, or class variables.”*
