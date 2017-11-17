class Solution:
    seen = set()
    island_count = 0
    height = 0
    width = 0
    grid = []

    def neighbors(self, coord):         
        return [i for i in [(coord[0]-1, coord[1]),(coord[0]+1, coord[1]),(coord[0], coord[1]-1),(
                coord[0], coord[1]+1)] if self.is_valid(i) and not self.is_seen(i)]
    
    def is_valid(self, coord):
        return (coord[0] >= 0 and coord[0] < self.height) and (
                coord[1] >= 0 and coord[1] < self.width)
    
    def is_seen(self, coord):
        return coord in self.seen

    def dfs(self, coord):
        self.seen.add(coord)
        if self.grid[coord[0]][coord[1]] == '0':
            return False
        for new_coord in self.neighbors(coord):
            self.dfs(new_coord)

    def numIslands(self, grid):
        if not grid:
            return 0
        self.height = len(grid)
        self.width = len(grid[0])
        self.grid = grid
        self.seen = set()
        self.island_count = 0
        for i in range(0, self.height):
            for j in range(0, self.width):
                if not self.is_seen((i, j)):
                    if self.grid[i][j] == '1':
                        self.island_count += 1
                        self.dfs((i,j))
                    else:
                        self.seen.add((i,j))
        return self.island_count
