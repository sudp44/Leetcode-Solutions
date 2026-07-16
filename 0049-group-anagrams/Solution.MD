**Problem**  
Group strings that are anagrams (same letters, same counts).

---

**Core Idea**  
Anagrams share an identical **character‑frequency profile**. Turn each word into a frequency key (26‑element tuple or delimited string). Use a hash map to group by key.

**Key Generation (two common ways)**  
1. **Tuple (faster)**  
   `count = [0]*26` → fill counts → `key = tuple(count)`  
2. **String**  
   `count = [0]*26` → fill counts → `cnt = [str(c) for c in count]` → `key = "#".join(cnt)`

**Steps**  
1. Create `hm = {}` (or `defaultdict(list)`).  
2. For each word:  
   - Build frequency array `count[26]` for `'a'..'z'`.  
   - Convert to key (tuple or string).  
   - `hm[key].append(word)`.  
3. Return `list(hm.values())`.

**Complexity**  
- **Time:** O(N·K) where N = number of words, K = max word length.  
- **Space:** O(N·K) for the grouped output.

**Common Mistakes**  
- Using variable‑length frequency array (`[0]*len(word)`) instead of fixed 26 → crashes or wrong keys.  
- Passing ints to `"#".join()` → `TypeError`. Convert to strings first.  
- Dictionary access backwards: `key[hm]` instead of `hm[key]`.  
- Shadowing built‑in `str` – use `s` or `word`.  
- Iterating dict without `.items()` / `.values()` → `ValueError`.

**When to prefer sorting**  
If the alphabet is large (e.g., Unicode), sorting the word (`sorted(word)`) as key is simpler but O(N·K log K). For lowercase letters only, the counting method is optimal.
