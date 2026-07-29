**Find First and Last Position of Element in Sorted Array** (binary search for boundaries)

---

**Problem**  
Given a sorted array and a target, return the starting and ending index of the target. If not found, return `[-1, -1]`.

**Core Technique**  
Two **modified binary searches** (or one helper with a flag) to find the leftmost and rightmost occurrence. When `nums[mid] == target`, we **do not stop** – we check neighbours to decide if we are at the boundary, otherwise we continue searching.

---

**Algorithm Steps**  
1. `first = findBound(nums, target, True)`  
   - If `first == -1` → return `[-1, -1]`.  
2. `last = findBound(nums, target, False)`.  
3. Return `[first, last]`.

**Helper `findBound(nums, target, isFirst)`**  
1. `start = 0`, `end = len(nums) - 1`.  
2. `while start <= end`:  
   - `mid = (start + end) // 2`.  
   - If `nums[mid] < target` → `start = mid + 1`.  
   - If `nums[mid] > target` → `end = mid - 1`.  
   - **If `nums[mid] == target`:**  
     - **For first occurrence (`isFirst=True`):**  
       - If `mid == 0` **or** `nums[mid] != nums[mid-1]` → this is the first → return `mid`.  
       - Else (left neighbour also `target`) → go left: `end = mid - 1`.  
     - **For last occurrence (`isFirst=False`):**  
       - If `mid == len(nums)-1` **or** `nums[mid] != nums[mid+1]` → this is the last → return `mid`.  
       - Else (right neighbour also `target`) → go right: `start = mid + 1`.  
3. Return `-1` (target not found).

---

**Why this works**  
- The array is sorted, so identical values are contiguous.  
- When we land on a `target`, we check if the immediate neighbour is different. If it is, we are at the edge of the block.  
- If not, the block extends further, so we move the search to the left (for first) or right (for last) half, exactly like a normal binary search but only when the neighbour is also target.

---

**Complexity**  
- **Time:** O(log n) – two binary searches, each halving the search space.  
- **Space:** O(1) – only a few variables.

---

**Common Mistakes**  
- Returning `mid` immediately upon finding `target` without checking neighbours (returns a middle occurrence, not the boundary).  
- Forgetting that the array might be empty or the target not present – handle via `first == -1`.  
- Using `start <= end` with `mid ± 1` updates – this is correct because we discard `mid` only when we are **certain** it’s not the boundary.  
- Confusing the neighbour condition: for first, check **left** (`mid-1`); for last, check **right** (`mid+1`).

---

**Memory Hooks**  
> *“When target found, don't stop – check the neighbour. If neighbour different → boundary found. Else keep going towards the edge.”*  
> *“First? Look left. Last? Look right.”*  
> *“`mid == 0 or nums[mid] != nums[mid-1]` → first. `mid == n-1 or nums[mid] != nums[mid+1]` → last.”*
