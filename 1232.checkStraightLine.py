class Solution:
    def checkStraightLine(self, cs: List[List[int]]) -> bool:
        delt = None
        f = 0
        l = len(cs)

        for i in range(l):
            if i == 0:
                continue
            xdelt = cs[i][0] - cs[i - 1][0]
            ydelt = cs[i][1] - cs[i - 1][1]
            if xdelt == 0:
                xdelt = ydelt

            if ydelt == 0:
                ydelt = xdelt

            if not delt:
                delt = xdelt / ydelt

            now = xdelt / ydelt

            if now != delt:
                return False

        return True