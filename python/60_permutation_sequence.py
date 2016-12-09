class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        a = [i+1 for i in range(n)]
        b = []
        import math
        while n > 0:
            c = (k-1)/math.factorial(n-1)+1
            k %= math.factorial(n-1)
            b.append(str(a[c-1]))
            del a[c-1]
            n -= 1

        return ''.join(b)

solution = Solution()
print solution.getPermutation(4,18)