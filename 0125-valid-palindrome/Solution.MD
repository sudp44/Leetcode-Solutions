**Valid Palindrome**:

---

**Problem**  
Check if a string is a palindrome considering only alphanumeric characters and ignoring case.

**Core Technique**  
Two pointers (`left`, `right`) skipping non‑alphanumeric, compare case‑insensitively.

**Algorithm Steps**  
1. `left = 0`, `right = len(s) - 1`.  
2. **While** `left < right`:  
   - Inner `while left < right and not s[left].isalnum(): left += 1` – skip junk left.  
   - Inner `while left < right and not s[right].isalnum(): right -= 1` – skip junk right.  
   - **If** `s[left].lower() != s[right].lower()`: return `False`.  
   - `left += 1`, `right -= 1` – move inward.  
3. Return `True`.

**Complexity**  
- **Time:** O(n) – each character visited at most once.  
- **Space:** O(1) – only two pointers.

**Why inner `while` loops?**  
They skip all non‑alphanumeric characters in one go, ensuring `left` and `right` always point to alphanumeric before comparison. Without them, you’d need messy interleaved checks.

**Common Mistakes**  
- Forgetting `left < right` guard inside the inner `while` loops → index out of bounds.  
- Using `while left <= right` instead of `<` (redundant middle‑char check, not wrong but unnecessary).  
- Not converting case with `.lower()` → false mismatch on `'A'` vs `'a'`.  
- Comparing without first skipping non‑alphanumeric → `"a."` treated as not equal.

**Memory Hook**  
> *“Skip junk left, skip junk right, compare lowered – move inward.”*
