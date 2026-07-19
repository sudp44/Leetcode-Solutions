**First Missing Positive** (in‑place, O(n) time, O(1) space)

---

**Problem**  
Find the smallest positive integer missing from an unsorted array.  
The answer is always in `1 … n+1` (where `n = len(nums)`).

**Core Idea**  
Use the array’s **indices as a native hash set** to mark which numbers `1..n` are present.  
- Number `x` is represented by the **sign of `nums[x]`** (negative = present).  
- Special case: `x = n` uses `nums[0]` as its marker (since index `n` would be out of bounds).

---

### Steps & Rationale

1. **Check if `1` exists** – If not, return `1` immediately.  
   *Why?* `1` is the smallest possible answer; also, we’ll later use `1` as a safe placeholder for invalid values.

2. **Clean the array** – Replace all numbers `≤ 0` or `> n` with `1`.  
   *Why?* Only numbers in `1..n` can affect the answer. Replacing garbage with `1` is safe because we already confirmed `1` exists – no false positives introduced.

3. **Mark presence** – For each `i`, let `a = abs(nums[i])`.  
   - If `a == n`: mark `nums[0]` negative (`nums[0] = -abs(nums[0])`).  
   - Else: mark `nums[a]` negative (`nums[a] = -abs(nums[a])`).  
   *Why `abs`?* A cell might already be negative from an earlier mark. `abs` recovers the original number so we mark the correct index.  
   *Why `-abs` and not just `-`?* Prevents flipping a negative value back to positive if the same number appears multiple times (idempotent marking).

4. **Find the first missing** –  
   - Loop `i = 1 … n-1`: if `nums[i] > 0` (i.e., not marked), return `i`.  
   - If `nums[0] > 0`, return `n`.  
   - Otherwise, return `n+1`.  
   *Why this order?* Smallest first: `1..n-1` checked before `n`.

---

### Key Insights (the “why” behind the trick)

- **Answer bounded by `n+1`**: You can’t fit `n+1` distinct positives in `n` slots, so the first missing is at most `n+1`.
- **`abs` is critical**: Without it, you lose the original number after a cell becomes a marker (read negative index → wrong marking).
- **Early `1` check**: Both early exit and guarantees the placeholder `1` used in cleaning doesn’t create a fake positive.
- **Index `0` stores `n`**: Because valid indices go up to `n-1`, we recycle index `0` (which otherwise would never be used, since `1` uses index `1`).

---

### Complexity

- **Time**: O(n) – three linear passes (check 1, clean, mark, scan). Each element visited O(1) times.
- **Space**: O(1) – only a few variables, modifies input array in place.

---

### Common Mistakes

- Forgetting the initial check for `1` – leads to marking with a `1` that might not exist.
- Replacing invalid numbers with something other than `1` (e.g., `-1`) – breaks the positive‑invariant before marking.
- Not using `abs` when reading `a = nums[i]` – negative indices corrupt marking.
- Not using `-abs` when writing markers – duplicates can flip sign back to positive.
- Checking `nums[0]` before indices `1..n-1` – may return a larger missing number while a smaller one exists.

---

**Memory Hook**  
> “Check 1, clean with 1, mark with `-abs`, scan small to big – answer always 1..n+1.”
