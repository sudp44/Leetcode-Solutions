class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. Count frequencies
        freq = Counter(tasks)

        # 2. Build a max‑heap using negative frequencies (Python has min‑heap)
        max_heap = [-f for f in freq.values()]
        heapq.heapify(max_heap)

        time = 0

        # 3. Process cycles of size n+1
        while max_heap:
            temp = []
            # Take up to n+1 tasks (the cooling interval + the executed one)
            for _ in range(n + 1):
                if max_heap:
                    # Pop the task with the highest remaining frequency
                    temp.append(-heapq.heappop(max_heap))
                else:
                    break

            # Decrease frequencies, keep those > 0 back in the heap
            for f in temp:
                f -= 1
                if f > 0:
                    heapq.heappush(max_heap, -f)

            # If heap still has tasks, we must wait the full n+1 units (idle slots)
            # Otherwise it's the last batch, only add the number of tasks just executed
            time += (n + 1) if max_heap else len(temp)

        return time
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna