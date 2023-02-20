"""
Shortest Path with Alternating Colors

You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.
You are given two arrays redEdges and blueEdges where:
redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]

Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]
 
Constraints:

1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < n
"""
from enum import Enum

class Color(Enum):
    kInit = 0
    kRed = 1
    kBlue = 2

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        res = [-1] * n
        graph = [[] for _ in range(n)]
        q = collections.deque([(0, Color.kInit)])
        for u, v in redEdges:
            graph[u].append((v, Color.kRed))

        for u, v in blueEdges:
            graph[u].append((v, Color.kBlue))

        step = 0
        while q:
            for _ in range(len(q)):
                u, prevColor = q.popleft()
                if res[u] == -1:
                    res[u] = step
                for i, (v, edgeColor) in enumerate(graph[u]):
                    if v == -1 or edgeColor == prevColor:
                        continue
                    q.append((v, edgeColor))
                    graph[u][i] = (-1, edgeColor)
            step += 1
        return res