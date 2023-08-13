
# **Algorithms Fundamentals with Python: Retake Exam**
Please submit your solutions (source code) to all the below-described problems in [Judge](https://judge.softuni.org/Contests/4048).
## **3. Roads Builder**
You have been given a list of **cities**, each represented by a **unique name**, along with the **distances between them**. Some of the roads connecting these cities are marked as **"critical"**. The distances between cities are represented as **non-negative integers**.

Your task is to design a program that **connects all the cities** with the **minimum total distance**, while also ensuring that all **critical roads connect cities through the critical road**. A road can only connect two cities and has a non-negative distance.
### **Input**
- On the first line, you will receive an integer – **e** – number of roads.
- On the next **e lines**, you will receive roads in the following format: **"{city1} {city2} {distance} {critical}"**.
  - If the road is not connecting two critical cities then the input will consist only of 3 arguments.
  - You can assume that there will be **at least 1 critical road**.
### **Output**
- Print the minimum total distance required to connect all critical, including all critical cities too.
### **Examples**

| **Input**| **Output**|
|:----|:----|
| <p>15</p><p>A D 8</p><p>D B 6 critical</p><p>A H 7</p><p>D H 10</p><p>D I 3</p><p>H I 4</p><p>B I 5 critical</p><p>I G 9</p><p>I E 20 critical</p><p>B F 4</p><p>B G 9 critical</p><p>G F 12</p><p>G C 8</p><p>F C 2</p><p>C E 14 critical</p>| 67|
| <p>5</p><p>A B 9</p><p>A D 4 critical</p><p>D B 6</p><p>D C 11 critical</p><p>B C 5</p>| 20|


