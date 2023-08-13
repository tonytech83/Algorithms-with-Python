
# **Algorithms Fundamentals with Python: Retake Exam**
Please submit your solutions (source code) to all the below-described problems in [Judge](https://judge.softuni.org/Contests/4048).
## **1. Sum Finder**
Given a set of **n positive integers**, find all possible subsets of the set that have a sum **less than or equal to a target sum.**

For example, given the input list **[2, 4, 5, 8, 9]** and a target sum of **10**, the program should return the following list of valid subsets: **[[2], [4], [5], [2, 4], [2, 5], [8], [4, 5], [9], [2, 8]]**
### **Input**
1. A list of **n positive integers**, nums. (1 <= **n** <= 20).
- A target sum, target. (1 <= **target** <= 1000).
### **Output**
- A list of all valid subsets of the nums list, where each subset is represented as a list of integers.
  - A subset is considered valid if the sum of its elements is **less than or equal to the target sum**.
- The subsets in the output should be sorted in ascending order, and each subset should be printed on a separate line, with its elements separated by a single space.
### **Examples**

| **Input**| **Output**|
|:----|:----|
| <p>2, 4, 5, 8, 9</p><p>10</p>| <p>2</p><p>2 4</p><p>2 5</p><p>2 8</p><p>4</p><p>4 5</p><p>5</p><p>8</p><p>9</p>|
| <p>3, 4, 5, 6, 7</p><p>12</p>| <p>3</p><p>3 4</p><p>3 4 5</p><p>3 5</p><p>3 6</p><p>3 7</p><p>4</p><p>4 5</p><p>4 6</p><p>4 7</p><p>5</p><p>5 6</p><p>5 7</p><p>6</p><p>7</p>|


