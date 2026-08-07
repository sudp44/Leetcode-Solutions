**Find Median from Data Stream**

---

## 📌 **Problem**
Design a data structure that supports:
- `addNum(num)` – insert an integer
- `findMedian()` – return the median of all inserted numbers

## 💡 **Core Idea**
Maintain two heaps:
- **max‑heap** (`lo`) – stores the **smaller half** of the numbers
- **min‑heap** (`hi`) – stores the **larger half**

Then:
- If total count is **odd**, median = top of `lo`
- If total count is **even**, median = average of tops of `lo` and `hi`

## 🏗️ **Data Structures**
- `self.lo` → **max‑heap** (Python: min‑heap storing **negatives**)
- `self.hi` → **min‑heap** (standard)
- Invariant: `len(lo) == len(hi)` or `len(lo) == len(hi) + 1`

## 🧮 **Algorithm Steps**

### **`addNum(num)`**
1. Push `-num` onto `lo` (max‑heap).  
2. Pop the largest from `lo` (i.e., `-heapq.heappop(lo)`) and push it onto `hi`.  
3. If `len(lo) < len(hi)`, pop the smallest from `hi` and push its negative back to `lo`.  
   → This ensures `lo` always has the smaller half and is never smaller in size than `hi`.

### **`findMedian()`**
- If `len(lo) > len(hi)` → `-lo[0]` (the largest of the smaller half)
- Else → `(-lo[0] + hi[0]) / 2.0`

## ⏱️ **Complexity**
- `addNum`: **O(log n)** – each push/pop is O(log n)
- `findMedian`: **O(1)** – just reads the top(s)
- Space: **O(n)** for the two heaps

## 🔑 **Key Points**
- We **always add to `lo` first**, then rebalance → guarantees the invariant.
- The balancing step moves one element from `lo` to `hi` unconditionally, then corrects sizes if needed.
- Python has no built‑in max‑heap → we store **negative** numbers in `lo`.
- `lo[0]` is the *smallest* negative, i.e., the *largest* positive value → the true top of the max‑heap.
- Median of an even count uses **true division** (`/ 2.0`) to get a float.

## ⚠️ **Common Mistakes**
- Forgetting to negate when pushing/poping `lo` (leads to min‑heap behavior).
- Reversing the roles of `lo` and `hi` in `findMedian`.
- Not maintaining the size invariant strictly.
- Using integer division (`//`) for even‑count median (should be float).

## 🧠 **Memory Hook**
> *“Add to lo, move max to hi, then if lo is too small, move min back to lo. Median: if lo bigger → top of lo, else average of both tops.”*

And for the negation trick:  
> *“Max‑heap? Just flip signs. Push `-num`, pop `-val`.”*
