**Binary Search** (exact value search)

---

**Problem**  
Given a sorted array and a target, return its index. If not found, return `-1`.

**Core Technique**  
**Binary Search** – repeatedly divide the search interval in half.

**Algorithm Steps**  
1. `left = 0`, `right = len(nums) - 1`.  
2. `while left <= right:`  
   - `mid = (left + right) // 2`  
   - If `nums[mid] == target` → return `mid`.  
   - If `nums[mid] > target` → `right = mid - 1` (target must be in left half).  
   - If `nums[mid] < target` → `left = mid + 1` (target must be in right half).  
3. Return `-1` (target not found).

**Why `while left <= right`?**  
- The search space is inclusive: `[left, right]`.  
- When `left == right`, there is exactly one element remaining that still needs to be checked.  
- Using `while left < right` would stop before checking that last element, requiring an extra check outside the loop.  
- We use `mid ± 1` because `mid` itself has already been compared and is excluded.

**Complexity**  
- **Time:** O(log n) – search space halved each iteration.  
- **Space:** O(1) – only a few integer variables.

**Common Mistakes**  
- Using `<` instead of `<=` → missing the final single element.  
- Incorrect update: `right = mid` or `left = mid` without `±1` → can cause infinite loops.  
- Forgetting that `mid` is already checked → leads to unnecessary comparisons or infinite loops.  
- Not handling empty input (the loop condition handles it naturally, but always good to consider).

**Key Invariant**  
If the target exists, it is always in the inclusive range `[left, right]`.

**Memory Hook**  
> *“`while left <= right` with `mid ± 1` – because every element, including the last one, must be checked.”*
