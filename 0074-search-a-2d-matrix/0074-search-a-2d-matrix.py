class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m*n - 1

        while(l <= r):
            mid = (l+r)//2
            mid_value = matrix[mid//n][mid%n]
            if mid_value == target:
                return True
            elif mid_value > target:
                r = mid-1
            else:
                l = mid+1
            
        
        return False
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna