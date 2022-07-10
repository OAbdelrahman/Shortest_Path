# Shortest_Path (Greedy Algorithm)

### Programming Language
Python

### Purpose:
This program finds the shortest path in a weighted graph. <br>

### How it works:
This program takes in an adjacency matrix of a weighted graph. <br>
Hard coded for the following matrix:
[[0, 7, 0, 0, 0, 10, 15, 0],<br>
[7, 0, 12, 5, 0, 0, 0, 9],<br>
[0, 12, 0, 6, 0, 0, 0, 0],<br>
[0, 5, 6, 0, 14, 8, 0, 0],<br>
[0, 0, 0, 14, 0, 3, 0, 0],<br>
[10, 0, 0, 8, 3, 0, 0, 0],<br>
[15, 0, 0, 0, 0, 0, 0, 0],<br>
[0, 9, 0, 0, 0, 0, 0, 0]]<br>

<pre>
   2
  / \
 3---1--7
 |\  |
 4 | 0--6
  \|/
   5
</pre>

The program starts at the first node, then takes the least weight out of the available options. <br>
It keeps track of the nodes it visits and the total weight.<br>

The output for the example graph is:<br>
[[0, -1], [1, 0], [3, 1], [2, 3], [5, 3], [4, 5], [7, 1], [6, 0]] <br>

The first element [0, -1] is the start node.
