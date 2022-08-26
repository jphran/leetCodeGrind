class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        # list of blocked positions
        empty_row = "." * n
        rows = [False] * n
        cols = [False] * n
        l_diags = [False] * (2 * n - 1)
        r_diags = [False] * (2 * n - 1)

        board = [empty_row for _ in range(n)]
        soln: list[list[str]] = []

        def is_blocked(x: int, y: int) -> bool:
            return rows[y] or cols[x] or l_diags[x + y] or r_diags[x + (n - 1 - y)]

        def reserve(x: int, y: int, reserve: bool) -> None:
            if reserve:
                board[y] = empty_row[:x] + "Q" + empty_row[x + 1:]
            else:
                board[y] = empty_row
            rows[y] = reserve
            cols[x] = reserve
            l_diags[x + y] = reserve
            r_diags[x + (n - 1 - y)] = reserve

        def backtrack(y: int):
            if y == n:
                soln.append(board[:])
                return

            for x in range(n):
                if is_blocked(x, y):
                    continue

                reserve(x, y, True)
                backtrack(y + 1)
                reserve(x, y, False)

        backtrack(0)

        return soln


if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(4))