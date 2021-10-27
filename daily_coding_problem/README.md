# Daily Coding Problems

## Index

- [Solution #928](https://github.com/mhetrerajat/ds-challenge/pull/18)
- [Solution #931](https://github.com/mhetrerajat/ds-challenge/pull/17)
- [Solution #933](https://github.com/mhetrerajat/ds-challenge/pull/16)
- [Solution #934](https://github.com/mhetrerajat/ds-challenge/pull/15)
- [Solution #942](https://github.com/mhetrerajat/ds-challenge/pull/8)
- [Solution #947](https://github.com/mhetrerajat/ds-challenge/pull/14)
- [Solution #965](https://github.com/mhetrerajat/ds-challenge/pull/23)
- [Solution #964](https://github.com/mhetrerajat/ds-challenge/pull/24)
- [Solution #973](https://github.com/mhetrerajat/ds-challenge/blob/master/daily_coding_problem/973.py)

## Problem #939

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

[Solution](./939.py)

For example, given the following matrix:

```bash
[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
```

You should print out the following:

```bash
1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
```

## Problem #940

[Solution](./940.py)

A network consists of nodes labeled 0 to N. You are given a list of edges (a, b, t), describing the time t it takes for a message to be sent from node a to node b. Whenever a node receives a message, it immediately passes the message on to a neighboring node, if possible.

Assuming all nodes are connected, determine how long it will take for every node to receive a message that begins at node 0.

For example, given N = 5, and the following edges:

```bash
edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]
```

You should return 9, because propagating the message from 0 -> 2 -> 3 -> 4 will take that much time.
