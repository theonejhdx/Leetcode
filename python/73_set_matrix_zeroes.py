class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        n_list = []

        for i in range(m):
            flag = 0
            for j in range(n):
                if matrix[i][j] == 0:
                    if j not in n_list:
                        n_list.append(j)
                    flag = 1
            if flag == 1:
                matrix[i] = [0 for k in range(n)]

        for j in sorted(n_list):
            for i in range(m):
                matrix[i][j] = 0
        print matrix

solution = Solution()
solution.setZeroes([[0, 1]])