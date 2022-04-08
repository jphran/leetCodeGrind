"""
https://leetcode.com/problems/non-overlapping-intervals/

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals
you need to remove to make the rest of the intervals non-overlapping.
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        num_removed = 0
        last_included = 0
        intervals.sort(key=lambda x: (x[0], x[-1]))

        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[last_included][-1]:  # case where there's no overlap
                last_included = i
            elif intervals[i][-1] <= intervals[last_included][-1]:  # case where there's full overlap
                last_included = i
                num_removed += 1
            else:  # default case with partial overlap
                num_removed += 1

        return num_removed



if __name__ == "__main__":
    s = Solution()
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(s.eraseOverlapIntervals(intervals))
