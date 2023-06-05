def large(a): 
    max_ = a[0]
    for i in a:
        if i > max_:
           max_ = i
    return max_ 


list1 = [-19,5,10,30]
result = large(list1)
print('max=',result)
def name(b):
    min_ = b[0]
    for e in b:
        if e < min_:
           min_ = e
    return min_
result = name(list1)
print ('min=', result)       