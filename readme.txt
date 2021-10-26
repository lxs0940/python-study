def iSP_recursive(n, k, p):          
    if n == k:
        return True
    if p == 0 and n != k:
        return False
    while p >= 1:
        if n%p != 0:
            p -= 1
        else:
            return iSP_recursive(n, k+p, p-1) or iSP_recursive(n, k, p-1)

def isSemiPerfect(n):
    if n == 1:
        return False
    p = n // 2 
    while n%p != 0:
        p -= 1
    return iSP_recursive(n, p, p-1) or iSP_recursive(n, 0, p-1)