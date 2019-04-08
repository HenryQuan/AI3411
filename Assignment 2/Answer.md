# Q1
|a)|UCS|IDS|A*|IDA*|
|---|---|---|---|---|
|start10|2565|2407|33|29|
|start20|Mem|5297410|915|952|
|start27|Mem|Time|1873|2237|
|start35|Mem|Time|Mem|215612|
|start43|Mem|Time|Mem|2884650|

b) 
#### UCS
#### IDS
This is a memory efficient UCS.
#### A*
#### IDA*
This is a memory efficient A*.

# Q2
**a)**
~~~
start49(S), showpos(S), h(S,H).
MBDC
LAKH
JFEI
 ONG
S = [4/1, 2/2, 1/2, 1/4, 1/3, 3/3, 3/2, 4/4, ... / ...|...],
H = 25.
~~~
~~~
start51(S), showpos(S), h(S,H).
GKJI
 MNC
EOHA
FBLD
S = [2/1, 3/4, 4/2, 2/4, 4/4, 3/1, 4/1, 1/1, ... / ...|...],
H = 43.
~~~

**b)**

551168

**c)**

It cannot find the solution so it goes deeper.

# Q3

# Q4
**a)**

Manhattan distance, h(x, y, xG, yG) = (xG - x) + (yG - y).

**b)**

i) Yes, it is still admissible since it simply measures the stright line distance. Moving diagonally does not affect it much and it might even become a better heuristic because of it.

ii) No, it is not admissible anymore becuase of diagonal move. Manhattan distance does not work diagonally because it is designed for horizontal and vertical moves.

# Q5

