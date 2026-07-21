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
