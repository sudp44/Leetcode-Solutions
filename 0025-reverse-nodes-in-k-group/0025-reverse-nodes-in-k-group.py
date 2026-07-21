# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper function to reverse exactly k nodes starting from `head`
        def reverseLinkedList(head, k):
            newHead = None
            ptr = head
            while k > 0:
                nextNode = ptr.next
                ptr.next = newHead
                newHead = ptr
                ptr = nextNode
                k -= 1
            return newHead

        ptr = head
        ktail = None          # Tail of the last processed group
        newHead = None        # Final head of the result list

        while ptr:
            count = 0
            # Move ptr forward to check if there are at least k nodes left
            ptr = head         # Reset ptr to the start of the current group
            while count < k and ptr:
                ptr = ptr.next
                count += 1

            if count == k:
                revHead = reverseLinkedList(head, k)  # Reverse the k nodes starting from head

                if newHead is None:       # First reversed group
                    newHead = revHead
                if ktail:                 # Connect previous group to the new reversed head
                    ktail.next = revHead

                ktail = head              # After reversal, `head` becomes the tail of this group
                head = ptr                # Move `head` to the start of the next group
            # If count < k, we exit the loop and attach remaining nodes as they are
            else:
                break

        if ktail:                         # Attach any remaining nodes (< k) unchanged
            ktail.next = head

        return newHead if newHead else head   # If no reversal happened (k > len), return original head

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna