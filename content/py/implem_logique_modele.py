def ET(P, Q):
    if P == False:
        return False
    else:
        return Q

assert(False, False) == False
assert(False, True)  == False
assert( True, False) == False
assert( True,  True) ==  True
