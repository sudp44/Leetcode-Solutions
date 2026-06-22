class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min = prices[0]
        profit = 0

        for i in range(n):
            if (prices[i] < min):
                min = prices[i]
            
            if (prices[i]-min) > profit:
                profit = prices[i]-min
                
        return profit
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna