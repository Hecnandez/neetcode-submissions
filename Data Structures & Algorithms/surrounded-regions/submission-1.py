class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visits = set()

        def bfs(r, c):
            current = [(r, c)]
            touchesEdge = r == 0 or r == rows - 1 or c == 0 or c == cols - 1

            visits.add((r, c))
            q = deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [1, 0], [-1, 0], [0, 1], [0, -1]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        r in range(rows)
                        and c in range(cols)
                        and (r, c) not in visits
                        and board[r][c] == "O"
                    ):
                        visits.add((r, c))
                        current.append((r, c))
                        q.append((r, c))
                        if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                            touchesEdge = True

            print(current)
            if not touchesEdge:
                for row, col in current:
                    board[row][col] = "X"

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visits:
                    bfs(r, c)
