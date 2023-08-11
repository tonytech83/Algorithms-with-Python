
# **Algorithms Fundamentals with Python: Exam**
Please submit your solutions (source code) to all the below-described problems in [Judge](https://judge.softuni.org/Contests/4044).
## **3. Goals**
You are given a list of numbers, representing the goals scored by a football team in each match played in the current season. You want to find the best sequence of matches where the **number of goals scored increases from one match to the next**. 

For example, if the team's goal scores are [0, 1, 3, 2, 4, 6, 5], then the best subsequence is 5, corresponding to the sequence [0, 1, 3, 4, 6].

Assume that **ties are allowed**, i.e., a match where the team scores the **same number of goals** as in the previous match is considered to be **increasing**.
### **Input**
- On the first line, you will receive the sequence of goals in the following format: **"{first\_match\_goals}, {second\_match\_goals}, …, {n\_match\_goals}"**.
### **Output**
- Print the best sequence in the following format: **"{first\_seq\_goals} … {n\_seq\_goals}"**.
### **Constraints**
- Numbers will be integers in the range **[1… 10]**.
- You may assume that the input list contains at least one element.
### **Examples**

|**Input**|**Output**|
| :-: | :-: |
|0, 1, 3, 2, 4, 6, 5|0 1 3 4 6|
|2, 2, 1, 5, 4, 6, 7, 3|2 2 5 6 7|

