import time

def prim_e(n):
    if n < 2:
        return False
    i = 2
    while (i * i <= n):
        if n % i == 0:
            return False
        i = i + 1
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


t0=time.time()
print(n_prim(10001))
t1=time.time()
print(t1-t0)