**Pow(x, n)**

---

## Problem
Implement `pow(x, n)`, which calculates `x` raised to the power `n` (i.e., `x^n`).

**Constraints:**
- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31 - 1`
- `n` is an integer.
- Either `x` is not zero or `n > 0`.

**Example:** `x = 2.0, n = 10` → `1024.0`

## Core Technique
**Binary exponentiation (exponentiation by squaring)**.  
Compute `x^n` in O(log n) time by repeatedly squaring the base and halving the exponent, using the binary representation of `n`.

## Algorithm Steps
1. Handle base case: if `n == 0`, return `1.0`.
2. If `n < 0`, invert `x` (`x = 1/x`) and make `n` positive (`n = -n`).  
   (Python integers are unbounded, so no overflow worry – no need for `long`.)
3. Initialize `result = 1.0`, `current_product = x`.
4. While `n > 0`:
   - If `n % 2 == 1`: `result *= current_product`
   - `current_product *= current_product`
   - `n //= 2`
5. Return `result`.

## Python Code (iterative, canonical)
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1 / x
            n = -n
        result = 1.0
        current_product = x
        while n > 0:
            if n % 2 == 1:
                result *= current_product
            current_product *= current_product
            n //= 2
        return result
```

## Why It Works (Binary Representation Insight)
- Any integer `n` is a sum of powers of 2. For example, `13 = 8 + 4 + 1`.
- Therefore `x^13 = x^8 · x^4 · x^1`.
- The loop extracts the bits of `n` from LSB to MSB using `n % 2` (read bit) and `n //= 2` (right shift to get next bit).
- `current_product` holds `x^(2^k)` at step `k`; it's squared each iteration to become the next power.
- `result` accumulates the product of `current_product` for every bit that is `1`.
- At the end, `result` is exactly `x^n`.

**Clarification on "right shift":** `n //= 2` removes the rightmost bit and shifts the remaining bits to the right. The loop reads bits from right to left (LSB → MSB), so the loop direction is leftwards across the bit positions while the bits themselves shift right. Both are correct.

## Complexity
- **Time:** O(log n) – the exponent is halved each iteration.
- **Space:** O(1) – only a few variables.

## Common Mistakes
- Forgetting to handle negative exponents (invert and negate).
- Using `/` instead of `//` for integer division of `n`.
- Trying to use `long` equivalent in Python (unnecessary).
- Not initializing `result = 1.0` (not `0`).
- Confusing `current_product` with the final answer – it's only a factor.
- Forgetting to square `current_product` even when the bit is 0.

## Memory Hook
> *"Binary exponentiation: square the base, halve the exponent. If bit is 1, multiply into result."*

Or shorter:
> *"x^n via bits of n: square, multiply when bit is 1."*

## Alternative (Recursive)
```python
def myPow(self, x: float, n: int) -> float:
    if n == 0:
        return 1.0
    if n < 0:
        return 1 / self.myPow(x, -n)
    half = self.myPow(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x
```
This uses O(log n) space due to recursion. The iterative version is preferred for O(1) space.
