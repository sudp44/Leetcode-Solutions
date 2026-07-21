**Longest Substring Without Repeating Characters** (sliding window with set)

---

**Problem**  
Find the length of the longest contiguous substring with all unique characters.

**Technique**  
Dynamic sliding window (two pointers) with a hash set to track the current window's characters.

**Why Sliding Window?**  
- **Contiguous substring** required.  
- **Monotonic property**: adding a character can never make a window “more unique” — once a duplicate appears, you must shrink from the left.  
- Avoids O(n²) brute force.

**Algorithm Steps**  
1. `left = 0`, `right = 0`, `ans = 0`, empty set `seen`.  
2. While `right < len(s)`:  
   - Let `c = s[right]`.  
   - **If `c` already in `seen`**:  
     - Repeatedly remove `s[left]` from `seen`, `left += 1` until `c` is no longer in `seen`.  
   - Add `c` to `seen`.  
   - `ans = max(ans, right - left + 1)`.  
   - `right += 1`.  
3. Return `ans`.

**Key Invariant**  
`seen` always contains exactly the characters in the window `s[left … right-1]` (before adding the new character). After processing, the window `[left, right]` is always unique.

**Complexity**  
- **Time:** O(n) – each character added/removed at most once.  
- **Space:** O(min(n, alphabet size)) – the set holds at most all distinct characters.

**Common Mistakes**  
- Forgetting to increment `left` after removing from set (set and window go out of sync).  
- Using a `for` loop and trying to manually skip indices (doesn’t work).  
- Returning `ans` before updating it for the final window.  
- Not handling empty string (although the code checks it).

**When to Apply Sliding Window**  
Look for:  
- Contiguous subarray/substring.  
- A constraint that becomes **harder** to satisfy as the window grows (like “all unique”).  
- You need O(n) time, and brute force is O(n²) or worse.

**Memory Hook**  
> “Expand with `right`, if duplicate → shrink `left` until it’s gone. The window is always unique, track max length.”
