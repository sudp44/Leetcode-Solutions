## Will doing nums[insert_index] = nums[i] not disturb the array values for the next for loop iteration?
No, it won’t disturb future loop values, and here’s why:

### `insert_index` is always ≤ `i`

At the start of each loop:

- `insert_index` is the position where the **next unique number** should go.
- It only ever moves forward when a new unique is found.
- Since you increment `i` every iteration and `insert_index` at most once per iteration, `insert_index <= i` always holds.

So when you do:

```python
nums[insert_index] = nums[i]
```

you are writing to an index that is either:

- **behind `i`** → an already processed position, or
- **equal to `i`** → writing the same value into the same spot (no change).

You are **never writing ahead of `i`**, so the next loop iteration’s `nums[i]` and `nums[i+1]` remain untouched.

---

### Example trace

`nums = [1, 1, 2, 2, 3]`

| `i` | `nums[i]` | `nums[i-1]` | action | `insert_index` | array after |
|-----|-----------|-------------|--------|----------------|-------------|
| 1   | 1         | 1           | skip   | 1              | `[1,1,2,2,3]` |
| 2   | 2         | 1           | write `nums[1] = 2` | 2 | `[1,2,2,2,3]` |
| 3   | 2         | 2           | skip   | 2              | same |
| 4   | 3         | 2           | write `nums[2] = 3` | 3 | `[1,2,3,2,3]` |

Notice:

- At `i=2`, we wrote to `nums[1]`, which is **before** `i`.
- At `i=4`, we wrote to `nums[2]`, which is also **before** `i`.
- `nums[4]` and `nums[3]` for future iterations were never affected.

---

### Conclusion

The assignment `nums[insert_index] = nums[i]` is safe because it only overwrites positions that have already been processed or are the current position itself. Future iterations always read indices at or after the current `i`, so they are not disturbed.
