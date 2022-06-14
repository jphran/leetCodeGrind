"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
"""
from collections import deque
from typing import Final


class Solution:
    _DIRECTIONS: Final = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        max_y = len(heights)
        max_x = len(heights[0])
        touches_pacific: set[tuple[int, int]] = {(0, y) for y in range(max_y)}
        touches_pacific.update({(x, 0) for x in range(max_x)})
        touches_atlantic: set[tuple[int, int]] = {(max_x - 1, y) for y in range(max_y)}
        touches_atlantic.update({(x, max_y - 1) for x in range(max_x)})

        def _all_drainage_nodes(starts: set[tuple[int, int]]) -> set[tuple[int, int]]:
            q: deque[tuple[int, int]] = deque(starts)
            visited: set[tuple[int, int]] = set()
            connected: set[tuple[int, int]] = set()

            while q:
                coords = q.pop()
                # prune path
                if coords in visited:
                    continue
                visited.add(coords)

                for x_offset, y_offset in self._DIRECTIONS:
                    new_x = coords[0] + x_offset
                    new_y = coords[1] + y_offset
                    if not (0 <= new_x < max_x):
                        continue
                    if not (0 <= new_y < max_y):
                        continue
                    new_coords = (new_x, new_y)
                    if heights[new_y][new_x] >= heights[coords[1]][coords[0]]:
                        connected.add(new_coords)
                        q.append(new_coords)

            return connected

        touches_pacific.update(_all_drainage_nodes(touches_pacific))
        touches_atlantic.update(_all_drainage_nodes(touches_atlantic))

        touches_both: list[list[int]] = []
        for coords in touches_atlantic:
            if coords in touches_pacific:
                touches_both.append([coords[1], coords[0]])

        return touches_both


if __name__ == "__main__":
    s = Solution()
    heights = [[1, 1], [1, 1], [1, 1]]
    print(s.pacificAtlantic(heights))
