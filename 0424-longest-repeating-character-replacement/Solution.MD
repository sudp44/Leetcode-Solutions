**Longest Repeating Character Replacement** (sliding window with “lazy” max frequency)

---

**Problem**  
Given a string `s` and integer `k`, find the length of the longest substring that can be formed by replacing at most `k` characters to make all characters the same.

**Core Idea**  
For any window, the optimal strategy is to keep the most frequent character and replace the rest.  
A window is **valid** if:  
`window_length – max_freq_in_window ≤ k`.  
Use a sliding window that **never shrinks `maxOccurance`** even when the most frequent character leaves the window. This gives O(n) time.

**Algorithm Steps**  
1. `left = 0`, `occurrence[26]` all zeros, `maxOccurance = 0`, `ans = 0`.  
2. **For** `right` from `0` to `n-1`:  
   - Add `s[right]` to frequency array; update `maxOccurance = max(maxOccurance, freq[s[right]])`.  
   - **If** `(right - left + 1) - maxOccurance > k`:  
     - Remove `s[left]` from freq, `left += 1`.  
   - `ans = max(ans, right - left + 1)`.  
3. Return `ans`.

**Why not decreasing `maxOccurance` works (the “trick”)**  
- `maxOccurance` can become **overestimated** (larger than actual max in the current window).  
- This means `window_length – maxOccurance` is **smaller** than the true replacement count, so we sometimes **don’t shrink when we should** — the window may stay invalid.  
- However, `maxOccurance` acts as a **cap**: the window length is limited to `maxOccurance + k`.  
- The only time `maxOccurance` increases is when we actually have that many copies of a character in the window, making that length valid.  
- Therefore, the global maximum window length that updates `ans` corresponds to a genuine valid window that existed when `maxOccurance` was last increased.  
- The answer is never overestimated, despite the “lazy” max.

**Complexity**  
- **Time:** O(n) – each character added/removed at most once.  
- **Space:** O(1) – fixed array of 26.

**Common Mistakes**  
- Trying to recalculate the true maximum frequency inside the window every step (would be O(26n) or worse, but still linear if you scan 26; however the lazy approach is simpler and genuinely O(n) without the constant factor worry).  
- Confusing uppercase/lowercase – here it’s uppercase letters, use `ord(c)-ord('A')`.  
- Forgetting that window is allowed to stay invalid but its length never increases until a new `maxOccurance` is set.

**Memory Hook**  
> “Slide right, keep lazy max, cap window size at maxOccurance + k. Shrink when (len – maxOcc) > k. Answer is max window ever seen.”
