# OU
def OU(P, Q):
    if P == False:
        return Q
    else:
        return True

# NON

def non1(P):
    if P == True:
        return False
    if P == False:
        return True

def non2(P):
    if P == True:
        return False
    else:
        return True

def non3(P):
    if P == True:
        return False
    return True

def non4(P):
    if P:
        return False
    else:
        return True

def non5(P):
    return not P
