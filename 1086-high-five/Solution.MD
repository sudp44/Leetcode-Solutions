**1086. High Five** including a ready‑to‑run test snippet

---

**Problem**  
For each student, compute the average of their top 5 scores (integer division). Return `[id, avg]` sorted by id.

**Core Technique**  
Use a **max‑heap per student** to efficiently get the top 5 scores. Python only has a min‑heap, so we push **negated** scores.

**Steps**  
1. `scores = defaultdict(list)` – each value is a heap (list).  
2. For each `[id, score]` in `items`:  
   - `heapq.heappush(scores[id], -score)`   (simulate max‑heap).  
3. For each `id` in sorted order:  
   - Pop 5 times, accumulating `total += -heapq.heappop(scores[id])`.  
   - Append `[id, total // 5]` to result.  
4. Return result.

**Code**  
```python
import heapq
from collections import defaultdict

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list)
        for sid, score in items:
            heapq.heappush(scores[sid], -score)
        
        res = []
        for sid in sorted(scores.keys()):
            total = 0
            for _ in range(5):
                total += -heapq.heappop(scores[sid])
            res.append([sid, total // 5])
        return res
```

**Complexity**  
- Time: O(n log 5 + m log 5) ≈ O(n) where n = total scores, m = number of students.  
- Space: O(n) to store all scores in heaps.

**Common Mistakes**  
- Forgetting to negate scores (would pop smallest instead of largest).  
- Not sorting student IDs (output must be sorted).  
- Assuming integer division floor – it’s fine because total is positive.

**Memory Hook**  
> *“Max‑heap per student via negative scores. Push all, then pop top 5. Sorted IDs at the end.”*

---

**Run the code yourself**  
Copy this entire script into any Python 3 online compiler (e.g., [Replit](https://replit.com/), [Programiz](https://www.programiz.com/python-programming/online-compiler/)) to test with the example:

```python
import heapq
from collections import defaultdict
from typing import List

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list)
        for sid, score in items:
            heapq.heappush(scores[sid], -score)
        res = []
        for sid in sorted(scores.keys()):
            total = 0
            for _ in range(5):
                total += -heapq.heappop(scores[sid])
            res.append([sid, total // 5])
        return res

# Test with example
if __name__ == "__main__":
    items = [
        [1,91], [1,92], [2,93], [2,97], [1,60],
        [2,77], [1,65], [1,87], [1,100], [2,100], [2,76]
    ]
    sol = Solution()
    print(sol.highFive(items))   # Expected: [[1, 87], [2, 88]]
```