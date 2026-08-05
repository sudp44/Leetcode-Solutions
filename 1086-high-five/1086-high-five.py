import heapq
from collections import defaultdict
from typing import List

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # Map each student ID to a max‑heap (stored as negative scores)
        scores = defaultdict(list)   # list will be used as a heap
        
        for id_, score in items:
            # Python has only min‑heap, so push negative score to simulate max‑heap
            heapq.heappush(scores[id_], -score)
        
        result = []
        # TreeMap in Java → sorted keys in Python
        for id_ in sorted(scores.keys()):
            total = 0
            # Poll the top 5 scores (largest)
            for _ in range(5):
                # Pop the smallest negative → largest original score
                total += -heapq.heappop(scores[id_])
            result.append([id_, total // 5])
        
        return result