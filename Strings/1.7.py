def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j,end=" ")
        print(end="\n")
    print("\n")
def rotate_matrix_clockwise(matrix):
    length=len(matrix)
    half_length=int(length/2)
    for i in range(length):
        for j in range(i,length):
            a[i][j],a[j][i]=a[j][i],a[i][j]
    for i in range(length):
        for j in range(half_length):
            a[i][j],a[i][length-j-1]=a[i][length-j-1],a[i][j]
    return matrix
def rotate_matrix_anticlockwise(matrix):
    matrix_length=len(matrix)
    half_length=int(matrix_length/2)
    for i in range(half_length):
        for j in range(i,matrix_length-i-1):
            temp=a[i][j]
            a[i][j]=a[j][matrix_length-1-i]
            a[j][matrix_length-1-i]=a[matrix_length-1-i][matrix_length-1-j]
            a[matrix_length-1-i][matrix_length-1-j]=a[matrix_length-1-j][i]
            a[matrix_length-1-j][i]=temp

    return matrix
def rotate_matrix(matrix):
    level=0
    total_levels=int(len(matrix)/2)
    last=len(matrix)-1
    while(level<total_levels):
        for i in range(level,last):
            matrix[level][i],matrix[i][last]=matrix[i][last],matrix[level][i]
            matrix[level][i],matrix[last-i+level]=matrix[last-i+level],matrix[level][i]
            matrix[level][i],matrix[last-i+level][level]=matrix[last-i+level][level],matrix[level][i]
        level=level+1
        last=last-1
    return matrix
a=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]
print_matrix(a)
rotate_matrix(a)
print_matrix(a)