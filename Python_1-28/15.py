grid = []
n = int(input("how big of a grid?:  "))+1

for x in range(n):
    throwaway = [0]*n
    grid.append(throwaway)
    
for x in range(n):
    grid[0][x] = 1
    grid[x][0] = 1
    
for i in range(1,n):
    for x in range(i,n):
        grid[x][i] = grid[x-1][i]+grid[x][i-1]
        grid[i][x] = grid[i-1][x] + grid[i][x-1]
        
print("your answer is",grid[n-1][n-1])




##def p_grid():
##    for line in grid:
##        print(line)

