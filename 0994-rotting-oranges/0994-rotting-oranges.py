class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        time, fresh = 0,0
        rows, cols = len(grid),len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    q.append([i,j])
        
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                check = [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
                for i in check:
                    R,C = i
                    if R>=0 and C>=0 and R<len(grid) and C<len(grid[0]) and grid[R][C]==1:
                        grid[R][C] = 2
                        q.append([R,C])
                        fresh-=1
            time+=1
        
        return time if fresh==0 else -1
