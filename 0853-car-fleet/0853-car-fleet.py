class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        if n == 0:
            return 0

        # Pair each position with the time required to reach the target
        cars = [(pos, (target - pos) / spd) for pos, spd in zip(position, speed)]

        # Sort by position descending: closest to target first
        cars.sort(key=lambda x: x[0], reverse=True)

        fleets = 0
        last_time = 0.0  # time of the previous fleet (initially 0, so any positive time will be >0)

        for pos, time in cars:
            # If this car takes longer to reach target, it forms a new fleet
            # (it cannot catch up to the fleet ahead, which is already faster)
            if time > last_time:
                fleets += 1
                last_time = time

        return fleets

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna