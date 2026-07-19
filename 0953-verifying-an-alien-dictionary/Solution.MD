**Verifying an Alien Dictionary**:

---

**Problem**  
Given a list of words and an alien alphabet order, check if the words are sorted lexicographically according to that order.

**Core Idea**  
1. Map each alien character to its index (rank) → `order_map`.  
2. Compare every adjacent pair of words. If any pair is out of order, return `False`.  
3. To compare two words:  
   - Loop over the characters of the **first** word.  
   - If the first word is longer and the second word ends first → `return False` (prefix rule).  
   - At the first differing character, check ranks: if `rank(c1) > rank(c2)` → `return False`; otherwise `break` (this pair is okay).  
   - If loop finishes without finding a difference, the pair is sorted.

**Key Conditions**  
- **Prefix check:** `if j >= len(word2): return False` (word2 finished, but word1 still has characters → word1 > word2, not sorted).  
- **First difference check:** `if order_map[word1[j]] > order_map[word2[j]]: return False` else `break`.  
- Only compare **adjacent** words; sorting is transitive if each adjacent pair is sorted.

**Complexity**  
- **Time:** O(C) where C = total characters in all words (each character visited at most once during comparisons).  
- **Space:** O(1) extra (the order map has fixed 26 entries).

**Common Mistakes**  
- Forgetting to `break` after finding a valid differing character → might continue and fail on later characters.  
- Missing the prefix case (longer word after shorter prefix is invalid).  
- Starting inner loop with `range(len(word1))` but not checking `j >= len(word2)` before accessing `word2[j]`.

**Memory Hook**  
> “Map order ranks, compare adjacent pairs, stop at first difference – shorter must come first, else check ranks.”
