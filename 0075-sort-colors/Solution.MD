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
