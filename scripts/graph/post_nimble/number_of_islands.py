"""
https://leetcode.com/problems/number-of-islands/
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
"""
import queue

class Solution:
    _udlr = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    _y_dim: int
    _x_dim: int

    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        self._y_dim= len(grid)
        self._x_dim = len(grid[0])
        visited: set[tuple[int, int]] = set()
        num_islands = 0

        for i in range(self._x_dim):
            for j in range(self._y_dim):
                if (i, j) in visited or grid[j][i] == "0":
                    continue
                else:
                    self._bfs(grid, (i, j), visited)
                    num_islands += 1

        return num_islands

    def _bfs(self, grid: list[list[str]], start: tuple[int, int], visited: set[tuple[int, int]]) -> None:
        q: queue[tuple[int, int]] = queue.deque()
        q.append(start)

        while len(q) != 0:
            curr_x, curr_y = q.pop()

            for x, y in self._udlr:
                new_x = curr_x + x
                if new_x < 0 or new_x >= self._x_dim:
                    continue
                new_y = curr_y + y
                if new_y < 0 or new_y >= self._y_dim:
                    continue
                new_coord = (new_x, new_y)
                if new_coord in visited:
                    continue
                visited.add(new_coord)
                if grid[new_y][new_x] == "1":
                    q.append(new_coord)


if __name__ == '__main__':
    s = Solution()
    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    print(s.numIslands(grid))
