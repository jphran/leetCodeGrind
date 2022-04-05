"""
https://leetcode.com/problems/pacific-atlantic-water-flow/

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches
 the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c]
 represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and
west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell
(ri, ci) to both the Pacific and Atlantic oceans.
"""

from queue import Queue
class Solution:
    _nesw = [[0, -1], [-1, 0], [0, 1], [1, 0]]

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        pacific_ocean = [[0, j] for j in range(len(heights[0]))]
        pacific_ocean.extend([[i, 0] for i in range(len(heights))])
        pacific_drainage = self._all_connected_nodes(starts=pacific_ocean, heights=heights)

        atlantic_ocean = [[len(heights) - 1, j] for j in range(len(heights[0]))]
        atlantic_ocean.extend([[i, len(heights[0]) - 1] for i in range(len(heights))])
        atlantic_drainage = self._all_connected_nodes(starts=atlantic_ocean, heights=heights)

        result = []
        for coord in pacific_drainage:
            if coord in atlantic_drainage:
                result.append(coord)

        return result

    def _all_connected_nodes(self, starts: list[list[int]], heights: list[list[int]]) -> list[list[int]]:
        """BFS return all connected nodes in drainage."""
        to_visit: queue[list[int]] = Queue()
        visited: list[list[int]] = []
        to_visit.put([starts[0][0], starts[0][1]])

        while len(to_visit.queue) != 0:
            curr_node = to_visit.get()
            if curr_node in visited:
                continue
            visited.append(curr_node)

            # where to go
            curr_height = heights[curr_node[0]][curr_node[1]]
            for dir in self._nesw:
                new_node = [curr_node[0] + dir[0], curr_node[1] + dir[1]]
                if new_node in visited:
                    continue
                if len(heights) <= new_node[0] or new_node[0] < 0 or len(heights) <= new_node[1] or new_node[1] < 0:
                    continue
                if heights[new_node[0]][new_node[1]] >= curr_height:
                    to_visit.put([new_node[0], new_node[1]])

        return visited

if __name__ == '__main__':
    s = Solution()
    input = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    output = s.pacificAtlantic(input)
    print(output)