**Reverse Nodes in k‑Group**, including both the iterative and recursive solutions

---

**Problem**  
Reverse every group of `k` consecutive nodes in a linked list. If the remaining nodes are fewer than `k`, leave them as is.

**Core Idea**  
- For each segment of length `k`, reverse it, then connect it to the previous reversed group.  
- Two approaches: **iterative** (process group by group) and **recursive** (reverse the first `k`, then recursively solve the rest).

---

### Iterative Approach

**Steps**  
1. Use `newHead` for the final result, `ktail` to point to the tail of the last reversed group.  
2. While there is a group of `k` nodes left:  
   - Save `head` as the start of this group.  
   - Count `k` nodes; if not enough, break.  
   - Reverse these `k` nodes using `reverseLinkedList(head, k)`.  
   - Connect: if first group → set `newHead = revHead`; else `ktail.next = revHead`.  
   - Update `ktail` to the original `head` (now the tail of the reversed group).  
   - Move `head` to the node after the reversed group (`ptr`).  
3. After loop, attach any remaining nodes: `if ktail: ktail.next = head`.  
4. Return `newHead` if any reversal happened, else original `head`.

**Helper: Reverse exactly k nodes**  
```python
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
```

**Full Iterative Code**  
```python
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(head, k):
            prev, curr = None, head
            while k > 0:
                nxt = curr.next
                curr.next = prev
                prev, curr = curr, nxt
                k -= 1
            return prev

        ptr = head
        ktail = None
        newHead = None

        while ptr:
            ptr = head
            count = 0
            while count < k and ptr:
                ptr = ptr.next
                count += 1
            if count < k:
                break

            revHead = reverse(head, k)
            if not newHead:
                newHead = revHead
            if ktail:
                ktail.next = revHead
            ktail = head
            head = ptr

        if ktail:
            ktail.next = head
        return newHead if newHead else head
```

---

### Recursive Approach

**Idea**  
- If fewer than `k` nodes remain, return `head` unchanged.  
- Otherwise, reverse the first `k` nodes, then recursively call for the rest.  
- `head` becomes the tail of the reversed segment; its `next` points to the result of the recursive call.

**Steps**  
1. **Check if enough nodes**: count `k` nodes from `curr`. If not enough, return `head`.  
2. **Reverse the first k nodes**: standard reverse of `k` nodes starting from `head`.  
3. **Recursion**: `head.next = self.reverseKGroup(curr, k)` where `curr` is the node right after the reversed group.  
4. Return the new head of the reversed segment (`prev`).

**Recursive Code**  
```python
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Check if there are at least k nodes left
        curr = head
        count = 0
        while count < k and curr:
            curr = curr.next
            count += 1
        if count < k:          # not enough nodes, keep as is
            return head

        # Reverse the first k nodes
        prev, curr = None, head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt

        # head is now the tail of the reversed segment; connect to the rest
        head.next = self.reverseKGroup(curr, k)   # curr is the first node of the next segment
        return prev
```

**Complexity**  
- **Time**: O(n) – each node visited at most twice.  
- **Space**:  
  - Iterative: O(1) extra space.  
  - Recursive: O(n/k) call stack space, which is O(n) in worst case (if k=1), but usually acceptable.

**Key Pitfalls**  
- Connecting the groups correctly: after reversing, the old `head` becomes the tail; set its `next` to the next reversed group (or remaining nodes).  
- Keeping track of the new head to return.  
- Handling the case where `k` is larger than the list length.  
- In recursive: base case must correctly count nodes before attempting reverse.

**Memory Hook**  
> “Check k, reverse k, connect tail to rest. Iterative: `ktail` keeps the joint. Recursive: tail’s `next` points to recursion result.”
