**Logic: Contains Duplicate II (Sliding Window + Set)**

- **Goal**: Return `True` if `nums[i] == nums[j]` and `|i - j| ≤ k`.

- **Idea**: Keep a set of the last `k` elements (a sliding window).  
  For each new element, check if it’s already in the window → duplicate found.  
  If not, add it, and if the window grows beyond `k`, remove the oldest element (index `i - k`).

- **Steps**:  
  1. Initialize an empty set `seen`.  
  2. Iterate `i` from `0` to `n-1`:  
     - If `nums[i]` in `seen` → return `True`.  
     - Else, add `nums[i]` to `seen`.  
     - If `len(seen) > k` → remove `nums[i - k]` (the element that just fell out of the window).  
  3. If loop finishes → return `False`.

The removal step’s purpose is to **prepare the set for the next iteration**, ensuring that when we move to `i+1`, the set contains exactly the `k` elements that are within distance `k` of that new index.  

At the current index `i`:
1. We first check `nums[i]` against the **existing `k` elements** in the set (which represent indices `i-k ... i-1`).  
   → That’s a comparison between `nums[i]` and the previous `k` elements, covering all distances up to `k`.
2. We add `nums[i]` to the set → now it holds `k+1` elements.
3. If the set size exceeds `k`, we remove `nums[i-k]`.  
   → The set shrinks back to `k` elements, representing indices `i-k+1 ... i`.

So for the **next** index `i+1`, the set will again contain `k` elements (indices `i-k+1 ... i`).  
The cycle repeats: check the new element against those `k`, then add it, then evict the oldest.  

This pattern guarantees that for every index `i`, the element `nums[i]` is compared with **all** previous indices within distance `k` — exactly `k+1` elements are involved in the check at each step (the new one + the `k` in the set before removal).

- **Why it works**: The set always contains exactly the last `k` distinct values. Any duplicate found inside it is guaranteed to be within distance `k`.

- **Complexity**:  
  - Time: O(n) – each element is added/removed at most once.  
  - Space: O(min(n, k+1)) – the set holds at most `k+1` elements.
