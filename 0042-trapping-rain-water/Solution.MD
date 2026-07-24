**Trapping Rain Water** (two‑pointer), focusing on the invariant that makes `left_max` sufficient

---

**Problem**  
Given an array of bar heights, compute total water trapped after raining.

**Core Technique**  
Two pointers (`left`, `right`) with running maximums (`left_max`, `right_max`). Process the side with the smaller height each step.

**Algorithm Steps**  
1. `left = 0`, `right = n-1`, `left_max = height[left]`, `right_max = height[right]`, `total = 0`.  
2. While `left < right`:  
   - **If `height[left] < height[right]`:**  
     - Update `left_max = max(left_max, height[left])`.  
     - Add `left_max - height[left]` to `total`.  
     - `left += 1`.  
   - **Else:**  
     - Update `right_max = max(right_max, height[right])`.  
     - Add `right_max - height[right]` to `total`.  
     - `right -= 1`.  
3. Return `total`.

**Why `left_max` alone works (the invariant)**  
When we process a left bar, the condition `height[left] < height[right]` guarantees that the right side has at least one bar taller than the current left bar.  
Therefore, the **true** right maximum is at least `height[right]`, making `left_max` the bottleneck (`min(left_max, true_right_max) = left_max`).  
We do not need to know the exact right maximum – `left_max` is enough.

**Why the invariant never breaks**  
- To move `left` past a tall bar, we previously needed an even taller bar on the right (`height[right] > that tall bar`).  
- That tall right bar remains in the right‑side suffix as the right pointer moves inward, so `right_max` stays ≥ that tall right bar ≥ `left_max`.  
- Consequently, `left_max ≤ right_max` always holds when processing a left bar.

**Complexity**  
- **Time:** O(n) – each bar visited once.  
- **Space:** O(1) – only four integers.

**Common Mistakes**  
- Updating `right_max` with `height[left]` instead of `height[right]`.  
- Processing the wrong pointer – always the side with **smaller** `height`.  
- Forgetting that `left_max - height[left]` is zero when the bar is a new maximum (no water there).

**Memory Hook**  
> *“Short side moves. The moving pointer’s max is the bottleneck because the stationary side holds a taller bar – captured in the other max.”*  
Or more concisely: **“Short moves, tall stays, max of short side limits water.”**

---

### The Core Confusion
A case like:  
`left_max = 10`, current `height[left] = 1`, `height[right] = 2`, and the true right maximum is only 2.  
If that happened, the real water would be `min(10,2) - 1 = 1`, but the algorithm would use `left_max - 1 = 9`, giving a wrong answer.

**But this scenario can never occur in the algorithm.**  
Let’s see exactly why.

---

### The Invariant that Protects Us

When we are about to process a left bar (i.e., when `height[left] < height[right]`), we always have the guarantee:

\[
\text{left\_max} \le \text{right\_max}
\]

where `right_max` is the maximum height from the current `right` index to the **end** of the array.  
If this holds, then `min(left_max, true\_right\_max) = left_max` (because `true_right_max ≥ right_max ≥ left_max`), so we can safely use `left_max`.

**How do we know left_max ≤ right_max?**

- `left_max` can only become large if we previously **moved the left pointer past a tall bar**.
- To move past that tall bar, the algorithm required `height[left] < height[right]` at that earlier moment. So there was a right bar **even taller** than that tall left bar.
- That even taller right bar remains in the suffix that `right_max` covers (because as the right pointer moves left, the suffix only grows; it never drops bars that were once to the right of the current right pointer).  
  Therefore, `right_max` stays at least as large as that very tall right bar, which was larger than the tall left bar. So `right_max` remains ≥ that tall left bar = `left_max`.

Thus, `left_max` is always ≤ `right_max` whenever we process a left pointer. The dangerous situation where `left_max` towers over the true right maximum cannot arise.

---

### Concrete Example Where It Might Seem to Fail – But Works

Take `heights = [10, 1, 2]`.  
- `left=0` (10), `right=2` (2). Since `10 < 2` is false, we process **right**, not left.
- The left pointer never leaves the 10, so we never process the middle `1` using `left_max`.  
  Instead, the middle `1` is processed as a **right** bar (when `right` moves onto it), and its water is computed using `right_max`.

So the algorithm cleverly avoids the bad case by never moving `left` past a bar that is taller than all remaining right bars.

