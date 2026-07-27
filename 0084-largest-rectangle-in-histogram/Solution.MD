**Largest Rectangle in Histogram** (monotonic stack)

---

**Problem**  
Given an array of bar heights, find the area of the largest rectangle that can be formed in the histogram.

**Core Technique**  
**Monotonically increasing stack** of **indices**. When a smaller height appears, pop the stack and treat each popped height as the **shortest bar** in a rectangle. Compute the area using the current index as the right boundary and the new stack top as the left boundary.

**Algorithm Steps**  
1. `max_area = 0`, `stack = []`, `n = len(heights)`.  
2. Loop `i` from `0` to `n` (inclusive):  
   - `current_height = heights[i]` if `i < n` else `0` (virtual bar to force emptying the stack).  
   - **While** stack is not empty and `current_height < heights[stack[-1]]`:  
     - Pop `idx = stack.pop()`, `H = heights[idx]`.  
     - **Width**:  
       - If stack is empty → `width = i` (rectangle extends from index 0 to i‑1).  
       - Else → `width = i - stack[-1] - 1` (left boundary is the index just after the new top).  
     - `max_area = max(max_area, H * width)`.  
   - Push `i` onto the stack.  
3. Return `max_area`.

**Why width works**  
- The popped bar `H` is the minimum height of the rectangle.  
- **Right boundary**: the current index `i` (the first bar shorter than `H` to the right).  
- **Left boundary**: the index after the next smaller bar in the stack, which is `stack[-1] + 1` if stack not empty, or `0` if the stack is empty.  
- Width = number of contiguous bars with height ≥ H = `i - left`.  
  - Empty stack: left = 0 → width = `i`.  
  - Non‑empty: left = `stack[-1] + 1` → width = `i - stack[-1] - 1`.

**Why virtual 0?**  
After the loop, the stack may still have bars that never found a right‑side shorter bar. The virtual `0` at index `n` acts as a universal right boundary, ensuring all remaining bars are popped and their rectangles computed.

**Complexity**  
- **Time:** O(n) – each index pushed & popped once.  
- **Space:** O(n) for the stack.

**Common Mistakes**  
- Forgetting to handle the stack‑empty case in width (using `i - stack[-1] - 1` without checking emptiness → index error).  
- Not adding the virtual `0` at the end (incomplete area calculations).  
- Using `pop()` on an empty stack (the `while` condition prevents it).  
- Using the popped index itself as the left boundary (wrong: left is the new top’s index + 1).

**Memory Hook**  
> *“Increasing stack of indices. Smaller bar pops bigger bars — each popped bar is the roof of a rectangle that ends just before the new smaller bar. Width is `i` if stack empty, else `i - top - 1`. A phantom zero clears the leftover.”*
