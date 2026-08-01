**Stack using two Queues**

---

**Problem**  
Implement a **stack** (LIFO) using only two queues.  
The solution should support `push`, `pop`, `top`, and `empty`.

**Core Technique**  
Make either `pop` (or `top`) **expensive** by rotating all but the last element to the second queue. The last element is the most recently pushed → stack’s top.

**Why two queues?**  
A single queue is inherently FIFO. To get LIFO, we need to repeatedly dequeue from the front and enqueue to the back until only the newest element remains. We use the second queue as a temporary holding area.

---

**Algorithm (pop‑expensive approach)**

1. **`push(x)`** – simply enqueue `x` to `q1` (O(1)).
2. **`pop()`** – O(n)  
   - While `len(q1) > 1`: dequeue from `q1` and enqueue to `q2`.  
   - Dequeue the **last remaining element** from `q1` (this is the stack’s top).  
   - Swap `q1` and `q2` so that `q1` again holds all remaining elements.
3. **`top()`** – same as `pop`, but instead of removing the last element, we peek it and then also move it to `q2` before swapping.
4. **`empty()`** – return `True` if both queues are empty.

**Complexity**  
- `push`: O(1)  
- `pop` / `top`: O(n) worst case (all elements moved once)  
- `empty`: O(1)  
- Space: O(n)

**Alternative (push‑expensive)**  
You could also make `push` O(n) by always inserting the new element at the front of the queue (using the second queue). Then `pop`/`top` become O(1). Either variation is acceptable.

---

**Common Mistakes**  
- Using the two‑stack pattern (FIFO) when you need a stack – that gives a queue.  
- Forgetting to swap the queues after moving elements – leads to lost elements and wrong order.  
- Not moving the last element in `top` – just peeking would break the order if you later call `pop`. You must move it to `q2` as well.

**Memory Hook**  
> *“For pop/top, drain all but the last from q1 to q2. The last one is the newest – the top. Then swap the queue names.”*