---

### What Happens When `left_max` Really Is High?

For `left_max` to become, say, 10, we must have moved the `left` pointer past a bar of height 10. That requires that at that moment, `height[right]` was **greater than 10**. For example:

`heights = [10, 1, 12, 3]`  
- `left=0` (10), `right=2` (12). `10<12` → process left: `left_max` becomes 10, `left` moves to 1.
- `left=1` (1), `right=2` (12). `1<12` → process left: `left_max` remains 10 (since max(10,1)=10), water added = 10‑1 = 9, correct because `right_max` here is at least 12.
- The tall right bar (12) ensures `right_max` ≥ 12, so `left_max` is still the bottleneck.

No overcount.

---

### Memory Hook to Replace the Confusion

> **“The side with the smaller height moves. To move left past a tall bar, we must have already seen an even taller right bar — and that right bar stays in `right_max` forever. So when we process left, `left_max` is always ≤ `right_max`. Therefore, `left_max` alone decides the water.”**

In one line: **“The moving pointer’s max is always the limiting one, because the stationary side holds a taller bar that has been, or will be, captured in the other max.”**

Yes, that's exactly it! You've nailed the invariant. Let me confirm and refine your wording just a tiny bit, then give a final memory anchor.

---

### Understanding

1. **To move `left` past a bar, we must have seen a taller bar on the right.**  
   Because the algorithm only moves `left` when `height[left] < height[right]`. So when `left` advances, we know that at that moment, the right side has a bar higher than the one we're leaving behind.

2. **That tall right bar stays in the right side's "domain".**  
   The right pointer only moves when `height[right] <= height[left]`. So if the right bar was taller than the left, the right pointer **stays put** – it doesn't move until the left side catches up.  
   Therefore, that tall right bar remains in the suffix that `right_max` covers. So `right_max` (the maximum of the right side we've seen) is at least as large as that tall right bar.

3. **Thus, `left_max` (which can be at most the height of the tallest bar we've passed on the left) cannot exceed `right_max` (which includes that tall right bar).**  
   Since the tall right bar enabled us to pass the left bar, `right_max` ≥ that tall right bar > the left bar we left behind. So `left_max` is always ≤ `right_max`.

4. **When we are now at the current `left` (after advancing), we may be on a smaller or larger bar.**  
   If larger, `left_max` updates to this new bar, but still ≤ `right_max` because the right side still has that tall bar (or an even taller one).  
   If smaller, `left_max` stays the same, still ≤ `right_max`.

5. **Therefore, for the current `left`, the bottleneck is `left_max`**, and water added is `left_max - height[left]`.

The only tiny nuance: `right_max` as maintained in the algorithm is the max of the bars **from the current `right` pointer to the end**, and that includes the tall right bar that enabled left to move. So indeed `left_max <= right_max` always holds when processing a left bar.

---

### Final memory hook

> **"To move left, a taller right must exist. That right bar stays until left catches up, so right_max dominates left_max. Hence left_max is the bottleneck."**

Or even shorter:

> **"Tall right guards left; left_max never outgrows right_max."**

---

- **Whenever the algorithm moves the left pointer, there is at least one bar on the right (the one that caused `height[left] < height[right]`) that is taller than the tallest bar on the left up to that point.**  
- **The right pointer never moves past that tall bar until the left side grows taller than it (or equal), which can only happen if an even taller left bar is encountered, but then that left movement would again require an even taller right bar to exist.**  
- **Thus, at every step where we process a left bar, the right side contains at least one bar that is strictly taller than the maximum height seen on the left (`left_max`).**  
- **Therefore, `left_max` is always strictly less than the true maximum on the right (or at most equal in edge cases), making `left_max` the bottleneck for the current left position.**  

**The "tall right bar" that allowed the left to move remains in place (the right pointer hasn't moved past it yet), so `right_max` (which includes that bar) is at least that tall right bar's height, which is greater than any `left_max` that existed at that moment. Even if `left_max` later grows as we encounter taller left bars, those new left bars were only passed because we compared them to an **even taller right bar** that is still in the right side's domain. So `left_max` never outgrows `right_max`.**

**Bottom line:** The side with the moving pointer always has its own max as the limiting factor because the other side holds a “guard” bar that is taller than anything seen on the moving side.
