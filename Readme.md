# Coin Changing Algorithms Comparison

#
To Run this python script you can use the Below mentioned command

```python3 main.py <change_needed> <no of denomination> <denomination of currency comma serprated>```
##
The above command will generate output for both the algorithms also if you want to run the  algorithm Individually you can use below mentioned commands:
```
python3 coin_change_greedy.py  <change_needed> <no of denomination> <denomination of currency comma serprated>
python3 recursion.py  <change_needed> <no of denomination> <denomination of currency comma serprated>
python3 coin_change_dp.py  <change_needed> <no of denomination> <denomination of currency comma serprated>
```
## Ouput time is in microseconds
##
The output will be generated in output.txt which will include 
>Coin Used, Time taken , Algo used (for greedy algo)
Minimum coin-count, Time taken ,Algo used(for recursion)
Coin Used, Time taken , Algo used (for dp algo)
_example:-_

```
Coin Used: [10, 1]
Time taken: 9
Algo used: greedy

Minimum coin-count: 2
Time taken: 250
Algo used: recursion


Coin Used: [10, 1]
Time taken: 25
Algo used: dp
```




#For individual algorithm filename should be recursion.py for recursive, coin_change_greedy.py for rreedy solution and coin_change_dp.py for dynamic programming solution of change-making problem.

and then Enter the amount
Example: Enter n (total change in cents): 10

after that enter the number of denomination
Example: Enter number of denominations k: 4

after that enter the available  denominations
Example: Enter denomination array d of size k : 1,2,3,4


#
To Run the whole code at once user can use shell script i.e.

``` bash bash.sh```

