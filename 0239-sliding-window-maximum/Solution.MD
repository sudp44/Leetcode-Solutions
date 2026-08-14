**Sliding Window Maximum** (monotonic deque)

---

**Problem**  
Given an array `nums` and window size `k`, return the maximum for each sliding window of size `k`.

**Core Idea**  
Use a **deque of indices** that is always **monotonically decreasing** in value (`nums[deq[0]] ≥ nums[deq[1]] ≥ …`).  
The front of the deque is always the maximum of the current window.

**Why a deque (not a regular queue)?**  
- Need **O(1) removals from both ends**:  
  - Front: throw away indices that have left the window.  
  - Back: throw away indices that are smaller than the new element (they can never be max now).

**Why store indices (not values)?**  
- To know when an element falls out of the window (`deq[0] < i - k + 1`).  
- Values alone wouldn’t tell us when they expire.

**Algorithm Steps**  
1. Initialize an empty `deque` and `result` list.  
2. For each `i` from `0` to `n-1`:  
   - **Remove out‑of‑window** from front: while `deq[0] < i - k + 1`, `popleft()`.  
   - **Maintain decreasing order**: while `deq` not empty and `nums[deq[-1]] < nums[i]`, `pop()` from back.  
   - **Append current index** `i` to the deque.  
   - **If a full window has formed** (`i >= k-1`), record `nums[deq[0]]` as the max for this window.

**Why removing smaller ones from the back works**  
- Any older, smaller value can never become the maximum in any future window that includes the new, larger element.  
- So we discard them to keep the deque strictly decreasing.

The line:

```python
while queue and nums[queue[-1]] < nums[i]:
    queue.pop()
```

is how we maintain the deque as a **monotonically decreasing queue of indices**. Let’s build the intuition clearly.

---

### 1. What does this line actually do?

It removes **indices from the back of the deque** whose corresponding values are **strictly smaller** than the current element `nums[i]`.

Why from the back?  
Because we want the deque’s values (not the indices) to be arranged like:

```
front ──────> back
[large, large, smaller, smallest]
```

When a new element arrives, we compare it with the **back** (the smallest in the deque). If the new element is larger, the old back is useless, so we remove it. We repeat until the back is no longer smaller (or the deque is empty).

---

### 2. Why is an element “useless” if a new larger element arrives?

Because the new element is **to the right** in the array and **larger in value**. For any future window that contains the new element:

- The new element will stay in the window **at least as long** as the older element.
- Since it’s larger, the older element can **never** be the maximum again.

So the old smaller element can be safely thrown away.

**Imagine a row of candidates for “tallest person” contest.**  
When a new, taller person walks in, all the shorter people behind them can no longer win any contest from that point onward. We remove them.

---

### 3. What is the purpose of the while loop?

We keep popping until we hit something **larger than or equal to** `nums[i]`. That remaining element (if any) still has a chance to be a future maximum after `nums[i]` eventually leaves the window. But if all are smaller, we pop everything and `i` becomes the new sole candidate.

**Example:**

Array: `[5, 3, 4]`  
Deque (indices): initially `[0]` (value 5).

- `i = 1`, value `3`:  
  Back value is `5`, and `5 < 3`? No. So we just add index `1`.  
  Deque = `[0, 1]` → values `[5, 3]` (decreasing).

- `i = 2`, value `4`:  
  Back value is `3`, and `3 < 4`? Yes → pop index `1`.  
  Now back value is `5`, and `5 < 4`? No → stop.  
  Add index `2`.  
  Deque = `[0, 2]` → values `[5, 4]` (still decreasing).

Now for any window ending at `i=2` or later, index `1` (value 3) can never be the maximum because both `4` and `5` are larger and at least as far right. So it was safe to drop.

---

### 4. What stays in the deque?

After this cleanup, the deque always holds indices whose values are **non‑increasing**:

```
nums[deque[0]] ≥ nums[deque[1]] ≥ … ≥ nums[deque[-1]]
```

- `deque[0]` is always the **maximum of the current window**.
- The other elements are **potential future maxima** – they are in decreasing order and will become the front as their predecessors expire.

---

### 5. One‑line memory hook

> *“When a new larger value comes, all smaller previous candidates become irrelevant. Pop them from the back until a bigger or equal one remains.”*

So the line is simply enforcing the invariant that the deque is decreasing. That is the key to O(1) window maximums.

**Complexity**  
- **Time:** O(n) – each element pushed and popped at most once.  
- **Space:** O(k) – deque size bounded by window size.

**Key Invariant**  
The deque’s values are always **non‑increasing** (`≥`). Therefore the front is the largest.

**Common Mistakes**  
- Storing values instead of indices (can’t detect expiration).  
- Using a list with `pop(0)` → O(n²) (use `deque` for O(1) left pops).  
- Forgetting to check both ends (out of window AND smaller values).  
- Not handling `k=0` or empty array.

**Memory Hook**  
> “Deque of indices, keep it decreasing. Pop old from front, pop weak from back. Front is the window’s king.”
