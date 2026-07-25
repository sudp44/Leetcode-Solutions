**Daily Temperatures** (monotonic decreasing stack)

---

**Problem**  
Given an array of daily temperatures, return an array where for each day you tell how many days you would have to wait until a warmer temperature. If no warmer day exists, put 0.

**Core Technique**  
**Monotonic decreasing stack** storing **indices** of unresolved days (those still waiting for a warmer day). The stack’s temperatures (values at those indices) are always in decreasing order from bottom to top.

**Algorithm Steps**  
1. Initialize `answer = [0] * n` and an empty stack.  
2. Iterate `i` from 0 to n‑1:  
   - **While** stack is not empty and `temperatures[i] > temperatures[stack[-1]]`:  
     - Pop the top index `idx`.  
     - Set `answer[idx] = i - idx` (the number of days between the two).  
   - Push `i` onto the stack.  
3. Return `answer`. (Indices left in the stack never found a warmer day; their answer remains 0 by default.)

**Why it works**  
- The stack only contains days that haven’t yet seen a warmer temperature.  
- Because we pop when we find a warmer temperature, the temperatures corresponding to indices in the stack are strictly decreasing.  
- Each index is pushed once and popped once → O(n) time.

**Complexity**  
- **Time:** O(n) – each index pushed/popped at most once.  
- **Space:** O(n) – worst‑case stack size (e.g., decreasing temperatures).

**Key Intuition**  
> *“When you find a warmer day, it resolves all previous colder days that are waiting.”*

**Common Mistakes**  
- Storing temperatures instead of indices (need indices to compute distance).  
- Forgetting to set default answer to 0 for days that never get a warmer temperature.  
- Using a strictly increasing stack instead of decreasing.

**Memory Hook**  
> *“Stack indices of unresolved days. When a warmer day comes, pop and fill the gap. Stack stays decreasing.”*
