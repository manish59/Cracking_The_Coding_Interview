a=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
next_matrix=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
def path(a,row,col,b,count):
    right=(row,col+1)
    down=(row+1,col)
    if row+1<len(a):
        if not down in b:
            b[down]=1
            path(a, row + 1, col,b,count)
        else:
            b[down]=b[down]+1
        count+=1
    if col+1<len(a):
        if not right in b:
            path(a,row,col+1,b,count)
            b[right]=1
        else:
            b[right] = b[right] + 1
        count +=1
    return count
b={}
count=0
result=path(a,0,0,b,count)
print(result)
print(b)