**Permutation in String** (fixed‑size sliding window with frequency arrays)

---

**Problem**  
Check if any permutation of `s1` is a contiguous substring of `s2`.

**Core Idea**  
Two strings are permutations ⇔ they have identical character frequencies.  
Use a **window of length `len(s1)`** sliding across `s2`. Maintain two frequency arrays (size 26 for `'a'..'z'`). Compare them at each step.

**Steps**  
1. If `len(s1) > len(s2)`: return `False`.  
2. Build `s1Map` (target frequencies) and `s2Map` (first window of `s2` of same length).  
3. Loop `i` from `0` to `len(s2) - len(s1) - 1` (all windows except the last):  
   - If `s1Map == s2Map` → return `True`.  
   - Slide window:  
     - Add `s2[i + len(s1)]` to `s2Map`.  
     - Remove `s2[i]` from `s2Map`.  
4. After the loop, check the final window: `return s1Map == s2Map`.

**Complexity**  
- **Time:** O(len(s2)) – sliding window is linear, array comparisons are O(26) = O(1).  
- **Space:** O(1) – two arrays of fixed size 26.

**Key Details**  
- Mapping: `ord(char) - ord('a')` converts `'a'..'z'` to indices `0..25`.  
- The loop runs `len(s2)-len(s1)` times, then we manually compare the last window.  
- `s1Map == s2Map` does element‑wise list comparison (Python).

**Common Mistakes**  
- Not checking the last window after the loop.  
- Off‑by‑one in the slide (adding/removing wrong indices).  
- Forgetting early exit when `s1` is longer than `s2`.

**Memory Hook**  
> “Fixed window equals `s1` length. Slide right: add new char, drop left char. Compare arrays at each stop.”
