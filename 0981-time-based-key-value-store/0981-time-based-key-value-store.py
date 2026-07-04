from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        # Maps key -> list of (timestamp, value) tuples
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Since timestamps always increase, appending keeps the list sorted
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # If the key doesn't exist, return empty string
        if key not in self.map:
            return ""
        
        values_list = self.map[key]
        
        # Use binary search to find the insertion point for the timestamp
        # bisect_right finds the first index where the stored timestamp > target timestamp
        idx = bisect.bisect_right(values_list, (timestamp, chr(127)))
        
        # If idx is 0, it means all stored timestamps are greater than the requested timestamp
        if idx == 0:
            return ""
            
        # The largest timestamp <= target will be at index (idx - 1)
        return values_list[idx - 1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna