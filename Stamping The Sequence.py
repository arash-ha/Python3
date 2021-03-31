"""
Stamping The Sequence

You want to form a target string of lowercase letters.
At the beginning, your sequence is target.length '?' marks.  You also have a stamp of lowercase letters.
On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the corresponding letter from the stamp.  You can make up to 10 * target.length turns.
For example, if the initial sequence is "?????", and your stamp is "abc",  then you may make "abc??", "?abc?", "??abc" in the first turn.  (Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)
If the sequence is possible to stamp, then return an array of the index of the left-most letter being stamped at each turn.  If the sequence is not possible to stamp, return an empty array.
For example, if the sequence is "ababc", and the stamp is "abc", then we could return the answer [0, 2], corresponding to the moves "?????" -> "abc??" -> "ababc".
Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within 10 * target.length moves.  Any answers specifying more than this number of moves will not be accepted.

Example 1:

Input: stamp = "abc", target = "ababc"
Output: [0,2]
([1,0,2] would also be accepted as an answer, as well as some other answers.)

Example 2:

Input: stamp = "abca", target = "aabcaca"
Output: [3,0,1]

Note:

1 <= stamp.length <= target.length <= 1000
stamp and target only contain lowercase letters.
"""

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        def check(s):
            b = False
            for c1, c2 in zip(s, stamp):
                if c1 == "*":
                    continue
                elif c1 != c2:
                    return False
                else:
                    b = True
            return b
        root, move, mx, arr = "*" * len(target), 0, 10 * len(target), []
        while move < mx:
            pre = move
            for i in range(len(target) - len(stamp) + 1):
                if check(target[i : i + len(stamp)]):
                    move += 1
                    arr = [i] + arr
                    target = target[:i] + "*" * len(stamp) + target[i + len(stamp):]
            if target == root:
                return arr
            if move == pre:
                break
        return []