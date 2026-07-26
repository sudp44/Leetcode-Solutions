**Minimum Remove to Make Valid Parentheses**

---

**Problem**  
Given a string with parentheses and other characters, remove the minimum number of parentheses so the resulting string is valid. Return **any** valid string.

**Core Technique**  
**Stack + Set** – first pass to identify unmatched parentheses, second pass to build the result skipping those indices.

**Algorithm Steps**  
1. Initialize an empty `stack` (for indices of unmatched `'('`) and an empty `set` (`remove_indices`).  
2. **First pass** – iterate over `enumerate(s)`:  
   - If `ch == '('`: push its index onto the stack.  
   - If `ch == ')'`:  
     - If stack is empty → no matching `'('` → add index to `remove_indices`.  
     - Else → pop the stack (match found).  
3. After the loop, any indices left in the stack are unmatched `'('` → add all of them to `remove_indices` (`remove_indices.update(stack)`).  
4. **Second pass** – build result: join all characters whose index is **not** in `remove_indices`.

**Complexity**  
- **Time:** O(n) – two passes.  
- **Space:** O(n) – stack + set, plus the output string.

**Why it works**  
- A `')'` without a prior unmatched `'('` can never be part of a valid string → must be removed.  
- Any `'('` that remains unmatched after the whole string must be removed.  
- By saving indices and rebuilding, we preserve all other characters in order.

**Common Mistakes**  
- Forgetting to transfer leftover stack indices into the removal set.  
- Using only a counter instead of a stack (loses position information for unmatched `'('`).  
- Using `remove` methods that modify the string while iterating (avoid by building a new one).

**Memory Hook**  
> *"Stack matches pairs; set marks loners. Rebuild skipping marked spots."*
