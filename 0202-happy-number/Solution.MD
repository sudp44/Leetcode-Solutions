**Happy Number**

---

## Problem
A happy number is defined by the process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (happy) or it loops endlessly in a cycle (not happy).

Return `True` if `n` is a happy number, else `False`.

**Example:**
- `19` → `1²+9²=82` → `68` → `100` → `1` → **Happy**
- `2` → `4` → `16` → `37` → `58` → `89` → `145` → `42` → `20` → `4` … cycle → **Not Happy**

## Core Technique
**Cycle detection** using a hash set (`seen`). If we encounter a number we’ve already seen, we’re in a cycle → not happy.

## Algorithm Steps
1. Initialize an empty set `seen`.
2. While `n != 1` and `n not in seen`:
   - Add `n` to `seen`.
   - Compute the sum of the squares of the digits of `n` and assign back to `n`.
3. Return `n == 1` (if we exit because `n == 1`, it's happy; otherwise we hit a cycle, so not happy).

## Helper: Sum of Squares of Digits
```python
def get_sum_of_squares(n: int) -> int:
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10
    return total
```

## Python Code (canonical)
```python
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.get_sum_of_squares(n)
        return n == 1

    def get_sum_of_squares(self, n: int) -> int:
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total
```

## Complexity
- **Time:** O(log n) per transformation; total iterations are bounded (numbers either reach 1 or enter a small cycle). In practice, O(log n) or O(1) amortized.
- **Space:** O(k) where k is the number of distinct values before a cycle or reaching 1 (typically small, ≤ 1000).

## Common Mistakes
- Forgetting to use a set → infinite loop.
- Incorrect sum of squares (e.g., forgetting to square, or summing digits instead of squares).
- Using string conversion (`str(n)`) – works but slower; arithmetic is preferred.
- Not handling `n = 1` correctly (returns True immediately).

## Alternative: Floyd’s Cycle Detection (O(1) space)
Use slow and fast pointers like in Linked List Cycle. Both compute the next sum; if they meet and it's not 1, there's a cycle.
```python
def isHappy(self, n: int) -> bool:
    def next_num(x):
        total = 0
        while x:
            x, d = divmod(x, 10)
            total += d * d
        return total

    slow = n
    fast = next_num(n)
    while fast != 1 and slow != fast:
        slow = next_num(slow)
        fast = next_num(next_num(fast))
    return fast == 1
```

## Memory Hook
> *“Sum of squares, track seen, if repeat → not happy.”*

Or:  
> *“Happy number: square digits, sum, repeat. Cycle? Not happy.”*
