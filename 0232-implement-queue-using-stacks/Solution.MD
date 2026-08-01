**Queue using two Stacks** (FIFO from LIFO)

---

**Problem**  
Implement a **queue** (FIFO) using only two stacks.  
Methods: `push`, `pop`, `peek`, `empty`.

**Core Technique**  
Use two stacks:  
- `in_stack` receives new elements (enqueue).  
- `out_stack` holds elements in reversed order (dequeue).  
When `out_stack` is empty, flip all elements from `in_stack` onto `out_stack` – this reverses their order so the oldest becomes the top. Each element is moved at most once.

**Algorithm Steps**  
1. **`push(x)`** – push `x` onto `in_stack`. O(1)  
2. **`pop()`** – call `_move_if_needed()`, then `return out_stack.pop()`.  
3. **`peek()`** – call `_move_if_needed()`, then `return out_stack[-1]`.  
4. **`empty()`** – return `not in_stack and not out_stack`.  
5. **`_move_if_needed()`** – if `out_stack` is empty:  
   `while in_stack: out_stack.append(in_stack.pop())`

**Why it works (Amortized O(1))**  
- Each element is pushed once, moved once, and popped once.  
- The cost of moving N elements is spread over N operations → amortized O(1) per `pop`/`peek`.  
- The queue’s front is always on top of `out_stack` (if not empty), or will be after the next move.

**Complexity**  
- `push`: O(1)  
- `pop` / `peek`: Amortized O(1), worst case O(n) (occasional full transfer)  
- `empty`: O(1)  
- Space: O(n)

**Common Mistakes**  
- Forgetting to call `_move_if_needed` before `pop`/`peek`.  
- Leaving `in_stack` non‑empty when `out_stack` becomes empty again – the move only triggers when `out_stack` is empty, which is correct; new elements stay in `in_stack` until the next drain.  
- Using `pop()` on an empty stack – ensure `_move_if_needed` is called and still check emptiness if needed.  
- Confusing with the reverse problem (stack from two queues) – this one is a queue from two stacks.

**Memory Hook**  
> *“Push to `in`, pop from `out`. When `out` is dry, dump `in` upside‑down into `out`. Front lives at the top of `out`.”*
