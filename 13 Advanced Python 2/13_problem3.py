def Divide5(n):
    if n%5 == 0:
        return True
    return False

l = [232,34,345,5,46,5,54,635,34,3534,52,4535,24,3543545,45,345,3535354353,35,353,53]
NewList = list(filter(Divide5,l))
print(NewList)