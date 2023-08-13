
# **Algorithms Fundamentals with Python: Retake Exam**
Please submit your solutions (source code) to all the below-described problems in [Judge](https://judge.softuni.org/Contests/4048).
## **2. Stock Prices**
You are a data scientist working for a financial firm, and you are tasked with analyzing the stock prices of a particular company to identify the longest continuous upward trend in the stock price history. 

Specifically, you are given a database that contains the **daily closing prices** of the stock for a given period, represented as an **array of n integers**. You are also given a **limit k** on the **maximum change** allowed between any two **adjacent prices**.

Write a program that takes an array of **daily closing prices** and a **limit k** as input, and outputs the **longest sequence (does not have to be a contiguous subsequence) of increasing stock prices** over a continuous period.
### **Input**
- A sequence of **n integers** representing the daily closing prices of the stock for a given period in the following format: **"{price1}, {price2}, …, {priceN}"**.
- An integer **k** representing the maximum change allowed between any two adjacent prices.
### **Output**
- The longest continuous upward trend in the following format: **"{price1} {price2} … {priceN}"**.
### **Constraints**
- The count of prices will be in the range **[1… 100]**.
- The daily closing prices are integers in the range **[1… 1000]**.
- The maximum allowed change will be in the range **[1… 100]**.
### **Examples**

| **Input**| **Output**|
|:----|:----|
| <p>1, 3, 2, 5, 4, 7, 6, 8</p><p>1</p>| 1 2|
| <p>1, 21, 3, 19, 5, 17, 7, 15, 9, 10</p><p>2</p>| 1 3 5 7 9 10|


