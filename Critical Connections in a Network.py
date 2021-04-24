"""
Critical Connections in a Network

There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.
A critical connection is a connection that, if removed, will make some server unable to reach some other server.
Return all critical connections in the network in any order.

Example 1:

Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
"""

class Solution:
    def __init__(self):
        self.critical = []

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(node, parent, index):
            lows[node] = index

            for child in c_dic[node]:
                if child == parent:
                    continue
                elif lows[child] == -1:
                    lows[node] = min(lows[node], dfs(child, node, index+1))
                else:
                    lows[node] = min(lows[node], lows[child])        
            if lows[node] == index and node != 0:
                self.critical.append([parent, node])
            return lows[node]

        lows = [-1] * n
        c_dic = defaultdict(set)
        for u, v in connections:
            c_dic[u].add(v)
            c_dic[v].add(u)
        dfs(0, -1, 0)

        return self.critical