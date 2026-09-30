**Multiply Strings**

---

## Python Code (Runnable)

```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        # Multiply from right to left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                mul = digit1 * digit2

                pos_low = i + j + 1
                pos_high = i + j

                total = mul + result[pos_low]
                result[pos_low] = total % 10
                result[pos_high] += total // 10

        # Convert to string, skipping leading zeros
        res_str = ''.join(str(d) for d in result).lstrip('0')
        return res_str if res_str else "0"


# ------------------ Test ------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.multiply("2", "3"))          # "6"
    print(sol.multiply("123", "456"))      # "56088"
    print(sol.multiply("0", "123"))        # "0"
    print(sol.multiply("999", "999"))      # "998001"
```

**How to run:** Copy the entire block into any Python 3 online compiler and click Run.

---

## Explanation

### Problem
Given two non‑negative integers `num1` and `num2` represented as strings, return the product as a string. You must not use any built‑in big‑integer library or convert the inputs to integers directly.

### Approach
We simulate the standard grade‑school multiplication algorithm.

1. **Edge case:** If either number is `"0"`, the product is `"0"`.
2. **Result array:** The product of an `m`‑digit number and an `n`‑digit number can have at most `m + n` digits. We create an array `result` of size `m + n` filled with zeros.
3. **Nested loops:** Iterate `i` from the end of `num1` to the start, and `j` from the end of `num2` to the start.
   - Compute the product of the current digits: `mul = digit1 * digit2`.
   - The result of this product contributes to positions `i + j` and `i + j + 1` in the result array.
   - Add `mul` to the current value at `pos_low = i + j + 1`.
   - Set `result[pos_low]` to `total % 10` and carry `total // 10` to `pos_high = i + j`.
4. **Build the string:** After all multiplications, convert the result array to a string. Skip leading zeros. If the result is all zeros (already handled), return `"0"`.

### Why positions `i + j` and `i + j + 1`?
Think of the multiplication as aligning the digits. The rightmost digit of `num1` is at index `m-1`, and the rightmost of `num2` at `n-1`. Their product goes to the least significant position of the result, which is index `m + n - 1`. In general, the product of `num1[i]` and `num2[j]` lands at position `i + j` (carry) and `i + j + 1` (current digit). This is a standard trick for string multiplication.

### Complexity
- **Time:** O(m × n) – two nested loops, each digit of one number multiplied with each digit of the other.
- **Space:** O(m + n) – the result array.

---

## Quick Recall Notes

**Problem:** Multiply two non‑negative integers given as strings, without using built‑in big integer conversion.

**Core Technique:** Grade‑school multiplication simulated with an array.

**Algorithm Steps:**
1. If either string is `"0"`, return `"0"`.
2. Create `result` array of size `len(num1) + len(num2)`, initialized to 0.
3. For `i` from `len(num1)-1` down to 0:
   - For `j` from `len(num2)-1` down to 0:
     - `mul = int(num1[i]) * int(num2[j])`
     - `pos_low = i + j + 1`
     - `pos_high = i + j`
     - `total = mul + result[pos_low]`
     - `result[pos_low] = total % 10`
     - `result[pos_high] += total // 10`
4. Convert `result` to string, skipping leading zeros.

**Key Insight:** The product of digits at indices `i` and `j` contributes to positions `i+j` (carry) and `i+j+1` (current digit) in the result array.

**Complexity:** O(m×n) time, O(m+n) space.

**Common Mistakes:**
- Forgetting to handle `"0"` inputs.
- Not skipping leading zeros in the final string.
- Incorrect position calculation (`i+j` vs `i+j+1`).
- Forgetting to add carry to `pos_high` (must use `+=`, not `=`).
- Using integer conversion of the whole string (not allowed).

**Memory Hook:**
> *"Multiply digit by digit, store in array at positions i+j and i+j+1. Carry to the left. Skip leading zeros."*

Or: *"Grade‑school multiplication with an array of size m+n."*

**Edge Cases:**
- One or both numbers zero.
- Numbers with leading zeros? (Problem guarantees no leading zeros except "0" itself.)
- Very large numbers (up to 200 digits) — array approach handles it.
