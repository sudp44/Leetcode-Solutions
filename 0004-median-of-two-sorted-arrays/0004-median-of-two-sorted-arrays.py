class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        x, y = len(nums1), len(nums2)
        start, end = 0, x
        
        while start <= end:
            partX = (start + end) // 2
            partY = (x + y + 1) // 2 - partX
            
            # Left and right elements for nums1 partition
            xLeft = nums1[partX - 1] if partX != 0 else float('-inf')
            xRight = nums1[partX] if partX != x else float('inf')
            
            # Left and right elements for nums2 partition
            yLeft = nums2[partY - 1] if partY != 0 else float('-inf')
            yRight = nums2[partY] if partY != y else float('inf')
            
            if xLeft <= yRight and yLeft <= xRight:
                # Found correct partition
                if (x + y) % 2 == 0:
                    return (max(xLeft, yLeft) + min(xRight, yRight)) / 2
                else:
                    return max(xLeft, yLeft)
            elif xLeft > yRight:
                end = partX - 1
            else:
                start = partX + 1
        
        return 0.0  # Should never be reached

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna