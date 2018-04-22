def prim_e(b):
    db=1
    for i in range(1, b):
        if b%i==0:
            db+=1
        if db>2:
            return False
    return True

def n_prim(n):
    i=2
    while n>0:
        if prim_e(i):
            n-=1
            if n==0:
                return i
        i+=1
    return -1

print(n_prim(10001))

#print(prim_e(8))