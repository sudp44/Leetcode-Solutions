class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for i in range(1, n+1):
            current_str = ""
            if (i%3 == 0):
                current_str += "Fizz"
            if (i%5 == 0):
                current_str += "Buzz"
            
            if not current_str:
                current_str = str(i)

            result.append(current_str)

        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna