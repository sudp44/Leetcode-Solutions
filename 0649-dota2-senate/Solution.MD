**Dota2 Senate**

---

**Problem**  
Two parties, Radiant and Dire, take turns banning the next opposing senator. Order of actions follows the original string order, with multiple rounds until one party remains. Predict the winner.

**Core Technique**  
Two queues storing the **indices** of Radiant and Dire senators. Simulate rounds by comparing the front of each queue: the smaller index acts first, bans the opponent, and itself re‑queues with `index + n` (to act in the next round). The party that empties first loses.

**Algorithm Steps**  
1. Create two deques: `radiant`, `dire`.  
2. Populate with indices of each senator from the original string.  
3. While both queues are non‑empty:  
   - Pop `r_idx` and `d_idx`.  
   - If `r_idx < d_idx` → Radiant acts first: re‑queue `r_idx + n` (Radiant survives).  
   - Else → Dire acts first: re‑queue `d_idx + n` (Dire survives).  
4. Return `"Radiant"` if `dire` is empty, else `"Dire"`.

**Why `+ n`?**  
All original indices are in `[0, n-1]`. Adding `n` pushes the surviving senator into the next round, making its index larger than any remaining original index. This ensures it acts **after** all current senators, preserving round order.

**Complexity**  
- **Time:** O(n) – each senator pushed/popped at most once.  
- **Space:** O(n) for the two queues.

**Edge Cases / Clarifications**  
- `r_idx` and `d_idx` are never equal because indices are unique to each party.  
- The first senator to act is the one with the smallest index among the remaining senators, which is always at the front of one of the queues.  
- No need for a separate round counter; the `+n` offset naturally creates round cycles.

**Memory Hook**  
> *“Two queues of indices, compare fronts. Smaller index bans the other, then requeues itself with `+n` to wait its next turn.”*
