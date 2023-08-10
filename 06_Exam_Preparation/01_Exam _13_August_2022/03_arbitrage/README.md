
**Algorithms with Python: Regular Exam**

Please submit your solutions (source code) to all below-described problems in [Judge](https://judge.softuni.org/Contests/3592).

**3. Arbitrage**

Arbitrage is the simultaneous purchase and sale of the same asset in order to profit from tiny differences in the asset's listed price. It exploits short-lived variations in the price of identical or similar financial instruments in different markets or in different forms.

You will receive a list of trading pairs and target currency to exploit arbitrage. 

Your task is write a program that detects if arbitrage is possible.
## **Input**
- On the first line you will receive an integer - n - number of the trading pairs.
- On the next n lines you will receive all trading pairs in the following format: "{from\_currency} {to\_currency} {price}".
- On the last line you will receive an integer - t - the target currency for arbitrage.
## **Output**
- On the first line print if arbitrage is possible: either True or False.
  - If arbitrage is possible print the best path separated by a space.
  - Otherwise, on the next lines, for each currency print the best possible amount that could be collected in the following format: "{currency}: {price}".
  - Price should be formatted to 3 decimal places. 
- The order of the output lines doesn't matter.
## **Constraints**
- The input will always be valid and will follow the format described in the Input section.
- n will always be an integer in the range [1… 50].
- Price for the trading pairs will be positive real numbers in the range [1… 100].
- The target currency will always be a currency from the provided trading pairs.
## **Examples**

|**Input**|**Output**|**Comments**|
| :-: | :-: | :-: |
|<p>5</p><p>GBP USD 1.27</p><p>USD AUD 1.43</p><p>USD NZD 1.51</p><p>NZD AUD 0.95</p><p>AUD GBP 0.55</p><p>GBP</p>|<p>True</p><p>GBP USD NZD AUD GBP</p>|<p>1. Let's say that we start with 1 GBP</p><p>2. 1 GBP -> USD = 1.27 USD</p><p>3. 1.27 USD -> NZD = 1.27 \* 1.51 = 1.9177 NZD</p><p>4. 1.9177 NZD -> AUD = 1.9177 \* 0.95 = 1.821815 AUD</p><p>5. 1.821815 AUD -> USD = 1.821815 \* 0.55 = 1.00199825</p><p>6. We started with 1 USD and ended with more than that, therefore arbitrage is possible.</p>|
|<p>5</p><p>GBP USD 1.27</p><p>USD AUD 1.43</p><p>USD NZD 1.51</p><p>NZD AUD 0.95</p><p>AUD GBP 0.50</p><p>GBP</p>|<p>False</p><p>GBP: 1.000</p><p>USD: 1.270</p><p>NZD: 1.918</p><p>AUD: 1.822</p><p></p>|<p>1. Let’s say that we start with 1 GBP</p><p>2. 1 GBP -> USD = 1.27 USD</p><p>3. 1.27 USD -> NZD = 1.27 \* 1.51 = 1.9177 NZD</p><p>4. 1.9177 NZD -> AUD = 1.9177 \* 0.95 = 1.821815 AUD</p><p>5. 1.821815 AUD -> USD = 1.821815 \* 0.5 = 0.9109075</p><p>6. We started with 1 USD and ended with less than that, therefore arbitrage is not possible.</p>|



