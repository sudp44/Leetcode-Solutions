**Longest Consecutive Sequence**

---

**Problem**  
Find the length of the longest consecutive elements sequence in an unsorted array. Must run in O(n) time.

**Core Idea**  
- Turn the array into a **set** for O(1) lookups.  
- Only attempt to build a sequence from a number if it is the **start** of a sequence (i.e., `num-1` not in set).  
- For each start, count how many consecutive numbers (`num+1, num+2, …`) exist in the set.  
- Track the maximum length.

**Why iterate over `numSet` instead of `nums`?**  
- **Avoid duplicate work:** If `nums` has repeats, iterating over the original array would start the same sequence multiple times, wasting time.  
- **Set gives unique elements:** The set contains each number only once, so each potential sequence start is processed at most once.  
- **Still O(n) time:** Building the set is O(n); iterating over the set and expanding sequences looks at each element at most twice (once when checking start, once when counted in a sequence). Total O(n).

**Algorithm Steps**  
1. If array is empty, return 0.  
2. Create `numSet = set(nums)`.  
3. Initialize `lcs = 1` (any single element is length 1).  
4. For each `num` in `numSet`:  
   - If `num - 1` is **not** in set → `num` is the start of a sequence.  
   - Count consecutive numbers: while `num+1` in set, increment count and move to next number.  
   - Update `lcs` if current sequence length is larger.  
5. Return `lcs`.

**Complexity**  
- **Time:** O(n) – building set O(n), and each number is visited O(1) times overall because the while‑loop only runs for sequence starts and each number is part of exactly one sequence.  
- **Space:** O(n) for the set.

**Key Insight**  
Only start counting at numbers that have no left neighbour (`num-1` not in set). This guarantees each sequence is built exactly once from its smallest element.

**Memory Hook**  
> “Set for O(1) check. Only build from the smallest element of a streak (`num-1` absent). Iterate on set, not array, to skip duplicates.”
