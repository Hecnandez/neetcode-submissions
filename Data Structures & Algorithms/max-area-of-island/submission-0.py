class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visits = set()
        self.best = 0

        def bfs(r, c):
            area = 1
            q = collections.deque()
            visits.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        r in range(rows)
                        and c in range(cols)
                        and grid[r][c] == 1
                        and (r, c) not in visits
                    ):
                        q.append((r, c))
                        visits.add((r, c))
                        area += 1

            self.best = max(self.best, area)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visits:
                    bfs(r, c)

        return self.best
