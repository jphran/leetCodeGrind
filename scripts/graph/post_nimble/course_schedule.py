"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must
take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Need to detect a cycle.
        if not prerequisites:
            return True

        # Build a graph
        course_graph: dict[int, list[int]] = defaultdict(list)
        for req in prerequisites:
            course_graph[req[1]].append(req[0])

        visited: set[int] = set()
        sorted_nodes: list[int] = []

        for curr_course in range(numCourses):
            if self.is_cyclic(curr_course, course_graph, visited, sorted_nodes):
                return False

        return True

    def is_cyclic(self, curr_course, course_graph, visited, sorted_nodes) -> bool:
        """Detects cycles in a graph."""
        if curr_course in visited:
            return False
        if curr_course in sorted_nodes:
            return True

        # post-order dfs
        sorted_nodes.append(curr_course)

        for neighbor in course_graph[curr_course]:
            if self.is_cyclic(neighbor, course_graph, visited, sorted_nodes):
                return True

        visited.add(curr_course)

        return False

