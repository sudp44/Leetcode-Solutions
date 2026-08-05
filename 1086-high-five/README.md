## 📘 1086. High Five

**Description**

---

Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents one score from a student with IDi, calculate each student's top five average.

Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student with IDj and their top five average. Sort result by IDj in increasing order.

A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer division.

---

**Given**  
A list `items` where `items[i] = [student_id, score]`. Multiple scores per student.

**Goal**  
For each student, compute the **average of their top 5 scores** (using integer division). Return an array of `[student_id, top_five_average]` **sorted by student_id** ascending.

**Example**
```
Input:  items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation:
  Student 1: top 5 = 100,92,91,87,65 → sum=435 → average=87
  Student 2: top 5 = 100,97,93,77,76 → sum=443 → average=88 (integer division)
```

**Constraints**  
- `1 <= items.length <= 1000`  
- `items[i].length == 2`  
- `1 <= student_id <= 1000`  
- `0 <= score <= 100`  
- Each student has at least 5 scores.