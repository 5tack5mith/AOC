grid = []
with open("input.txt") as f:
    for line in f:
        grid.append(list(line.strip()))
sum=0
def forklift (grid,sum):
    r = len(grid)
    c = len(grid[0])
    count=0
    rem = grid
    for i in range(0,r):
        for j in range(0,c):
            p=0
            if grid[i][j]=='@':
                for k in range(i-1,i+2):
                    if k < 0 or k>r-1 :
                        continue
                    for l in range(j-1,j+2):
                        if l< 0 or l>c-1 :
                            continue
                        if grid[k][l]=="@":
                            p=p+1
                if p<=4:
                    count+=1
                    rem[i][j]="X"
    sum+=count
    grid=rem
    if(count==0):
        return sum
    else:
        return forklift(grid,sum)
print(forklift(grid,sum))
