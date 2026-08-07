## 📘 Problem Description

```
759. Employee Free Time
Level
Hard

Description
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined). Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.


Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]

Output: [[3,4]]

Explanation: There are a total of three employees, and all common free time intervals would be [-inf, 1], [3, 4], [10, inf].

We discard any intervals that contain inf as they aren’t finite.

Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]

Output: [[5,6],[7,9]]

Constraints:

1 <= schedule.length , schedule[i].length <= 50
0 <= schedule[i].start < schedule[i].end <= 10^8
```

---

## 🧪 Complete Python Solution (runnable in any online compiler)

```python
import heapq
from typing import List

# The Interval class exactly as defined in the problem
class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"[{self.start}, {self.end}]"

class Solution:
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:
        # 1. Flatten all intervals into a min-heap sorted by start time
        heap = []
        for employee in schedule:
            for interval in employee:
                # push a tuple (start, interval) so the heap orders by start
                heapq.heappush(heap, (interval.start, interval))

        if not heap:
            return []

        # 2. Pop the very first interval as the "current" merged interval
        _, prev = heapq.heappop(heap)
        result = []

        # 3. Process remaining intervals in chronological order
        while heap:
            _, curr = heapq.heappop(heap)
            if prev.end < curr.start:
                # A gap exists → it is common free time
                result.append(Interval(prev.end, curr.start))
                prev = curr          # the current interval becomes the new reference
            else:
                # Intervals overlap (or touch) → merge by extending the end if needed
                if curr.end > prev.end:
                    prev.end = curr.end

        return result

# ---------------------------
# Test the solution
if __name__ == "__main__":
    def build_schedule(data):
        return [[Interval(s, e) for s, e in emp] for emp in data]

    sol = Solution()

    # Example 1
    sched1 = build_schedule([[[1,2],[5,6]], [[1,3]], [[4,10]]])
    print("Example 1:", sol.employeeFreeTime(sched1))
    # Expected: [[3,4]]

    # Example 2
    sched2 = build_schedule([[[1,3],[6,7]], [[2,4]], [[2,5],[9,12]]])
    print("Example 2:", sol.employeeFreeTime(sched2))
    # Expected: [[5,6],[7,9]]

    # Edge case: empty schedule
    print("Empty:", sol.employeeFreeTime([]))
    # Expected: []
```

Copy this entire block into any Python 3 online environment (Replit, Programiz, etc.) and run it to see the outputs.

---

## 🧠 Deep Recall Notes – Employee Free Time

### 1. The Core Intuition

Imagine putting every employee's working intervals on a single timeline. The times when **everyone** is free are exactly the gaps in the **merged union** of all their busy intervals.

Why?  
- If we combine all busy intervals from all employees, we get a set of time spans where **at least one person** is working.  
- The empty spaces left on the timeline after we overlay all these busy intervals are periods where **nobody** is working.  
- Those empty spaces are the common free time.

So the problem reduces to:
1. **Merge** all intervals (regardless of employee) into a list of non‑overlapping busy blocks.
2. **Collect the gaps** between those blocks.

This is exactly the same idea as the classic **"Merge Intervals"** problem, but here we don't return the merged busy intervals; we return the **gaps** between them.

### 2. How the algorithm works

**Step 1 – Flatten & Sort**  
We have separate lists for each employee, already sorted per employee. But overall the intervals are mixed. We need to process them chronologically by `start`.  
We use a **min‑heap** to efficiently sort all intervals by their start time. (An alternative is to put everything into a list and call `sorted()`, which has the same complexity.)

**Step 2 – Initialize the first interval**  
Take the earliest starting interval and call it `prev`. This will represent the **current merged busy block**.

**Step 3 – Sweep through the rest**  
For each next interval `curr` in chronological order:
- **If `prev.end < curr.start`**:  
  There is a gap between the end of the previous busy block and the start of this new interval.  
  That gap (`prev.end` → `curr.start`) is a time when **no employee** is working.  
  ➡️ Add this gap to the result.  
  Then we move on: set `prev = curr` because the new block begins after the gap.

- **If `prev.end >= curr.start`**:  
  The intervals overlap (or touch). This means the busy period extends continuously.  
  We merge them by extending the end of `prev` if `curr.end` is later.  
  (Note: touching intervals like `[1,2]` and `[2,3]` do **not** create a gap; they are continuous work.)

**Step 4 – End of list**  
After processing all intervals, any remaining gaps before the first busy block or after the last one are infinite in the original universe (`-inf` to first start, and last end to `inf`). The problem explicitly discards them, so we don't add them.

### 3. Why this is correct

- **Completeness**: Every possible free interval is a gap between two consecutive busy intervals in the merged timeline. There's no way for a free period to exist inside a merged busy block or outside the bounds of all merged blocks (except the infinite tails we discard).  
- **Optimality**: The algorithm runs in O(N log N) time and O(N) space, which is optimal for a comparison‑based approach.

### 4. Edge cases & constraints

- **Empty schedule**: return `[]`.
- **Only one employee**: the result is still the gaps in that employee's schedule? Wait – if only one employee, common free time is just the gaps in that employee's schedule? Actually, "common free time for all employees" means everyone is free. With one employee, that's exactly the gaps in his schedule (excluding -inf and +inf). So the merge logic works fine: it merges that employee's intervals (they are already non‑overlapping) and collects gaps between them.  
- **Adjacent intervals with `end == start`**: these are not gaps; they touch, so no free time.
- **All intervals overlapping into one continuous block**: no gaps, return `[]`.

### 5. Complexity

- **Time**: O(N log N) where N = total number of intervals across all employees. We push all intervals into the heap (each push O(log N)), then pop each one (each pop O(log N)). Sorting all intervals directly would also be O(N log N).  
- **Space**: O(N) for the heap (or for a sorted list if using that approach).

### 6. Memory Hook

> **“Flatten all busy intervals, sort by start, merge them, and wherever you see a jump between the end of one merged block and the start of the next, that jump is free for everyone.”**

**One‑line summary:** *Common free time = gaps in the merged union of all busy intervals.*

**Key picture:**
```
Emp A: [----]      [--------]
Emp B:    [---]         [----]
Emp C:          [--]          [---]
Merged: [----][--][---] [----] [---]
                        ^      ^
                     free time free time (ignore infinite tails)
```
