"""
https://leetcode.com/problems/meeting-rooms-ii/

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
return the minimum number of conference rooms required.
"""
import heapq


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        min_heap = []
        intervals.sort(key=lambda x: (x[0], x[-1]))

        for interval in intervals:
            # if room exists and meeting starts after a meeting ends
            if len(min_heap) != 0 and interval[0] >= min_heap[0]:
                heapq.heappop(min_heap)
            # add the new meeting end time to the room list
            heapq.heappush(min_heap, interval[-1])

        return len(min_heap)
