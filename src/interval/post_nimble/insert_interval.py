"""
https://leetcode.com/problems/insert-interval/

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the
start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given
an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals
still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
"""


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        output_interval: list[list[int]] = []
        idx = 0
        len_intervals = len(intervals)
        if len_intervals < 1:
            return [newInterval]

        # prepend
        while idx < len_intervals and intervals[idx][0] < newInterval[0]:
            output_interval.append(intervals[idx])
            idx += 1

        # no conflict
        if len(output_interval) == 0 or output_interval[-1][-1] < newInterval[0]:
            output_interval.append(newInterval)
        else:
            output_interval[-1][-1] = max(output_interval[-1][-1], newInterval[1])

        while idx < len_intervals:
            if intervals[idx][-1] < output_interval[-1][-1]:
                # merge whole thing
                pass
            elif intervals[idx][0] > output_interval[-1][-1]:
                output_interval.append(intervals[idx])
            else:
                output_interval[-1][-1] = intervals[idx][-1]
            idx += 1

        return output_interval

if __name__ == '__main__':
    s = Solution()
    if s.insert([[1,3],[6,9]], [2, 5]) == [[1,5],[6,9]]:
        print("First Success!")
    if s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]:
        print("Second Success!")