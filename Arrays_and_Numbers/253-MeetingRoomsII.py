'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
'''


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        d = {}

        d[intervals[0].end] = 1

        rooms = 1

        for i in range(1, len(intervals)):
            key = min(d.keys())
            print(key)
            if intervals[i].start >= key:
                d[key] -= 1
                if d[key] == 0:
                    del d[key]
            else:
                rooms += 1
            d[intervals[i].end] = d.get(intervals[i].end, 0) + 1

        return rooms