**Generate Parentheses** (backtracking)

---

**Problem**  
Given `n` pairs of parentheses, generate all valid combinations. A combination is valid if parentheses close in the correct order.

**Core Technique**  
**Backtracking** – build the string character by character, respecting two rules:  
- You may add `'('` if `open < n`.  
- You may add `')'` if `close < open`.

**Algorithm Steps**  
1. Create an empty result list `ans` and an empty builder (list of characters).  
2. Define a helper `backtrack(cur, open, close)`:  
   - **Base case:** if `len(cur) == 2n` → add `"".join(cur)` to `ans`, return.  
   - **If `open < n`:**  
     - `cur.append("(")`  
     - `backtrack(open+1, close)`  
     - `cur.pop()` (undo the choice)  
   - **If `close < open`:**  
     - `cur.append(")")`  
     - `backtrack(open, close+1)`  
     - `cur.pop()` (undo the choice)  
3. Start with `backtrack([], 0, 0)` and return `ans`.

**Why it works**  
- The `open < n` rule ensures we never use more than `n` left parentheses.  
- The `close < open` rule ensures we never close a parenthesis that wasn’t opened, which guarantees validity.  
- The recursion explores every sequence of `(` and `)` that follows these rules, which are exactly all valid combinations.  
- The `pop()` after recursion restores the builder to its previous state, allowing the next branch to start cleanly (backtracking).

**Complexity**  
- **Time:** O( (4ⁿ) / √n ) – the number of valid combinations is the Catalan number Cₙ. Each combination takes O(n) to build, so total work is O(n·Cₙ) ≈ O(4ⁿ / √n).  
- **Space:** O(n) – recursion depth up to 2n, plus the mutable builder of size up to 2n. The output list is not counted in auxiliary space.

**Common Mistakes**  
- Forgetting to `pop()` after the recursive call – leads to leftover characters and wrong combinations.  
- Swapping the order of `open < n` and `close < open` checks (both are independent `if`s, not `elif`s).  
- Using an immutable string and creating many intermediate objects (fine but slower).  
- Not converting the list of characters back to a string before adding to the result.

**Memory Hook**  
> *“Open if you can, close if you should. Append, recurse, pop – that’s the backtracking rhythm.”*
