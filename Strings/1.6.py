def string_compression(value):
    current_counter=0
    current_character=None
    result=""
    for i in value:
        if i==current_character:
            current_counter +=1
        else:
            if current_character!=None:
                result=result+current_character+str(current_counter)
            current_character=i
            current_counter=1
        print(current_character,current_counter)
    result=result+current_character+str(current_counter)
    return result
result=string_compression("aaaaabbbccccaaadd")
print(result)