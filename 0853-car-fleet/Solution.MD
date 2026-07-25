**Car Fleet** (monotonic sorting + time comparison)

---

**Problem**  
Cars start at different positions with different speeds heading toward the same target. They become a fleet if a faster car catches up to a slower one. Count the number of fleets that arrive at the target.

**Core Technique**  
Convert each car to a **(position, time_to_target)** pair, sort by position descending (closest to target first), then count how many cars have a **strictly greater time** than the last fleet’s time. Those start new fleets.

**Data Structures**  
- `cars` = list of `(position, time)` tuples (or lists).  
- `zip(position, speed)` pairs the lists element‑wise.

**Algorithm Steps**  
1. If no cars, return 0.  
2. Build `cars = [(pos, (target - pos) / spd) for pos, spd in zip(position, speed)]`.  
3. Sort `cars` by position descending (`key=lambda x: x[0], reverse=True`).  
4. `fleets = 0`, `last_time = 0.0`.  
5. For each `(pos, time)` in `cars`:  
   - If `time > last_time` → new fleet: `fleets += 1`, `last_time = time`.  
   - Else → merges into existing fleet (ignore).  
6. Return `fleets`.

**Why it works**  
- Closest cars are processed first. They form the first fleet (or set a fast time).  
- A car farther back can only merge if its time is ≤ the fleet ahead (i.e., it can catch up).  
- If its time is greater, it’s too slow → forms a new fleet behind.

**Complexity**  
- **Time:** O(n log n) – dominated by sorting.  
- **Space:** O(n) – for the `cars` list.

**Common Mistakes**  
- Sorting by position ascending instead of descending (must start from target side).  
- Using `>=` instead of `>` for fleet condition – equal times should merge, not create a new fleet.  
- Forgetting to handle empty input.

**Memory Hook**  
> *“Line them up closest to target. If the next car takes longer, it starts a new fleet; if it’s faster, it joins the one ahead.”*
