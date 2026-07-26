**Evaluate Reverse Polish Notation** (stack‑based postfix evaluation)

---

**Problem**  
Evaluate an arithmetic expression given in Reverse Polish Notation (postfix).  
Operators: `+`, `-`, `*`, `/`. Division truncates toward zero.

**Core Technique**  
**Stack** – push numbers onto the stack; when an operator is encountered, pop the top two numbers, apply the operator, and push the result back.

**Algorithm Steps**  
1. Initialize an empty stack.  
2. For each token in the input:  
   - **If token is an operator** (`+`, `-`, `*`, `/`):  
     - `b = stack.pop()` (second operand – rightmost).  
     - `a = stack.pop()` (first operand – leftmost).  
     - `result = applyOperator(token, a, b)`.  
     - `stack.append(result)`.  
   - **Else** (it’s a number): push `int(token)` onto the stack.  
3. After processing all tokens, the final result is the only element left in the stack. Return `stack.pop()`.

**Operator Logic**  
- `+`: `a + b`  
- `-`: `a - b`  
- `*`: `a * b`  
- `/`: `int(a / b)` — **must** truncate toward zero (Java‑style).  
  - Python’s `a // b` does floor division, which rounds down for negatives.  
  - `int(a / b)` performs floating‑point division then chops decimal toward zero → correct.

**Complexity**  
- **Time:** O(n) – one pass through the tokens.  
- **Space:** O(n) – stack can hold up to n/2 operands.

**Common Mistakes**  
- Using `a // b` for division instead of `int(a / b)` – breaks for negative results.  
- Popping operands in the wrong order: remember `b` (right operand) is popped first, then `a` (left operand).  
- Forgetting to convert string tokens to `int` before pushing.  
- Not handling division by zero (problem guarantees no division by zero, but in practice you might want a guard).

**Key Intuition**  
> *“Postfix: operators come after their operands. Stack holds intermediate results. When you see an operator, apply it to the last two numbers pushed.”*

**Memory Hook**  
> *“Number → push. Operator → pop two (b, then a), apply, push result. Left at the bottom, right at the top. Truncate division with `int(a/b)`.”*
