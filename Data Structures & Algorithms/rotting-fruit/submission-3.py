class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visits = set()
        goodCount = 0
        
        def rotFruit(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in visits or grid[r][c] != 1:
                return
            q.append((r, c))
            visits.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visits.add((r, c))
                elif grid[r][c] == 1:
                    goodCount += 1
        
        if len(q) == 0 and goodCount == 0:
            return 0

        minutes = -1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                rotFruit(r + 1, c)
                rotFruit(r - 1, c)
                rotFruit(r, c + 1)
                rotFruit(r, c - 1)

            minutes += 1

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1 
                    
        return minutes
