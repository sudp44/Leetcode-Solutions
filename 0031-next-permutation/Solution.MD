**Next Permutation**

---

**Problem**  
Find the next lexicographically greater permutation of a list of integers in‑place. If no such permutation exists (the list is non‑increasing), rearrange to the smallest possible order (ascending).

**Core Technique**  
**Find pivot → swap → reverse suffix.** The suffix to the right of the pivot is always descending. After swapping, it stays descending, so reversing makes it ascending (minimum order).

**Algorithm Steps**  
1. **Find pivot `i`** – Scan from the right. Stop at the first index where `nums[i] < nums[i+1]`.  
   `while i >= 0 and nums[i+1] <= nums[i]: i -= 1`  
2. **If `i >= 0`** (pivot found):  
   - Find `j` from the right where `nums[j] > nums[i]` (the smallest larger element in the suffix).  
   - Swap `nums[i]` and `nums[j]`.  
3. **Reverse the suffix** (from `i+1` to end).  
   `nums[i+1:] = nums[i+1:][::-1]`  
   If `i == -1`, this reverses the entire array (produces the first permutation).

**Why the suffix stays descending after the swap**  
- Before the swap, the suffix `nums[i+1 … n-1]` is **descending**.  
- `j` is the rightmost index with `nums[j] > nums[i]`. Therefore, for all indices `k > j`, we have `nums[k] ≤ nums[i]`.  
- After swapping, the new element at index `j` is the original `nums[i]`, which is **≤** the original `nums[j]` (since `nums[i] < nums[j]`).  
  - **Right side:** For any `k > j`, we know `nums[k] ≤ old nums[i] = new nums[j]`. So the descending order holds between `j` and the elements to its right.  
  - **Left side (within the suffix):** For any `k < j` in the suffix, we had `old nums[k] ≥ old nums[j] > old nums[i]`. After swapping, `new nums[k] = old nums[k]` remains ≥ `old nums[j] = new nums[i]`, so the order is preserved.  
- **Therefore, the suffix remains descending** – it only got one of its larger elements replaced by a smaller one, but that smaller one is still ≥ everything to its right. Reversing then yields the minimal arrangement.

**Complexity**  
- **Time:** O(n) – scanning twice + reversal.  
- **Space:** The line `nums[i+1:][::-1]` creates a temporary list, making it O(n). For true O(1) space, use a two‑pointer in‑place reversal.

**Common Mistakes**  
- Using `while i >= 0:` for the swap step instead of `if i >= 0:` → leads to infinite loop / multiple swaps.  
- Forgetting to reverse the suffix (essential step).  
- Using `<=` vs `<` incorrectly: pivot condition is `nums[i+1] <= nums[i]` for the descending scan, and `nums[j] <= nums[i]` for finding the swap partner.  
- Not handling the case `i == -1` (no pivot) correctly—reversal still works.

**Memory Hook**  
> *"Pivot where `i < i+1`, swap with the smallest larger right, then reverse the descending tail. The swap never breaks the descending suffix because the new element at `j` is smaller than the old one but still ≥ everything to its right."*
