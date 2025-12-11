with open("input.txt","r") as f:
    data = f.read()
    ranges = data.split(",")
    sum=0
    for i in ranges:
        a,b=i.split("-")
        for j in range(int(a),int(b)+1):
            l=len(str(j))
            s = str(j)
            ds=s+s
            for k in range(1,l):
                if ds[k:k+l]==s:
                    sum+=j
                    break

print(sum)
