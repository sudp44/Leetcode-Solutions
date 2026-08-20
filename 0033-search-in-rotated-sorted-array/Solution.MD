**Search in Rotated Sorted Array**

---

**Problem**  
Search for a target in a rotated sorted array with distinct values. Return its index, or `-1` if not found. Must run in O(log n).

**Core Technique**  
Binary search with an extra step: determine **which half is sorted**, then decide whether the target lies in that sorted half or the other.

**Algorithm Steps**  
1. `left = 0`, `right = len(nums) - 1`.  
2. **While** `left <= right`:  
   - `mid = (left + right) // 2`.  
   - If `nums[mid] == target` → return `mid`.  
   - **If left half is sorted** (`nums[left] <= nums[mid]`):  
     - If `target < nums[left]` OR `target > nums[mid]` → target is not in the sorted left half → `left = mid + 1`.  
     - Else → target is in the left half → `right = mid - 1`.  
   - **Else (right half is sorted)**:  
     - If `target > nums[right]` OR `target < nums[mid]` → target is not in the sorted right half → `right = mid - 1`.  
     - Else → target is in the right half → `left = mid + 1`.  
3. Return `-1`.

**Why it works**  
- A rotated sorted array has at least one sorted half at any step.  
- We first check if `target` equals `mid` (handles equality).  
- Then we use the sorted half’s range to eliminate half of the search space:  
  - If target is outside the sorted half’s range, it must be in the other half.  
  - If it’s inside, we search the sorted half.  
- This reduces the search space by half each iteration → O(log n).

**Complexity**  
- **Time:** O(log n)  
- **Space:** O(1) – only a few integer variables.

**Key Insights**  
- The condition `nums[left] <= nums[mid]` tells us the left half is sorted. Otherwise, the right half must be sorted.  
- To decide where to search, we check whether the target lies **within** the sorted half’s boundaries (`nums[left]` to `nums[mid]` for left, `nums[mid]` to `nums[right]` for right).  
- We use strict inequalities (`<`, `>`) because equality with `mid` is already handled earlier.

**Common Mistakes**  
- Forgetting to check `nums[mid] == target` first.  
- Using the wrong sorted half detection condition (`<` instead of `<=`).  
- Misplacing the range checks: e.g., for left sorted half, target must be `>= nums[left]` and `<= nums[mid]`; if it’s outside, search right.  
- Returning `nums[mid]` instead of `mid`.  
- Not handling the case where the array is not rotated (the left half will always be sorted and the logic still works).

**Memory Hook**  
> *“Find mid, check target. One half is sorted. If target inside sorted half → search there; else → search the other half.”*  
> More concise: **“Sorted half? Is target in its range? Yes → go there, No → go elsewhere.”**

**Code snapshot**  
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
```

This code is correct for distinct values. If the array may contain duplicates (LeetCode 81), this logic does not work in all cases.
