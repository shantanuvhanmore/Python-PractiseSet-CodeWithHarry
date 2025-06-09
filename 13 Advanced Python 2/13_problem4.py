from functools import reduce
l = [232,34,345,5,46,5,54,635,34,3534,52,4535,24,3543545,45,345,3535354353,35,353,53]

def great(a,b):
    if(a>b):
        return a
    return b

val = reduce(great,l)
print(val)