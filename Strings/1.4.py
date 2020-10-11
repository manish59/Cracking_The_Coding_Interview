def check_permutation_palindrome(value):
    d={}
    check_flag=0
    for i in value.upper():
        if i!=" ":
            if i not in d:
                d[i]=1
                check_flag 
            else:
                d[i]+=1
    print(d)
    check_odd_flag=0
    for i in d:
        if d[i]%2==1:
            check_odd_flag+=1
    return check_odd_flag <2   
def check_permutation_without_flag(value):
    d={}
    check_flag=0
    for i in value.upper():
        if i!=" ":
            if i not in d:
                d[i]=1
            else:
                check_flag -=1
                d[i]=d[i]+1
            if d[i]%2!=0:
                check_flag +=1
        print(check_flag)
    return check_flag<2

result=check_permutation_palindrome("Tact Coa")
result1=check_permutation_without_flag("taco cat")
print(result1)