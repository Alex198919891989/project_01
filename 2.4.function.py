# Пункт А
def remove_exclamation_marks (str):
    a = str.replace('!', '') 
    return a
# Пункт В
def remove_last_em(str):
    if str [-1] == '!': 
        b = str [:-1]
    else:
        b = str
    return b    
d= input ('введите строку')
print (remove_exclamation_marks (d))
print (remove_last_em (d))