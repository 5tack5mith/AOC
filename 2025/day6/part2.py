with open("input.txt") as f:
    lines = f.read().splitlines()  #splitlines to keep spaces intact 
    number_lines = lines[:-1]
    operator_line = lines[-1]

    # now padding all the strings according to the maximum length so that we access column wise 
    max_len = max(len(line) for line in number_lines)
    number_lines = [line.ljust(max_len) for line in number_lines]
    operator_line = operator_line.ljust(max_len)
    lines =[line.ljust(max_len) for line in lines ] 
    # ljust : left justifies the text  (adds space padding to the right)

    # now finding the seperating columns 
    sep=[]
    for i in range(max_len):
        is_sep = True
        for line in number_lines:
            if line[i]!=' ':
                is_sep=False
                break
        if is_sep:  
            sep.append(i)
            
    columns =[]
    start =0
    for i in sep:
        columns.append((start,i))
        start=i+1
    if start<max_len:
        columns.append((start,max_len))
    operators=[]
    int_matrices=[]
    for a,b in columns:
        operators.append(operator_line[a:b].strip())
        matrix = []
        for line in number_lines:
            row=[]
            for ch in line[a:b]:
                if ch.isdigit():
                    row.append(int(ch))
                else:
                    row.append('')
            matrix.append(row)
        transpose=[]
        for i in range(len(matrix[0])):
            row=[]
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            transpose.append(row)
        matrix=transpose
        int_matrices.append(matrix)
print(int_matrices)
sum=0
for index,i in enumerate(int_matrices):
    if operators[index]=="*":
        res=1
    if operators[index]=="+":
        res=0
    for j in i:
        num=0   
        for k in j:
            if type(k)==int:
                num=num*10+k
        if operators[index]=="*":
            res*=num
        if operators[index]=="+":
            res+=num
    sum+=res
print(sum)


            
