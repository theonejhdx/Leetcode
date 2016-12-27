# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda x: x.end)
        end_num = float('-inf')
        count = 0
        for interval in intervals:
            if interval.start >= end_num:
                end_num = interval.end
            else:
                count += 1

        return count

