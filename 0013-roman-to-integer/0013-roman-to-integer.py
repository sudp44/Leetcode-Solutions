class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
        "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

        n = len(s)
        i = 0
        sum = 0

        while(i < n):
            if(i < n-1):
                two_symbols = s[i:i+2]
                if two_symbols in values.keys():
                    sum = sum + values[two_symbols]
                    i += 2
                    continue
            one_symbol = s[i:i+1]
            if one_symbol in values.keys():
                sum  = sum + values[one_symbol]
            i += 1
        
        return sum


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna