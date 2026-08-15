### ✅ How single side max is enough to get the water level?

- We only move `left` forward when `height[left] < height[right]`.
- If the new left bar becomes a fresh `left_max`, then at that exact moment, `right` is pointing to a bar that is **taller** than this new left_max (since `height[right] > height[left]`).  
  Therefore `left_max < height[right] <= right_max`.
- If the left bar is **not** a fresh max, then `left_max` is older. But the only way `left_max` could have been set to that older value is that **some earlier `right`** was taller, allowing the left pointer to move past it. That older right bar remains inside `right_max`, so `left_max <= right_max`.

> `left_max <= right_max`

> **Whenever we process the left pointer, `left_max` is guaranteed to be ≤ `right_max`. Therefore, the water level at `left` is determined solely by `left_max`.**

### 🧠 Why this invariant is true (the deeper reason)

1. We initialise `left_max = height[0]` and `right_max = height[n-1]`.
2. We move the **right** pointer left whenever `height[left] >= height[right]`. Each time we do, we update `right_max = max(right_max, height[right])`.
3. We stop moving the right pointer only when `height[left] < height[right]`. At that point, `right_max` is at least as large as the current `height[right]`, which is larger than the current `height[left]`.
4. If `left_max` is larger than the current `height[left]`, it must have been created earlier, when a previous left bar satisfied `height[left] < height[right]`, and that right bar is still part of `right_max`. So `left_max` never outgrows `right_max`.

Thus, the **bottleneck is always `left_max` for left bars**.
