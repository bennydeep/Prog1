def prim_e(b):
    db=1
    for i in range(1, b):
        if b%i==0:
            db+=1
        if db>2:
            return False
    return True

print(prim_e(8))