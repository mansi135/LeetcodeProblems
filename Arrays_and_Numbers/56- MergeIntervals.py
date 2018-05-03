# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:
#
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considerred overlapping.


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        if not intervals:
            return []

        intervals.sort(key=lambda x: x.start)

        output = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i].start <= output[-1].end:
                output[-1].end = max(output[-1].end, intervals[i].end)
            else:
                output.append(intervals[i])

        return output

#         i = 0

#         while i < len(intervals)-1:

#             if intervals[i].end >= intervals[i+1].start:
#                 start = min(intervals[i].start, intervals[i+1].start)
#                 end = max(intervals[i].end, intervals[i+1].end)
#                 i += 2
#             else:
#                 start = intervals[i].start
#                 end = intervals[i].end
#                 i += 1
#             output.append(Interval(start,end))

#         if i == len(intervals)-1:
#             output.append(intervals[i])

#         if len(output) == len(intervals):
#             return output
#         else:
#             return self.merge(output)


