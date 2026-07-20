# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Min-heap to collect all node values
        min_heap = PriorityQueue()
        
        # Put all values into the priority queue
        for lst in lists:
            while lst:
                min_heap.put(lst.val)
                lst = lst.next
        
        # Dummy node to simplify building the result list
        dummy = ListNode(1)      # any value works
        merge = dummy
        
        # Extract values in increasing order and build the merged list
        while not min_heap.empty():
            val = min_heap.get()
            merge.next = ListNode(val)
            merge = merge.next
        
        return dummy.next


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna