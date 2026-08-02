**Open the Lock** (BFS on a graph of lock states)

---

**Problem**  
You have a 4‑digit circular lock (each wheel 0‑9). Given a list of deadend codes and a target, find the minimum number of turns to reach the target from `"0000"`, or `-1` if impossible. You cannot turn a wheel to a deadend.

**Core Technique**  
**BFS** on the implicit graph of all 10,000 possible lock combinations. Each state is a string of 4 digits; edges exist by turning one wheel up or down (digit ±1 modulo 10), avoiding deadends.

**Why BFS?**  
The lock dials are a graph with unweighted edges. BFS finds the shortest path (minimum turns) from start to target in O(V+E) time.

**Data Structures**  
- `dead` = `set(deadends)` – O(1) lookup for forbidden states.  
- `q` = `deque(["0000"])` – for BFS (FIFO). Use `popleft()` to remove front, `append()` to add back.  
- `seen` = `set(["0000"])` – avoids revisiting states and infinite loops.

**Algorithm Steps**  
1. If `"0000"` is in `dead` → return `-1`. If `target == "0000"` → return `0`.  
2. BFS loop:  
   - Track `steps` (turns).  
   - For each state in current level:  
     - If `cur == target` → return `steps`.  
     - If `cur` in `dead` → `continue`.  
     - Generate up to 8 neighbors: for each wheel `i` in 0..3:  
       - `up = (digit+1) % 10` → new string. If not dead and not seen, add to queue and seen.  
       - `down = (digit+9) % 10` (same as -1 mod 10). Same check.  
     - Restore original digit after each wheel.  
   - Increment `steps`.  
3. Queue empties → return `-1` (unreachable).

**Generating neighbors**  
```python
cur_chars = list(cur)
for i in range(4):
    orig = cur_chars[i]
    d = int(orig)
    cur_chars[i] = str((d + 1) % 10)   # up
    up = "".join(cur_chars)
    # check & push up if valid
    cur_chars[i] = str((d + 9) % 10)   # down
    down = "".join(cur_chars)
    # check & push down if valid
    cur_chars[i] = orig                # restore
```

**Complexity**  
- **Time:** O(10,000) – each state visited at most once, each produces up to 8 neighbors.  
- **Space:** O(10,000) for `seen` and `q` (worst case all states).

**Common Mistakes**  
- Not using `seen` – leads to infinite loops or exponential explosion.  
- Using a list instead of `deque` with `pop(0)` – O(n²) total.  
- Forgetting to check deadends after generating neighbors (must filter before enqueue).  
- Modulo for down: `(d - 1 + 10) % 10` or equivalently `(d + 9) % 10`.

**Memory Hook**  
> *“BFS on lock states, each turn changes one digit ±1 (mod 10). Keep `seen` and `dead` sets. Shortest path = number of levels in BFS.”*
