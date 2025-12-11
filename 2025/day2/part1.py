with open("input.txt","r") as f:
    data = f.read()
    ranges = data.split(",")
    i=0
    sum=0
    for i in ranges:
        a,b=i.split("-")
        for j in range(int(a),int(b)+1):
            d = len(str(j))
            if d%2==0:
                s= str(j)
                sub1=s[:(d//2)]
                sub2=s[(d//2):]
                if sub1==sub2:
                    sum+=j
print(sum)
