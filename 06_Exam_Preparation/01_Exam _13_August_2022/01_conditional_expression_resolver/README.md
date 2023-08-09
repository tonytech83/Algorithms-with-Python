
**Algorithms with Python: Regular Exam**

Please submit your solutions (source code) to all below-described problems in [Judge](https://judge.softuni.org/Contests/3592/).

**1. Conditional Expression Resolver**

The conditional operator ?:, also known as the ternary conditional operator, evaluates a boolean expression and returns the result of one of the two expressions, depending on whether the boolean expression evaluates to true or false.

Your task is to create a complex resolver that calculates the result for a given expression.

You can always assume that the given expression is valid and only consists of digits, ?, :, t (true) and f (false).
## **Input**
- The input will come in one line: the expression.
## **Output**
- The output is a single line: the result of the expression.
## **Constraints**
- The input will always follow this format: "{boolean value} ? {result if the value is true} : {result if the value is false}".
  - Keep in mind that both results can be expressions, too.
## **Examples**

| **Input**| **Output**| **Comments**|
|:----|:----|:----|
| t ? 4 : 2| 4| |
| f ? 4 : 2| 2| |
| f ? t ? 4 : 2 : 1| 1| (f ? (t ? 4 : 2) : 1)|
| t ? t ? t ? 4 : 1 : 2 : 3| 4| (t ? (t ? (t ? 4 : 1) : 2) : 3)|



