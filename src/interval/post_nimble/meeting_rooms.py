"""
https://leetcode.com/problems/meeting-rooms/

Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings.
"""

# WORKING FIRST TRY SOLN, now complete w out sorting
class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for idx in range(1, len(intervals)):
            if intervals[idx][0] < intervals[idx - 1][-1]:
                return False

        return True
