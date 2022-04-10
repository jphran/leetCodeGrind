from collections import defaultdict, deque


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if n <= 1:
            return True

        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited: set[int] = set()
        finished: set[int] = set()
        to_visit: deque[tuple[int, int]] = deque()
        to_visit.append((0, -1))

        while len(to_visit) != 0:
            curr_node, parent = to_visit.pop()

            # Graph contains cycle, invalid tree.
            if curr_node in visited:
                return False

            # Mark the node.
            visited.add(curr_node)

            for neighbor in graph[curr_node]:
                # Node has already been fully expanded
                if neighbor in finished:
                    continue
                if neighbor != parent:
                    to_visit.append((neighbor, curr_node))

        return len(visited) == n
