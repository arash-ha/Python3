"""
Satisfiability of Equality Equations

You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.
Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

Example 1:

Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.

Example 2:

Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
 
Constraints:

1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] is a lowercase letter.
equations[i][1] is either '=' or '!'.
equations[i][2] is '='.
equations[i][3] is a lowercase letter.
"""

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent, diff = {}, []

        def find(x):
            if x not in parent:
                return x
            else:
                return find(parent[x])

        for s in equations:
            a, b = s[0], s[3]
            if s[1] == "=":
                x, y = find(a), find(b)
                if x != y:
                    parent[y] = x
            else:    
                diff.append((a,b))
        return all(find(a) != find(b) for a, b in diff)