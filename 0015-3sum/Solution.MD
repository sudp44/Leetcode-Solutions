**3Sum** (sorting + two‑pointer with duplicate skipping)

---

**Problem**  
Find all unique triplets in an integer array that sum to zero. No duplicate triplets allowed.

**Core Technique**  
**Sort + outer loop for first element + two‑pointer for the pair that sums to -first.**

**Algorithm Steps**  
1. `nums.sort()` → enables two‑pointer and duplicate handling.  
2. For each `i` from `0` to `n-1`:  
   - **Early break:** if `nums[i] > 0`, stop (can’t sum to zero).  
   - **Skip duplicate first elements:** if `i > 0` and `nums[i] == nums[i-1]`, continue.  
   - Call `twoSum(nums, i, result)` to find pairs in `[i+1, n-1]` that sum to `-nums[i]`.  
3. `twoSum` helper:  
   - `left = i+1`, `right = n-1`.  
   - While `left < right`:  
     - `total = nums[i] + nums[left] + nums[right]`  
     - If `total < 0` → `left += 1`.  
     - If `total > 0` → `right -= 1`.  
     - If `total == 0`:  
       - Add `[nums[i], nums[left], nums[right]]` to result.  
       - `left += 1`, `right -= 1` (move past the used values).  
       - **Skip duplicate left values:** while `left < right` and `nums[left] == nums[left-1]`, `left += 1`.  
       - (Optionally skip duplicate right values for efficiency.)  

**Why increment/decrement BEFORE skipping duplicates?**  
- We just recorded a triplet with the current `left` and `right` values.  
- First `left += 1` (and `right -= 1`) moves us off those exact indices.  
- Then the `while` loop checks whether the new value at `left` is still the same as the one we just used (`nums[left-1]`), and skips it.  
- If we skipped before moving, we’d compare with an unrelated earlier value.

**Complexity**  
- **Time:** O(n²) – outer loop n times, inner two‑pointer O(n) per iteration.  
- **Space:** O(1) (ignoring output); sorting may use O(log n) stack.

**Key Pitfalls**  
- Forgetting to skip duplicate first elements (`nums[i] == nums[i-1]`).  
- Skipping left duplicates without first incrementing `left` → logic error.  
- Not adding the early break when `nums[i] > 0`.  
- Returning duplicate triplets.

**Memory Hook**  
> *“Sort, fix one, two pointers for the rest. Move off the used spot, then skip its duplicates.”*
