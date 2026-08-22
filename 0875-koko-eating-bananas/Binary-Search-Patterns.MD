**Binary Search Patterns**

1. **Exact Search (Standard Binary Search)**
   - Use when searching for a specific target value.
   - Condition: `while left <= right`
   - `mid = (left + right) // 2`
   - If `nums[mid] == target`: return `mid`
   - If `target > nums[mid]`: `left = mid + 1`
   - If `target < nums[mid]`: `right = mid - 1`
   - Return `-1` after loop.
   - **Why `<=`?** The interval is inclusive, and we must check the last remaining element.

2. **Boundary Search (Monotonic Condition, e.g., minimum feasible)**
   - Use when finding the first index where a condition becomes true (e.g., `canEat(speed)` returns true for all speeds ≥ answer).
   - Condition: `while left < right`
   - `mid = (left + right) // 2`
   - If `condition(mid)` is **true** (feasible): `right = mid`  ← keep `mid` as a candidate
   - Else (not feasible): `left = mid + 1`  ← discard `mid` and all smaller
   - After loop, `left == right` is the answer; return `left`.
   - No separate `ans` variable needed because the answer always remains inside `[left, right]`.

**When to Use Which**
- **Exact search**: known target, just find its index.
- **Boundary search**: want the first/smallest (or last/largest) index where a predicate holds (e.g., minimum eating speed, first bad version). The condition is monotonic: once true, it stays true.

**Why `left < right` works without storing `ans`**
- We never eliminate a feasible candidate: `right = mid` preserves `mid` in the interval.
- Only non‑feasible values are discarded with `left = mid + 1`.
- The interval shrinks until only one index remains—that index is guaranteed to be the answer.

**Memory Hook**
> *"Exact? `<=` and `mid±1`. Boundary? `<` and `right=mid` when true, `left=mid+1` when false."*

---

**Example (Koko Eating Bananas)**
```python
while left < right:
    mid = (left + right) // 2
    if canEat(piles, mid, h):
        right = mid        # feasible, try smaller
    else:
        left = mid + 1    # not feasible, need larger
return left
```

This is the boundary‑search pattern for the minimum feasible speed.

---

## 1. What is a “boundary” in boundary search?

A **boundary** is the **transition point** in a sequence where a condition changes from **false to true** (or true to false). The goal of a boundary search is to find that exact point.

Imagine you have a sorted list of possible answers (e.g., speeds, versions, positions). For each candidate, you can test a condition (e.g., “can finish in time”, “is a bad version”). The condition is **false for all candidates before the boundary**, and **true for all candidates after it**.

**Example (Koko Eating Bananas):**
- Speeds from 1 to max(piles).
- Condition: “Can Koko eat all bananas within h hours?”
- There is some minimum speed `K` where this becomes true.
- For speeds < `K`, condition is false.
- For speeds ≥ `K`, condition is true.
- The **boundary** is exactly `K` – the smallest speed where the condition flips from false to true.

So the boundary search finds that flip point. In the binary search, we maintain an interval `[left, right]` that contains this boundary. When we test `mid`, if condition is true, the boundary must be ≤ `mid`, so we set `right = mid`. If condition is false, the boundary must be > `mid`, so we set `left = mid + 1`. Eventually, `left == right` and that index is the boundary (the answer).

Other examples:
- **First Bad Version:** Versions from 1 to n. Condition: “is bad version”. The boundary is the first bad version.
- **Search Insert Position:** Array sorted, condition: “nums[i] >= target”. The boundary is the first index with value ≥ target.

---

## 2. What does “The condition is monotonic: once true, it stays true” mean?

**Monotonic** means the condition behaves in a predictable, one‑way direction as the input parameter increases. It never flips back and forth.

For a boundary search, we require the condition to be **monotonic** in this sense:

- As you increase the search parameter (e.g., speed, version number, index), the condition goes from **false** to **true**, and once it becomes true, it remains true for all larger parameters.

In other words, there is a single transition point. There is no scenario where the condition is true, then false, then true again.

**Why is monotonicity important for binary search?**
- Binary search relies on the ability to discard half of the search space after testing one candidate.
- If the condition is monotonic, then:
  - If `mid` is true, all values ≥ `mid` are also true. The boundary must be ≤ `mid`, so we can discard the right half and search left (set `right = mid`).
  - If `mid` is false, all values ≤ `mid` are also false. The boundary must be > `mid`, so we can discard the left half and search right (set `left = mid + 1`).
- Without monotonicity, you could not safely discard half the space because the condition might flip back.

**Example (monotonic):** Koko can finish within h hours at speed 5? Yes. Then at speed 6, 7, … she can also finish (faster speed never hurts). The condition “can finish” is monotonic with respect to speed: once true, it stays true.

**Counterexample (non-monotonic):** Suppose condition is “number is prime”. As number increases, prime status flips randomly. You cannot binary search for the first prime because there’s no consistent boundary; you can’t discard halves safely.

**In summary:**
- **Boundary** = the single point where the condition flips.
- **Monotonic condition** = the condition only flips once, allowing binary search to work by testing the middle and discarding a half.

This property is what lets the `while left < right` pattern converge to the answer without needing to store a separate `ans`. The answer (boundary) is always preserved in `[left, right]`.
