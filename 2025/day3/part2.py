def joltage(s,e,arr,n):
    if s>=len(arr) or e>len(arr):
        return n
    m=-1
    selected=s
    for i in range(s,e):
        if m<arr[i]:
            m=arr[i]
            selected = i
    n=n*10+arr[selected]
    return joltage(selected+1,e+1,arr,n)


with open("input.txt") as f:
    total=0
    for line in f:
        arr = [int(ch) for ch in line.strip()]
        l=len(arr)
        total+=joltage(0,l-12+1,arr,0)
    print(total)