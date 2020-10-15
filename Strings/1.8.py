def zero_rows(matrix,list_rows):
    for i in list_rows:
        matrix[i]=[0 for i in range(len(matrix[i]))]
def zero_columns(matrix,list_columns):
    for i in list_columns:
        for row in matrix:
            row[i]=0
    
def zero_matrix(matrix):
    list_rows=[]
    list_columns=[]
    length=len(matrix)
    for i in range(length):
        for j in range(len(a[i])):
            if matrix[i][j]==0:
                if i not in list_rows:
                    list_rows.append(i)
                if j not in list_columns:
                    list_columns.append(j)
    zero_rows(matrix,list_rows)
    zero_columns(matrix,list_columns)
a=[
    [1,2,3,4,5,6],
    [11,12,13,14,15,16],
    [21,22,23,0,25,26],
    [31,32,33,34,35,36],
]
def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j,end=" ")
        print(end="\n")
    print("\n")
zero_matrix(a)
print_matrix(a)