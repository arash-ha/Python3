

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        last, maxv = 0, 0
        res = ""
        for i in range(len(keysPressed)):
            diff = releaseTimes[i] - last
            if maxv < diff:
                maxv = diff
                res = keysPressed[i]
            elif maxv == diff and res < keysPressed[i]:
                res = keysPressed[i]
            last = releaseTimes[i]
        return res