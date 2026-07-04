from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        as_strs = [str(num) for num in nums]

        def compare(a: str, b:str) -> int:
            order1 = a + b
            order2 = b + a

            if order1 > order2:
                return -1
            elif order2 > order1:
                return 1
            else:
                return 0
            
        as_strs.sort(key = cmp_to_key(compare))

        if as_strs[0] == "0":
            return "0"

        return "".join(as_strs)       

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna