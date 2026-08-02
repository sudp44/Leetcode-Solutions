from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Preprocess deadends into a set for O(1) lookup
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0

        # BFS initialization
        q = deque()
        q.append("0000")
        seen = set()
        seen.add("0000")
        steps = 0

        while q:
            # Process all nodes at the current distance
            for _ in range(len(q)):
                cur = q.popleft()
                # If we reached target, return steps (guaranteed minimum)
                if cur == target:
                    return steps
                # Skip dead states (they shouldn't be in queue if we check before pushing,
                # but just in case a dead state slipped through)
                if cur in dead:
                    continue

                # Generate neighbors: turn each of the 4 wheels up/down
                cur_chars = list(cur)  # mutable list of characters
                for i in range(4):
                    orig = cur_chars[i]
                    d = int(orig)

                    # Turn up: (d+1) % 10
                    cur_chars[i] = str((d + 1) % 10)
                    up = "".join(cur_chars)
                    if up not in dead and up not in seen:
                        seen.add(up)
                        q.append(up)

                    # Turn down: (d+9) % 10 (equivalent to (d-1+10) % 10)
                    cur_chars[i] = str((d + 9) % 10)
                    down = "".join(cur_chars)
                    if down not in dead and down not in seen:
                        seen.add(down)
                        q.append(down)

                    # Restore original digit for next iteration
                    cur_chars[i] = orig

            steps += 1

        # Target not reachable
        return -1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna