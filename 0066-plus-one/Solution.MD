**Plus One**

---

## Problem
Given a non‑empty array of digits representing a non‑negative integer (most significant digit first), increment the integer by one and return the resulting array.

**Example:**
- `[1,2,3]` → `[1,2,4]`
- `[9,9,9]` → `[1,0,0,0]`

## Core Technique
Iterate from **right to left**, simulating elementary addition with carry.

## Algorithm Steps
1. Loop `i` from `len(digits) - 1` down to `0`:
   - If `digits[i] < 9`:
     - `digits[i] += 1`
     - **return** `digits` (no carry needed)
   - Else (`digits[i] == 9`):
     - `digits[i] = 0` (carry over)
2. If loop finishes, all digits were `9`.  
   Return `[1] + digits` (prepend a new leading `1`).

## Python Code
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
```

## Complexity
- **Time:** O(n) – one pass at most.
- **Space:** O(1) extra for in‑place modification; O(n) for the new array only in the all‑9s case (unavoidable since length increases).

## Common Mistakes
- Forgetting the all‑9s case → returns `[0,0,0]` instead of `[1,0,0,0]`.
- Modifying the array and then trying to return a new one incorrectly.
- Using extra space for a copy when not needed (except all‑9s).
- Looping from left to right (wrong direction for carry).

## Memory Hook
> *“From right: if <9, add 1 and done. If 9, set 0 and carry. All 9s? Prepend 1.”*

Or even shorter:
> *“Right to left, carry the 1.”*

## Why It Works
This mimics how you add 1 on paper. The first digit from the right that is not 9 simply increments, and everything to its right becomes 0 (already done). If every digit is 9, they all become 0 and a new leading 1 is added.
