class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        dic = {}

        for l in list(s):
            if l not in dic:
                dic[l] = 1
            else:
                dic[l] += 1

        result_list = sorted(dic.iteritems(), key=lambda x:x[1], reverse=True)
        result = ''
        for item in result_list:
            result += item[0]*item[1]

        return result

solution = Solution()
solution.frequencySort('tree')