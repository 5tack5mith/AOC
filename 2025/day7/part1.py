# laser function traces the tachyon beam's path
def laser (grid,i,j):
    k=i
    while k<len(grid):
        if grid[k][j]=="^":
            break
        grid[k][j]="|"
        k+=1
grid =[]
with open ("input.txt") as f:
    for line in f:
        grid.append(list(line.strip()))
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]=="S":
            laser(grid,i+1,j)
        if grid[i][j]=="^":
            laser(grid,i,j-1)
            laser(grid,i,j+1)

for row in grid:
    print("".join(row))

count=0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]=="^":
            if grid[i-1][j]=="|":
                count+=1
print(count)