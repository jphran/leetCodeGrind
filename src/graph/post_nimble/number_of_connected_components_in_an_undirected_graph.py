"""
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

You have a graph of n nodes. You are given an integer n and an array edges where
edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.
"""
from collections import defaultdict, deque


class Solution:
    _visited: set[int]

    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        if n <= 0:
            return 0

        # Construct adjacency list.
        graph: dict[int, list[int]] = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        self._visited = set()
        num_connected = 0

        for i in range(n):
            if i in self._visited:
                continue
            num_connected += 1
            self._bfs_expand_all_nodes(i, graph)

        return num_connected

    def _bfs_expand_all_nodes(self, start: int, graph: dict[int, list[int]]) -> None:
        to_visit_queue: deque[tuple[int, int]] = deque()
        to_visit_queue.append((start, -1))  # node, parent

        while len(to_visit_queue) != 0:
            curr_node, parent = to_visit_queue.popleft()

            if curr_node in self._visited:
                continue

            self._visited.add(curr_node)

            for neighbor in graph[curr_node]:
                if neighbor != parent:
                    to_visit_queue.append((neighbor, curr_node))
