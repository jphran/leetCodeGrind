"""
https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) == 1:
            return intervals

        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        output_intervals: list[list[int]] = [sorted_intervals[0]]
        for interval in sorted_intervals:
            last = output_intervals[-1][-1]
            if last < interval[0]:  # append
                output_intervals.append(interval)
            elif last < interval[-1]:  # merge
                output_intervals[-1][-1] = interval[-1]
            # else skip

        return output_intervals