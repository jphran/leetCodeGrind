"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
from collections import deque


class Solution:
    _adjacent = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def _bfs(
        self,
        grid: list[list[str]],
        start: tuple[int, int],
        visited: set[tuple[int, int]],
    ) -> None:
        """Simple bfs to find all attached landmass to start."""
        q: deque[tuple[int, int]] = deque()
        q.append(start)

        while q:
            curr_coord = q.popleft()
            for x_offset, y_offset in self._adjacent:
                new_x = curr_coord[0] + x_offset
                new_y = curr_coord[1] + y_offset
                # is new coord valid
                if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
                    new_coord = (new_x, new_y)
                    # have we visited
                    if new_coord not in visited:
                        visited.add(new_coord)
                        # is it land
                        if grid[new_y][new_x] == "1":
                            q.append(new_coord)

    def numIslands(self, grid: list[list[str]]) -> int:
        visited: set[tuple[int, int]] = set()
        num_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                new_coord = (j, i)
                if new_coord not in visited:
                    visited.add(new_coord)
                    if grid[i][j] == "1":
                        num_islands += 1
                        self._bfs(grid, new_coord, visited)

        return num_islands


if __name__ == "__main__":
    s = Solution()
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print(s.numIslands(grid))
