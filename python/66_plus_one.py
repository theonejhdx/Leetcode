class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Method one
        # digits = [str(x) for x in digits]
        # number = int(''.join(digits)) + 1
        # return [int(x) for x in list(str(number))]

        # Method two
        flag = 1
        for i in range(0, len(digits))[::-1]:
            if flag == 1:
                if digits[i] == 9:
                    flag = 1
                    digits[i] = 0
                else:
                    flag = 0
                    digits[i] += 1
        if flag == 1:
            digits.insert(0, 1)
        return digits

solution = Solution()
print solution.plusOne([9])