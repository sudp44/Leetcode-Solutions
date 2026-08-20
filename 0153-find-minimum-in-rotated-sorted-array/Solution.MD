**Find Minimum in Rotated Sorted Array** (distinct values).

---

**Problem**  
Given a sorted array that has been rotated between 1 and n times, find the minimum element in O(log n) time.

**Core Technique**  
Binary search with `nums[left] < nums[right]` to detect a fully sorted subarray. Maintain the smallest value seen so far (`ans`).

**Algorithm Steps**  
1. `left = 0`, `right = n - 1`, `ans = nums[0]`.  
2. **While** `left <= right`:  
   - **If `nums[left] < nums[right]`** → the current segment is sorted.  
     Update `ans = min(ans, nums[left])` and `break` (no need to continue).  
   - Compute `mid = (left + right) // 2`.  
     Update `ans = min(ans, nums[mid])`.  
   - **If `nums[left] <= nums[mid]`**:  
     The left half `[left, mid]` is sorted, so the rotation/pivot is in the right half → `left = mid + 1`.  
   - **Else**:  
     The pivot is in the left half (or `mid` is the pivot) → `right = mid - 1`.  
3. Return `ans`.

**Why it works**  
- In a rotated sorted array, at most one side of the mid can be sorted.  
- If `nums[left] < nums[right]`, the whole segment is sorted → its leftmost element is the minimum.  
- Otherwise, the pivot (where a large element is followed by a small one) must lie in one of the halves.  
- We always move toward the pivot and update the minimum with every visited value, so we never lose the true minimum.

**Complexity**  
- **Time:** O(log n) – search space halves each iteration.  
- **Space:** O(1) – only a few variables.

**Common Mistakes**  
- Using `nums[left] < nums[mid]` instead of `nums[left] <= nums[mid]`.  
  For two elements like `[2, 1]`, `<` fails when `left` and `mid` are the same index, causing wrong answer.  
- Overwriting `ans` with `nums[left]` without `min()` – you may lose a smaller value found earlier.  
- Forgetting the early break when the segment is already sorted (inefficient, but not wrong).  
- For duplicates, this algorithm doesn't handle `nums[left] == nums[mid] == nums[right]`; that requires a different version.

**Memory Hook**  
> *"Sorted segment? Check `left < right`, then `left <= mid` tells you which side has the pivot. Always `ans = min(ans, nums[mid])` and never overwrite without `min`."*
