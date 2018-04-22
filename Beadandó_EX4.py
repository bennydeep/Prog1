def prim_e(b):
    db=1
    for i in range(1, b):
        if b%i==0:
            db+=1
        if db>2:
            return False
    return True

def sokadikprim(n):
    i=2
    while n>0:
        if prim_e(i):
            n-=1
            if n==0:
                return i
        i+=1
    return -1

print(sokadikprim(10001))


#print(prim_e(8))