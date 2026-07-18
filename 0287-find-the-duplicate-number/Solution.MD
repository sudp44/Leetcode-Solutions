**Find the Duplicate Number** (Floyd’s Tortoise & Hare):

---

**Problem**
Array of `n+1` integers in `[1, n]`, exactly one duplicate. Find the duplicate without modifying the array and using O(1) extra space.

**Core Idea**
Treat the array as a **linked list** where `i → nums[i]`. Since values are valid indices, a cycle forms. The **cycle entrance** is the duplicate number. Use Floyd’s cycle detection.

**Steps**
1. **Phase 1 – Find meeting point**  
   ```python
   slow = nums[0]           # move 1 step
   fast = nums[nums[0]]     # move 2 steps
   while slow != fast:
       slow = nums[slow]
       fast = nums[nums[fast]]
   ```
2. **Phase 2 – Find cycle entrance (duplicate)**  
   ```python
   slow = 0                 # reset to head
   while slow != fast:
       slow = nums[slow]    # both move 1 step
       fast = nums[fast]
   return slow              # or fast
   ```

**Why It Works**
- Because values are in `[1,n]`, each index points to a valid index → implicit linked list.
- Duplicate means at least two indices point to the same value → that node is the cycle entrance.
- Phase 1: `slow` and `fast` meet inside the cycle.
- Phase 2: Distance from head to entrance equals distance from meeting point to entrance (mod cycle length), so resetting `slow` to 0 and moving both one step makes them meet at the entrance.

**Alternative Initialization**
- You can start both at `0` (head) but need to move before checking equality (or use a `do-while` style). The above starts one step ahead to avoid an initial false equality.

**Complexity**
- **Time:** O(n) – each pointer traverses at most O(n) steps.
- **Space:** O(1) – only two pointers.

**Key Intuition**
- **Why not sort or use hash set?** Space O(n) or modification not allowed.
- **Why does this always work?** The duplicate creates a node with indegree ≥ 2 → that’s exactly the start of the cycle.
- **What if the duplicate appears more than twice?** Still works – just a cycle with a “rho” shape.

**Edge Cases / Common Mistakes**
- Array with duplicate at index 0 (e.g., `[1,1,…]`): Phase 1 loop may not run if `slow` and `fast` already equal; Phase 2 still correctly returns 1.
- Using `while slow != fast` for both phases (Phase 2 needs the reset).
- Starting `slow` and `fast` both at `0` without moving first → infinite loop or immediate false equality.

**Memory Hook**
> “Linked list in array, duplicate = cycle start. Two phases: meet first, then reset slow to head and walk together.”
