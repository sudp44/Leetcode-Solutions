**Task Scheduler**

---

## 1. Problem restatement
You have a list of tasks (represented by letters) and an integer `n` (cooldown period).  
Two **same** tasks must be separated by at least `n` units of time.  
At each time unit, you can either execute a task or stay idle.  
Find the **minimum number of time units** needed to finish all tasks.

**Example**  
`tasks = ["A","A","A","B","B","B"], n = 2`  
One optimal schedule:  
`A -> B -> idle -> A -> B -> idle -> A -> B`  
Length = 8.

---

## 2. Core intuition – greedy with the most frequent task
The bottleneck is the **most frequent task**.  
Let’s say task `A` appears `f_max` times.  
To schedule all `A`’s with at least `n` spaces between them, you need **at least**  
`(f_max - 1) * (n + 1) + 1` slots just for `A`.  

But if there are multiple tasks with the same maximum frequency, they can share those slots. The problem is to fill the remaining slots with other tasks or idle.

The **optimal greedy strategy**:
- At every “cycle” of length `n+1` (the cooldown width + the task itself), pick up to `n+1` distinct tasks that are **most frequent** at that moment.
- This minimises the idle time because we always use the most urgent tasks first (the ones with highest remaining counts).  
  If we don’t have enough distinct tasks to fill a cycle, the remaining slots become idle.

---

## 3. Algorithm step‑by‑step (using a max‑heap)

### Step 1 – Count frequencies
We count how many times each task appears.  
e.g. `tasks = ["A","A","A","B","B","B","C","C"]` →  
`freq = {A:3, B:3, C:2}`

### Step 2 – Build a max‑heap of frequencies
We use a max‑heap so we can always grab the task with the highest remaining count.  
Python has a min‑heap, so we push **negative** frequencies.  
Heap: `[-3, -3, -2]` (representing 3, 3, 2)

### Step 3 – Simulate cycles
We keep a variable `time = 0`.  
Repeat until the heap is empty:

- **Start a new cycle of length `n+1`** (because after performing one task, you must wait `n` slots before doing another of the same type). In this cycle we will try to fill up to `n+1` slots with **different** tasks.
- Create a temporary list `temp` to store the frequencies of the tasks we execute in this cycle.
- For `i` in `0` to `n` (i.e. `n+1` times):
  - If the heap is not empty: pop the largest frequency (`-f`), convert it to positive `f`, and add it to `temp`.
  - If the heap is empty, we have no more distinct tasks available – the rest of the cycle will be idle slots, but we don’t explicitly track idle; we just stop picking.
- Now we’ve taken up to `n+1` tasks out. For each frequency `f` in `temp`:
  - Decrease it by 1 (we executed the task once).
  - If the resulting frequency is still > 0, push it back into the heap (as negative).
- **Update `time`**:
  - If the heap is **not empty**, we know the cycle was completely full with tasks, so we spent exactly `n+1` time units (no idle).  
  - If the heap is **empty**, this was the last batch. We only need to add the actual number of tasks we executed in this cycle (i.e. `len(temp)`) because there’s no need to add trailing idle time after all tasks are done.

### Step 4 – Return `time`

---

## 4. Walkthrough with a concrete example

Let’s use `tasks = ["A","A","A","B","B","B","C","C"]` and `n = 2`.

**Frequencies:** `A:3, B:3, C:2`  
Heap: `[-3, -3, -2]`

**Cycle 1** (n+1 = 3 slots)
- Pop: 3 → temp = [3], heap = [-3, -2]
- Pop: 3 → temp = [3, 3], heap = [-2]
- Pop: 2 → temp = [3, 3, 2], heap = []   (only 3 distinct tasks)
- We filled all 3 slots with A, B, C.
- Decrease each: [2, 2, 1]. Push back those >0: `[-2, -2, -1]`.
- Heap not empty → `time += 3` → time = 3.

**Cycle 2**
- Pop: 2 → temp = [2], heap = [-2, -1]
- Pop: 2 → temp = [2, 2], heap = [-1]
- Pop: 1 → temp = [2, 2, 1], heap = []   (again 3 tasks)
- Decrease: [1, 1, 0]. Push back: `[-1, -1]`.
- Heap not empty → `time += 3` → time = 6.

**Cycle 3**
- Pop: 1 → temp = [1], heap = [-1]
- Pop: 1 → temp = [1, 1], heap = []
- i = 2: heap empty → stop picking.
- temp = [1, 1], we only did 2 tasks.
- Decrease: [0, 0]. Push back none (all exhausted).
- Heap **is** empty → this is the last batch.  
  `time += len(temp) = 2` → time = 8.

Heap empty, loop ends. Return `time = 8`.

The schedule would be:
Cycle1: A B C
Cycle2: A B C
Cycle3: A B (no C needed, we stop)
Total 8 slots, matching the optimal.

---

## 5. Why `time += maxHeap.isEmpty() ? temp.size() : n + 1`?
- If there are still tasks remaining after this cycle, the CPU was busy the whole time (either executing tasks or idle), so the interval took exactly `n+1` units.
- If this was the final cycle (heap empty), we only executed `temp.size()` tasks and then we’re done; we shouldn’t add extra idle time.

---

## 6. Complexity
- **Time:** O(t log 26) ≈ O(t) where `t` = total number of tasks. The heap size never exceeds 26 (uppercase English letters). Each push/pop is O(log 26) ≈ O(1).
- **Space:** O(1) extra — heap and temp list are bounded by 26.

---

## 7. Complete Python code (with comments)

```python
from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        # max-heap via negative frequencies
        max_heap = [-f for f in freq.values()]
        heapq.heapify(max_heap)

        time = 0

        while max_heap:
            temp = []
            # try to fill a full cycle of (n+1) distinct tasks
            for _ in range(n + 1):
                if max_heap:
                    # pop the most frequent task (largest positive frequency)
                    temp.append(-heapq.heappop(max_heap))
                else:
                    break  # no more distinct tasks available, remaining slots = idle

            # execute each taken task once, re-add if still remaining
            for f in temp:
                f -= 1
                if f > 0:
                    heapq.heappush(max_heap, -f)

            # if heap still has tasks, we spent a full (n+1) cycle;
            # otherwise it's the final batch and we only count the tasks we ran.
            time += (n + 1) if max_heap else len(temp)

        return time
```

---

## 8. Memory hook for quick recall

> *“Greedy with max‑heap of frequencies. Each cycle = n+1 slots; pick up to n+1 most frequent tasks. After processing, if heap not empty → full cycle time; else → only actual tasks in last batch. Heap size ≤ 26, so O(t) time.”*

**One‑line essence:**  
*Always schedule the most frequent task that can still run; pack cycles of size n+1; the last cycle may be shorter.*
