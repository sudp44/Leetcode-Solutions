**Valid Parentheses**

---

**Problem**  
Given a string containing `()`, `{}`, `[]`, determine if the input string is valid (open brackets closed in the correct order).

**Core Technique**  
**Stack + HashMap** for matching pairs.

**Algorithm Steps**  
1. Create a map: closing bracket → corresponding opening bracket (`')' → '('`, etc.).  
2. Iterate through each character `c` in the string:  
   - **If `c` is not in the map** (i.e., it's an opening bracket): push it onto the stack.  
   - **Else** (it's a closing bracket):  
     - If the stack is empty → return `False` (no matching opener).  
     - Pop the top element from the stack. If it doesn't match the expected opening bracket (`map[c] != top`), return `False`.  
3. After the loop, the stack must be empty (all openers matched) → return `True`, else `False`.

**Complexity**  
- **Time:** O(n) – single pass.  
- **Space:** O(n) – worst case stack size (all opening brackets).

**Key Intuition**  
- The most recent unmatched opening bracket must be closed first (LIFO → stack).  
- The hash map provides O(1) lookup for the corresponding opening bracket.

**Common Mistakes**  
- Forgetting to check if the stack is empty before popping.  
- Returning `True` before verifying the stack is empty after the loop.  
- Using multiple if‑else for bracket types instead of a map (not wrong, but verbose).

**Memory Hook**  
> *“Open → push. Close → pop and match. Stack must be empty at end.”*
