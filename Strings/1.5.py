def one_away(value1,value2):
    result=value1+value2
    d={}
    check_flag=0
    for i in result:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
            check_flag -=1
        if d[i]%2!=0:
            check_flag +=1
    print(check_flag)
    return (check_flag<=1 and check_flag>=0)
def second_one_way(value1,value2):
    d={}
    edit_counter=0
    for i in value1:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
    for i in value2:
        if i not in d:
            edit_counter=edit_counter+1  
    return edit_counter<=1
print(second_one_way("pale","ple"))
print(second_one_way("pales","pale"))
print(second_one_way("pale","bale"))
print(second_one_way("pale","bake"))
