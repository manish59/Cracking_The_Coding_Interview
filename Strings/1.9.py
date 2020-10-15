def string_rotation(s1,s2):
    #waterbottle
    #erbottlewa
    if len(s1)!=len(s2):
        return False
    temp=s1+s1
    if temp.find(s2):
        return True
    return False
result=string_rotation("waterabottle","bottlewatera")
print(result)