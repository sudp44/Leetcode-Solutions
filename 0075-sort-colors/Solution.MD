**Sort Colors (Dutch National Flag)**

---

**Problem**  
Sort an array of 0s, 1s, and 2s in‑place in a single pass.

**Core Technique**  
Three pointers (`lo`, `current`, `hi`) partition the array into four regions.

**The Four‑Region Invariant**  
- `[0 … lo-1]` → all **0s** (left bucket, done)  
- `[lo … current-1]` → all **1s** (middle, placed)  
- `[current … hi]` → **unknown** (still to inspect)  
- `[hi+1 … n-1]` → all **2s** (right bucket, done)

**Where does this model come from?**  
1. For two values (0 and 1), we use one boundary `lo` to push 0s left, leaving 1s on the right. Regions: `0s | 1s | unknown`.  
2. For three values, we mirror the idea on the right side for 2s with pointer `hi`. This adds a “2s” region on the right.  
3. The space between `lo` and `hi` is the unknown mix, scanned by `current`.  
→ Think of filling two outer buckets (0s left, 2s right) and leaving 1s in the middle. The scanner `current` moves through the middle, tossing each element to its correct bucket.

**Algorithm Steps**  
- Initialize `lo = 0`, `current = 0`, `hi = len(nums)-1`.  
- **While** `current <= hi`:  
  - **If `nums[current] == 0`**  
    - Swap `nums[lo]` and `nums[current]`.  
    - The element from `lo` is always a `1` (or self‑swap). So `current` can safely advance.  
    - `lo += 1`, `current += 1`.  
  - **If `nums[current] == 1`**  
    - Already in correct zone. `current += 1`.  
  - **If `nums[current] == 2`**  
    - Swap `nums[hi]` and `nums[current]`.  
    - The element from `hi` is **unknown** (could be 0/1/2). **Do NOT increment `current`** – re‑examine next iteration.  
    - `hi -= 1`.

**Why `current` advances only for 0 and 1, not for 2**  
- For 0: we get back a known 1, no need to recheck.  
- For 2: we get back an unknown element from the right; we must check it, so `current` stays put.

**Complexity**  
- **Time:** O(n) – each element examined at most twice.  
- **Space:** O(1) – only three pointers.

**Common Mistakes**  
- Incrementing `current` after a 2‑swap → skips the newly placed element.  
- Misplacing the invariant regions (e.g., thinking `lo` itself is a guaranteed 0).  
- Forgetting that the swap with `lo` when `lo == current` is harmless but still correct.

**Memory Hook**  
> *"0 → swap with lo, advance both. 1 → just move cur. 2 → swap with hi, move only hi—the stranger at cur must be judged next."*  
> *"Two outer buckets (0 left, 2 right), 1s in middle. Scanner cur moves through the unknown middle."*

---


### 1. Why the element from `lo` is always a `1` (not unknown)

The algorithm maintains a precise invariant after every step:

- `[0 … lo-1]` → all **0s**  
- `[lo … current-1]` → all **1s**  
- `[current … hi]` → **unknown**  
- `[hi+1 … n-1]` → all **2s**

When we encounter `nums[current] == 0`, we swap it with `nums[lo]`.

Now, what is at index `lo`?

- If `lo < current`, then `lo` lies inside the region `[lo … current-1]`, which by invariant is all **1s**.  
  So `nums[lo]` must be a `1`.  
  After swapping, the `0` goes to `lo`, and the `1` comes to `current`. A `1` is already in the correct zone, so we can safely move `current` forward without rechecking.

- If `lo == current`, we are swapping the element with itself.  
  No problem—it’s the same `0`, and both `lo` and `current` advance.

So `lo` never holds an unknown value when `current` reaches it; it only holds a `1` (or the same `0` when the pointers coincide).

In contrast, when we swap with `hi`, the element at `hi` is inside the **unknown** region, so it can be `0`, `1`, or `2`. That’s why we cannot advance `current` after a `2` swap—we must examine the new value next iteration.

---

An **invariant** is just a property that stays true before and after every step of the loop. It’s not magic — it’s a guarantee we **actively maintain** by how we update the pointers.

In this algorithm, the invariant is the four‑zone partition:

- `[0 … lo-1]` → all **0s**
- `[lo … current-1]` → all **1s**
- `[current … hi]` → **unknown**
- `[hi+1 … n-1]` → all **2s**

We don’t just assume this. We ensure it by the rules of the three cases.

### Why `nums[lo]` is always a `1` when `lo < current`

Think about how the region `[lo … current-1]` becomes all 1s:

- We only move `current` **without** moving `lo` when we see a **1** at `nums[current]`.  
  So every element that `current` leaves behind (and that `lo` doesn’t advance past) must be a 1.  
  Those elements accumulate in the zone `[lo … current-1]`.

- When we see a **0**, we swap it with `nums[lo]` and then increment **both** `lo` and `current`.  
  This means we don’t create a new gap; `lo` and `current` move together, so the zone `[lo … current-1]` stays unchanged (or shrinks by one on the left and gains a 1 on the right).

- When we see a **2**, we swap with `hi`, but `current` stays, and `hi` moves left. This doesn’t affect the 1s zone at all.

So by the time `lo < current`, every index from `lo` to `current-1` is filled with 1s. Therefore `nums[lo]` is a 1.

### Mini‑example to see it happen

`nums = [1, 0, 1]`

| Step | lo | current | hi | nums | action |
|------|----|---------|----|------|--------|
| init | 0  | 0       | 2  | [1,0,1] | `1` → just `current++` |
| 1    | 0  | 1       | 2  | [1,0,1] | `0` → swap with lo (0): [0,1,1]; `lo=1`,`current=2` |
| 2    | 1  | 2       | 2  | [0,1,1] | `1` → `current=3` > hi → stop |

At the moment we swapped the `0` (step 1), `lo=0, current=1`. The region `[0,0]` contained `nums[0]=1`, exactly as the invariant promised. That 1 came from the previous step where we saw a 1 and just moved `current` forward, leaving `lo` behind.

### Why not “unknown” like from `hi`?

- `hi` points into the **unknown** region `[current … hi]`, so when we swap with `hi`, we are pulling an **unprocessed** element – it could be 0, 1, or 2. We can’t trust it.
- `lo` points into the **processed 1s** region (if `lo < current`). That region has already been inspected and cleared of 0s and 2s. Hence it’s safe.

We start with the invariant true, and every operation preserves it. Therefore at any point, the invariant tells us exactly what value sits at `lo`.

---

### 2. Why `while current <= hi` and not `while current < hi`

Because the unknown region is **inclusive of `hi`**:

```
[lo, current-1]  → 1s
[current, hi]    → unknown
```

When `current == hi`, there is exactly **one unknown element left** at index `current`. We still need to process it. If the loop condition were `current < hi`, that last element would be skipped.

**Example:**

`nums = [2, 0, 1]` after a few steps might reach `current = hi` with the remaining element still needing sorting. Using `<` would leave that element unprocessed.

Only when `current > hi` is the unknown region completely empty, and the array is sorted.

---

### Quick memory hook

- **`lo` gives a `1`** because it points into the already-processed 1s zone.  
- **`hi` gives unknown** because it points into the unprocessed zone.  
- **`current <= hi`** because `hi` is still unknown—process it too.
