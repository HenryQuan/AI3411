# Q1
||UCS|IDS|A*|IDA*|
|---|---|---|---|---|
|start10|||||
|start20|||||
|start27|||||
|start35|||||
|start43|||||

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
