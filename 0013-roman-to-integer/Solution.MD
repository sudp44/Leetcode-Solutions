**Roman to Integer**:

---

**Problem**  
Convert a Roman numeral string to an integer.  
Symbols: I, V, X, L, C, D, M (and subtractive pairs like IV, IX, etc.).

**Approach**  
- Pre‑define a map of **single** and **two‑character** values.  
- Scan the string **left to right** with a controlled index.  
- At each position, try to read **two characters**. If they form a valid subtractive pair (e.g., "IV", "IX"), add its value and **advance the index by 2**.  
- Otherwise, read **one character**, add its value, advance index by 1.  

**Crucial: Use a `while` loop, NOT a `for` loop**  
```python
i = 0
while i < len(s):
    if i < n-1 and s[i:i+2] in values:
        total += values[s[i:i+2]]
        i += 2
    else:
        total += values[s[i]]
        i += 1
```
- A `for i in range(...):` loop cannot skip iterations – manually changing `i` inside the loop is ignored because `range` produces the next value regardless.
- A `while` loop gives full control over the index, which is necessary because a two‑symbol numeral consumes two characters.

**Complexity**  
- **Time:** O(n) – one pass over the string.  
- **Space:** O(1) – only a fixed dictionary and variables.

**Common Mistake**  
Using a `for` loop and writing `i += 2` or `i += 1` to skip indices – this **does not work** in Python. The loop continues with the next number from `range` and causes double‑counting (e.g., "IV" gives 4 + 5 = 9 instead of 4).

**Memory Hook**  
> “Two‑symbol check, while loop – not for – because you need to move `i` by 1 or 2.”
