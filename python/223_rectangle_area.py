class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        areaA = (C-A)*(D-B)
        areaB = (G-E)*(H-F)

        x = judgeValue(A, C, E, G)
        if x == 0:
            x = judgeValue(E, G, A, C)

        y = judgeValue(B, D, F, H)
        if y == 0:
            y = judgeValue(F, H, B, D)

        return areaA+areaB-x*y


def judgeValue(A, C, E, G):
    if A <= E and E < C and C <= G:
        return C-E
    elif A <= E and G <= C:
        return G-E
    else:
        return 0

solution = Solution()
print solution.computeArea(-2, -2, 2, 2, -3, -3, 3, -1)