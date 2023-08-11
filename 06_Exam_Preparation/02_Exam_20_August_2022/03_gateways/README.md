
**Algorithms Fundamentals with Python**

**3. Gateways**

You are wrapping through space and time using different gateways that are connected with each other in some way. You will be given the gateways, their connections, your start gateway number, and your target gateway. Then the task is simple you need to print the shortest distance from the start to the target gateway and print the gateways you used in the process.
## **Input**
- The input will come from the console on multiple lines:
  - first line **N** single integer – the number of gateways
  - second line **M** single integer –** the number of connections
  - **M** lines describing the connections in the format: **{from} {to}**
  - **S** single integer – the start gateway
  - **T** the target gateway
## **Output**
- The output is a sequence of integers that represents the path from the start gateway to the target one.
- If there is no path found - there is no output 
## **Constraints**
- The input will not contain more than 30 gateways or connections.
## **Examples**

| **Input**|**Output**|
|:----| :-: |
| <p>6</p><p>5</p><p>1 2</p><p>2 4</p><p>3 4</p><p>6 5</p><p>6 4</p><p>1</p><p>4</p>|1 2 4|
| <p>4</p><p>4</p><p>1 4</p><p>2 3</p><p>3 4</p><p>4 1</p><p>2</p><p>1</p>|2 3 4 1|
