
def ways(r,c,dp,grid):
    if c<0 or c>=len(grid[0]):
        return 0
    if r==len(grid):
        return 1;
    if dp[r][c]!=-1:
        return dp[r][c]
    if grid[r][c]=='.':
        ans = ways(r+1,c,dp,grid)
    else :
        ans = ways(r,c-1,dp,grid)+ ways(r,c+1,dp,grid)
    dp[r][c]=ans
    return ans

grid =[]
with open ("input.txt") as f:
    for line in f:
        grid.append(list(line.strip()))
r = len(grid)
c = len(grid[0])
dp = [[-1]*c for _ in range(r)]
start=-1
for i in range(0,c):
    if grid[0][i]=='S':
        start=i
answer= ways(1,start,dp,grid)
print(answer)