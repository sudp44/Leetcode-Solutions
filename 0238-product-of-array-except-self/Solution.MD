**Product of Array Except Self – Two‑Pass (Left & Right Products)**

---

**Core Idea**  
For each index `i`, `answer[i] = (product of all elements left of i) × (product of all elements right of i)`.  
We build the left part in a forward pass and multiply the right part in a backward pass – all in O(1) extra space (excluding the output array).

---

**Step‑by‑Step (and the “what comes first” rule)**

1. **Initialise**  
   `n = len(nums)`  
   `result = [1] * n`  
   `pre = 1`   ← product of elements **before** current index  
   `post = 1`  ← product of elements **after** current index

2. **First pass – left products (`i = 0` to `n-1`)**  
   ```python
   for i in range(n):
       result[i] = pre      # store left product for index i
       pre = pre * nums[i]  # update pre to include nums[i] for the NEXT i
   ```
   - **Why assignment first?**  
     `result[i]` needs the product of elements **before** `i`, which is currently in `pre` (nums[0]…nums[i-1]). If we multiplied `pre` first, we’d include `nums[i]` and `result[i]` would wrongly contain `nums[i]`.
   - **After** storing, `pre` absorbs `nums[i]` so it’s ready for index `i+1`.

3. **Second pass – right products (`i = n-1` down to `0`)**  
   ```python
   for i in range(n-1, -1, -1):
       result[i] = post * result[i]   # multiply existing left product by right product
       post = post * nums[i]          # update post to include nums[i] for the NEXT (leftwards) i
   ```
   - **Why multiply first?**  
     `result[i]` currently holds the left product. We now need to also include the product of all elements **after** `i`, which is exactly `post`. So `result[i] *= post` (or `result[i] = post * result[i]`).
   - **Then** update `post` by multiplying with `nums[i]` so that the next index (moving left) gets the correct right‑side product.

4. **Return `result`**

---

**Memory Hook**  
> *“Store the old `pre`/`post` before letting the current number join the club.”*  
> – In the first loop: `result[i] = pre`, **then** `pre` takes `nums[i]`.  
> – In the second loop: `result[i] = post * result[i]`, **then** `post` takes `nums[i]`.

---

**Complexity**  
- **Time:** O(n) – two linear passes.  
- **Space:** O(1) extra (the output array is not counted as extra space).

---

**Common Mistakes & Clarifications**  
- **Order in first loop:** `result[i] = pre` **before** `pre *= nums[i]`. Otherwise `nums[i]` contaminates its own left product.  
- **Order in second loop:** `result[i] *= post` **before** `post *= nums[i]`. Otherwise `nums[i]` becomes part of its own right product.  
- **Don’t** initialise `pre`/`post` with anything other than `1` – an empty product is `1`.  
- **Don’t** use division (not allowed). This two‑pointer product method is the intended solution.
