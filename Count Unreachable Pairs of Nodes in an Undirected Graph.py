"""
Count Unreachable Pairs of Nodes in an Undirected Graph

You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.
Return the number of pairs of different nodes that are unreachable from each other.

Example 1:

Input: n = 3, edges = [[0,1],[0,2],[1,2]]
Output: 0
Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.

Example 2:

Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
Output: 14
Explanation: There are 14 pairs of nodes that are unreachable from each other:
[[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
Therefore, we return 14.
 
Constraints:

1 <= n <= 10^5
0 <= edges.length <= 2 * 10^5
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated edges.
"""
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            if visited[node]:
                return 0
            visited[node] = True
            res = 1
            for nbr in graph[node]:
                res += dfs(nbr)
            return res
        graph = {}
        for i in range(n):
            graph[i] = []
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = [False for _ in range(n)]
        components = []
        for node in range(n):
            if visited[node] == False:
                components.append(dfs(node))   

        res = n * (n - 1) // 2
        for k in components:
            res -= k * (k - 1) // 2

        return res