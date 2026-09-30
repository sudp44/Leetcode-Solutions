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
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna