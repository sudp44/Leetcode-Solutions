class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.findBound(nums, target, True)

        if (first == -1):
            return [-1, -1]
        
        last = self.findBound(nums, target, False)

        return [first, last]
    
    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:
        start, end = 0, len(nums)-1

        while(start <= end):
            mid = (start+end) // 2

            if (nums[mid] == target):
                if isFirst:
                    if(mid == 0 or nums[mid] != nums[mid-1]):
                        return  mid
                    else:
                        end = mid-1
                else:
                    if(mid == len(nums)-1 or nums[mid] != nums[mid+1]):
                        return  mid
                    else:
                        start = mid+1
            elif  (nums[mid] > target):
                end = mid-1
            else:
                start = mid+1

        return -1
            
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna