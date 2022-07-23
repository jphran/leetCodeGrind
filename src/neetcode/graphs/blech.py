from collections import deque


class Solution:
    _directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def orangesRotting(self, grid: list[list[int]]) -> int:

        time_by_idx: dict[tuple[int, int], int] = {}
        fresh_by_idx: set[tuple[int, int]] = set()
        min_time = 0

        num_rows = len(grid)
        num_cols = len(grid[0])

        def _bfs(start: tuple[int, int]) -> tuple[int, bool]:
            q: deque[tuple[int, int]] = deque([start])
            time = 0
            has_collision = False

            while q:
                tmp = time
                for i in range(len(q)):
                    coord = q.popleft()
                    for x_offset, y_offset in self._directions:
                        new_x = coord[0] + x_offset
                        new_y = coord[1] + y_offset
                        new_coord = (new_x, new_y)

                        if 0 <= new_x < num_cols and 0 <= new_y < num_rows:
                            if new_coord in time_by_idx and time < time_by_idx[new_coord]:
                                if tmp == time:
                                    time += 1
                                time_by_idx[new_coord] = time
                                q.append(new_coord)
                                has_collision = True
                            elif grid[new_y][new_x] == 1 and new_coord not in time_by_idx:
                                if tmp == time:
                                    time += 1
                                time_by_idx[new_coord] = time
                                q.append(new_coord)
                                if new_coord in fresh_by_idx:
                                    fresh_by_idx.remove(new_coord)

            return time, has_collision

        for row_idx in range(num_rows):
            for col_idx in range(num_cols):
                coord = (col_idx, row_idx)
                val = grid[row_idx][col_idx]
                if val == 1 and coord not in time_by_idx:
                    fresh_by_idx.add(coord)
                elif val == 2:
                    t, has_collision = _bfs(coord)
                    if has_collision:
                        min_time = min(min_time, t)
                    else:
                        min_time = max(min_time, t)

        if len(time_by_idx) == 0 and len(fresh_by_idx) == 0:
            return 0
        elif len(fresh_by_idx) != 0:
            return -1
        return min_time
        # return min_time if len(fresh_by_idx) == 0 else -1

if __name__ == "__main__":
    s = Solution()
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(s.orangesRotting(grid))
